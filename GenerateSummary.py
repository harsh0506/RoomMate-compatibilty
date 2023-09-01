def generate_text(data):
    text = []

    if data.get('roomsharingprefrence'):
        text.append("I'm totally open to sharing a room, it's a great way to save on expenses and make new friends.")
    
    if data.get('yourgender'):
        text.append(f"As for my gender, I'm a {data['yourgender'].lower()}, and I'm looking for a {data['genderpref'].lower()} roommate too.")
    
    if data.get('budget'):
        text.append(f"Talking about budget, I'm comfortable with the range of {data['budget']}.")

    if data.get('agerange'):
        text.append(f"In terms of age, I'm in the range of {data['agerange']} years old.")
    
    if data.get('friendshipchoice'):
        text.append(data['friendshipchoice'])

    if data.get('personalitytrait'):
        text.append(f"When it comes to personality traits, I think {data['personalitytrait'].lower()} is crucial for a harmonious living arrangement.")

    if data.get('dailyroutine'):
        text.append(f"My daily routine is that of a {data['dailyroutine'].lower()}.")

    if data.get('roommatesdailyroutine'):
        text.append(f"I'm quite adaptable when it comes to roommates' daily routines, so I'm good with both early birds and night owls.")

    if data.get('moviepref'):
        text.append(f"As for movies, I'm a fan of {data['moviepref'].lower()}. Laughter is something I can't resist.")

    if data.get('citipref'):
        text.append(f"I have a soft spot for the city of {data['citipref']}.")

    if data.get('cleanliness'):
        text.append(data['cleanliness'])

    if data.get('skillscookclean'):
        text.append(f"On a scale of 1 to 5, my cooking and cleaning skills are around {data['skillscookclean']}.")

    if data.get('comforwithcompany'):
        text.append(data['comforwithcompany'])

    if data.get('conflictresolution'):
        text.append(f"In terms of conflict resolution, I prefer {data['conflictresolution'].lower()}. It's the best way to solve any issues.")

    if data.get('boundaries'):
        text.append(f"Setting boundaries is important. {data['boundaries']}")

    return "\n\n".join(text)

# Example usage:
data = {
    'roomsharingprefrence': True,
    'yourgender': 'Male',
    'genderpref': 'Male',
    'budget': '5000-10000',
    'agerange': '20-25',
    'friendshipchoice': 'Yes, I\'m looking for a friend.',
    'personalitytrait': 'Compatibility in Tastes and Habits',
    'dailyroutine': 'morning person',
    'roommatesdailyroutine': 'Both',
    'moviepref': 'Comedy',
    'citipref': 'Mumbai',
    'cleanliness': 'I\'m diligent about cleaning and enjoy maintaining cleanliness.',
    'skillscookclean': 3,
    'comforwithcompany': 'I enjoy company and having people over.',
    'conflictresolution': 'I prefer open and direct communication.',
    'boundaries': 'I believe in clear and open communication about boundaries.'
}

resulting_text = generate_text(data)
print(resulting_text)
