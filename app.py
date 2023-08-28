from flask import Flask, request, jsonify, send_file, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd
import time 

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
db = SQLAlchemy(app)


class UserData(db.Model):
    __tablename__ = 'userdata'
    id = Column(Integer, primary_key=True)
    roomsharingprefrence = Column(Boolean)
    yourgender = Column(String(255))
    genderpref = Column(String(255))
    budget = Column(String(255))
    agerange = Column(String(255))
    friendshipchoice = Column(String(255))
    personalitytrait = Column(String(255))
    dailyroutine = Column(String(255))
    roommatesdailyroutine = Column(String(255))
    dietrypref = Column(String(255))
    personality = Column(String(255))
    socialstatus = Column(String(255))
    youroccup = Column(String(255))
    roommateoccup = Column(String(255))
    moviepref = Column(String(255))
    citipref = Column(String(255))
    cleanliness = Column(String(255))
    skillscookclean = Column(Integer)
    comforwithcompany = Column(String(255))
    conflictresolution = Column(String(255))
    boundaries = Column(String(255))
    createdat = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updatedat = Column(TIMESTAMP, server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=datetime.utcnow)
    deletedat = Column(TIMESTAMP)


def data_to_dict(data):
    return {
        "id": data.id,
        "roomsharingprefrence": data.roomsharingprefrence,
        "yourgender": data.yourgender,
        "genderpref": data.genderpref,
        "budget": data.budget,
        "agerange": data.agerange,
        "friendshipchoice": data.friendshipchoice,
        "personalitytrait": data.personalitytrait,
        "dailyroutine": data.dailyroutine,
        "roommatesdailyroutine": data.roommatesdailyroutine,
        "dietrypref": data.dietrypref,
        "personality": data.personality,
        "socialstatus": data.socialstatus,
        "youroccup": data.youroccup,
        "roommateoccup": data.roommateoccup,
        "moviepref": data.moviepref,
        "citipref": data.citipref,
        "cleanliness": data.cleanliness,
        "skillscookclean": data.skillscookclean,
        "comforwithcompany": data.comforwithcompany,
        "conflictresolution": data.conflictresolution,
        "boundaries": data.boundaries,
        "createdat": data.createdat.strftime('%Y-%m-%d %H:%M:%S'),
        "updatedat": data.updatedat.strftime('%Y-%m-%d %H:%M:%S'),
        "deletedat": data.deletedat.strftime('%Y-%m-%d %H:%M:%S') if data.deletedat else None
    }


@app.route('/store_data', methods=['POST'])
def store_data():
    data = request.get_json()
    new_data = UserData(**data)

    try:
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"message": "Data stored successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def see():
    return jsonify({"msg": "jhbbewb"})


@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    try:
        start_time = time.time()
        all_data = UserData.query.all()
        data_list = [data_to_dict(data) for data in all_data]
        end_time = time.time()

        print(f"Time taken to send  POST requests: {end_time - start_time:.6f} seconds")

        return jsonify(data_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download_csv', methods=['GET'])
def download_csv():
    try:
        all_data = UserData.query.all()
        data_list = [data_to_dict(data) for data in all_data]

        df = pd.DataFrame(data_list)
        csv_data = df.to_csv(index=False)

        response = make_response(csv_data)
        response.headers['Content-Type'] = 'text/csv'
        response.headers['Content-Disposition'] = 'attachment; filename=data.csv'

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
