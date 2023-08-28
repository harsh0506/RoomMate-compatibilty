from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
db = SQLAlchemy(app)

class UserData(db.Model):
    __tablename__ = 'UserData'
    id = Column(Integer, primary_key=True)
    RoomSharingPrefrence = Column(Boolean)
    YourGender = Column(String(255))
    GenderPref = Column(String(255))
    Budget = Column(String(255))
    AgeRange = Column(String(255))
    FriendshipChoice = Column(String(255))
    PersonalityTrait = Column(String(255))
    DailyRoutine = Column(String(255))
    RoommatesDailyRoutine = Column(String(255))
    DietryPref = Column(String(255))
    Personality = Column(String(255))
    SocialStatus = Column(String(255))
    YourOccup = Column(String(255))
    RoommateOccup = Column(String(255))
    MoviePref = Column(String(255))
    CitiPref = Column(String(255))
    Cleanliness = Column(String(255))
    SkillsCookClean = Column(Integer)
    ComforWithCompany = Column(String(255))
    ConflictResolution = Column(String(255))
    Boundaries = Column(String(255))
    createdAt = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updatedAt = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.utcnow)
    deletedAt = Column(TIMESTAMP)

@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.json  # Assuming JSON data is sent in the request
    new_data = UserData(**data)
    
    try:
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"message": "Data stored successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@app.route("/",methods=["GET"])
def see():
    return jsonify({"msg":"jhbbewb"})    

if __name__ == '__main__':
    app.run(debug=True)
