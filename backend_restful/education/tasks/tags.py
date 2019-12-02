from backend_restful.db import users
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers
import json

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class tags:
    response = {}
    def __init__(self, data={}):
        data["associated"] = "5ddd62ffd8639286d599dcd6"
        data["designation"] = "5ddd62ffd8639286d599dcd7"
        #query database for dashboard info
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        education = db.education
        user_id = data.get("user_info")
        #pprint(user_id)
        query_result = education.find_one(
              {"_id" : ObjectId(user_id),
              "associated._id": ObjectId(data.get("associated")),
              "associated.designations._id": ObjectId(data.get("designation"))
              },
              {
               "associated.designations.tags.tasks":0
               }
        )
        #this is to avoid ObjectId not serializer error
        #query_result["_id"] = user_id
        print("showing results")
        pprint(query_result)
        for associate in query_result["associated"]:
            print(associate.get("_id"))
            if data["associated"] == str(associate.get("_id")):
                for designation in associate["designations"]:
                    if data["designation"] == str(designation.get("_id")):
                        self.response=json.loads(json.dumps(designation, default=str))
                        return
        self.response=json.loads(json.dumps({"error": "does not exist"}, default=str))