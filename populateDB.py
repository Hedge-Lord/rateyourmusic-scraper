from flask_pymongo import PyMongo
from flask import Flask, jsonify, make_response
from rymscraper import scraper
import time
import random

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://user:mypassword123@myatlasclusteredu.eiepfa0.mongodb.net/test"
mongo = PyMongo(app)

@app.route("/")
def test():
    return "Hello World!"

@app.route("/get/top/3000")
def get_top_3000():
    try:
        with scraper.Scraper() as rymscraper:
            top_artists = rymscraper.get_top_3000()
            db = mongo.db.top_artists
            for artist in top_artists["info"]:
                if db.count_documents({'name': artist}) > 0:
                    continue
                db.insert_one({"name": artist})
            return "success"
    except Exception as e:
        print(f"error occurred: {e}")
        return "unsuccess"
    
@app.route("/populate/top/3000")
def populate_top_3000():
    try:
        with scraper.Scraper() as rymscraper:
            db = mongo.db.top_artists
            artist_collection = mongo.db.artists
            top_artists = db.find({"name": {"$exists": True}})
            # artist = top_artists[0]
            # artist_info = rymscraper.get_artist_info(artist['name'])
            # print(artist_info)
            # artist_collection.insert_one({'name': artist['name'], 'info': artist_info})

            count = 0
            for artist in top_artists:
                try:
                    if artist_collection.count_documents({'name': artist['name']}) > 0:
                        print("skipping ", artist['name'])
                        db.delete_many({'name': artist['name']})
                        continue
                    time.sleep(4)
                    if count >= 5:
                        rymscraper.restart()
                        time.sleep(10)
                        time.sleep(random.uniform(3.0, 7.0))
                        count = 0

                    artist_info = rymscraper.get_artist_info(artist['name'])
                    print(artist['name'], artist_info)
                    artist_collection.insert_one({'name': artist['name'], 'info': artist_info})
                    if artist_info:
                        db.delete_many({'name': artist['name']})
                    count += 1
                except:
                    print("error retrieving: ", artist['name'])
                    None
        return "success"
    except Exception as e:
        print(f"error occurred: {e}")
        return "unsuccess"


@app.route("/populate")
def populate_db():
    return 


if __name__ == "__main__":
    while populate_top_3000() == "unsuccess":
        print("Running it up")
    print("Done")

