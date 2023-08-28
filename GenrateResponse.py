import random
import asyncio
import aiohttp
import time

def generate_roomte_testanswer():
    # Corresponding lists of answers for each column
    RoomSharingPrefrence = random.choice([True , False])
    YourGender = random.choice(["Male", "Female", "Prefer not to say", "Other"])
    GenderPref = random.choice(["Male", "Female", "Prefer not to say", "Other"])
    Budget = random.choice(["0-5000", "5000-10000", "10000-15000"])
    AgeRange = random.choice(["less than 20", "20-25", "25-30"])
    FriendshipChoice = random.choice([
        "Yes, I'm looking for a friend.",
        "I'm open to it, but it's not a necessity.",
        "No, I prefer to keep it professional."
    ])
    PersonalityTrait = random.choice(["Compatibility in Tastes and Habits", "Willingness to Explore New Activities and Places"])
    DailyRoutine = random.choice(["morning person", "night person"])
    RoommatesDailyRoutine = random.choice(["Morning", "night", "Both"])
    DietryPref = random.choice(["veg", "non-veg", "vegan", "Other"])
    Personality = random.choice(["Introvert", "Extrovert", "Ambivert"])
    SocialStatus = random.choice([
        "I'm a social butterfly, love it!",
        "I enjoy some socializing but also value my alone time.",
        "I'm more of an introvert, prefer quiet evenings."
    ])
    YourOccup = random.choice(["Student", "Working Professional", "Looking for Job/Education", "Entrepreneur", "Freelancer"])
    RoommateOccup = random.choice(["Student", "Working Professional", "Looking for Job/Education"])
    MoviePref = random.choice(["Comedy", "Fiction", "Thriller", "Action", "Sad (Romantic)", "Sci-Fi"])
    CitiPref = random.choice(["Mumbai", "Navi Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Greater Noida"])
    Cleanliness = random.choice([
        "I'm diligent about cleaning and enjoy maintaining a tidy space.",
        "I'm fairly organized but don't mind some mess.",
        "I'm more relaxed about cleaning and don't mind clutter."
    ])
    SkillsCookClean = random.choice([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])
    ComforWithCompany = random.choice([
        "I enjoy company and having people over.",
        "It depends on the situation.",
        "I prefer to keep my space private."
    ])
    ConflictResolution = random.choice([
        "I prefer open and direct communication.",
        "I like to find solutions collaboratively.",
        "I tend to avoid confrontation and handle issues privately."
    ])
    Boundaries = random.choice([
        "I believe in clear and open communication about boundaries and expectations from the start.",
        "I'm comfortable discussing boundaries when necessary, but I also value flexibility.",
        "I prefer a more relaxed approach and tend to go with the flow without setting strict boundaries."
    ])


    data = {
        "roomsharingprefrence": RoomSharingPrefrence,
        "yourgender": YourGender,
        "genderpref": GenderPref,
        "budget": Budget,
        "agerange": AgeRange,
        "friendshipchoice": FriendshipChoice,
        "personalitytrait": PersonalityTrait,
        "dailyroutine": DailyRoutine,
        "roommatesdailyroutine": RoommatesDailyRoutine,
        "dietrypref": DietryPref,
        "personality": Personality,
        "socialstatus": SocialStatus,
        "youroccup": YourOccup,
        "roommateoccup": RoommateOccup,
        "moviepref": MoviePref,
        "citipref": CitiPref,
        "cleanliness": Cleanliness,
        "skillscookclean": SkillsCookClean,
        "comforwithcompany": ComforWithCompany,
        "conflictresolution": ConflictResolution,
        "boundaries": Boundaries,
    }

    return data


async def send_post_request(session, data):
    headers = {'Content-Type': 'application/json'}

    url = 'http://localhost:5000/store_data'
    try:
        async with session.post(url, headers=headers, json=data) as response:
            print(await response.json())
            return await response.json()
    except aiohttp.ClientError as e:
        print("Error:", e)


async def main():
    start_time = time.time()

    num_requests = 10000
    reviews = [generate_roomte_testanswer() for _ in range(num_requests)]

    async with aiohttp.ClientSession() as session:
        tasks = [send_post_request(session, data) for data in reviews]
        results = await asyncio.gather(*tasks)

    end_time = time.time()

    print(
        f"Time taken to send {num_requests} POST requests: {end_time - start_time:.6f} seconds")
    


if __name__ == "__main__":
    asyncio.run(main())        










