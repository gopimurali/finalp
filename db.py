import pymongo

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo["Crawler"]
    crime_collection = db["Crime"]
    health_collection = db["Health"]
    diabetes_comments_collection = db["Diabetes_comments"]
    politics_collection = db["Politics"]
    youtube_collection = db["Newsinfo"]
    mongo.server_info()
except:
    print("Error - Could not connect to the database")