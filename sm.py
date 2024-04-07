from flask import Flask, Response
import pymongo
import json
from reddit_analysis import collect_new_crime_data, collect_new_political_data
from db import crime_collection, politics_collection
import time
import datetime

app = Flask(__name__)
# try:
#     mongo = pymongo.MongoClient(
#         host="localhost",
#         port=27017,
#         serverSelectionTimeoutMS = 1000
#     )
#     db = mongo["Crawler"]
#     crime_collection = db["Crime"]
#     politics_collection = db["Politics"]
#     mongo.server_info()
# except:
#     print("Error - Could not connect to database")

##################################
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {"fname" : "murali", "lname":"ponnada"}
        dbresponse = db.users.insert_one(user)
        print(dbresponse.inserted_id)
        return Response(
            response=json.dumps(
                {
                    "message":"user_created",
                    "id":f"{dbresponse.inserted_id} {user['fname']}"
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)

@app.route("/", methods=["GET"])
def get_user():
    return 'X'

@app.route("/pnewcrime", methods=["GET"])
def get_crime_data():
    try:
        # crime_records = collect_new_crime_data()
        # dbresponse = crime_collection.insert_many(crime_records)
        print("-------------------INSIDE PNEWCRIME--------------------")
        # print(crime_records)
        return Response(
            response=json.dumps(
                {
                    "message":"crime_reddit_data_created"
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("----------------------------"+str(ex)+"---------------------------"+str(datetime.datetime.now()))

@app.route("/pnewpolitics", methods=["GET"])
def get_data():
    try:
        # political_records = collect_new_political_data()
        # dbresponse = politics_collection.insert_many(records)
        print("-------------------INSIDE PNEWPOLITICS--------------------")
        return Response(
            response=json.dumps(
                {
                    "message":"political_reddit_data_created"
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
##################################

if __name__ == "__main__":
    app.run(port=2784, debug=True)