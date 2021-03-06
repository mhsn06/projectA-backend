from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers
import json
from bson.json_util import dumps

'''
user requirment: Description return a list of people based on filters
system requirement:
    1. 
'''

class list_people:
    response = None
    def __init__(self, data={}):
        #serialize data
        serializer = listPeopleSerializer(data=data["data"])

        if serializer.is_valid():
            client = DBHandler.get_database_client()
            db = client.test
            result = db.education.find({
                "associated.institute_id" : ObjectId(serializer.validated_data.get("institute_id")),
                "associated.designations.meta_data.class" : serializer.validated_data.get("meta_data").get("class")
            },{
                "associated.designations.meta_data":1
            })
            pprint(result.count())
            self.response = {"result":json.loads(json.dumps(list(result), default=str))}
        else:
            self.response = {"error": serializer.errors}




class listPeopleSerializer(serializers.Serializer):
    institute_id = serializers.CharField() # instititue id
    people_type = serializers.CharField() # student/teacher/commetee member/guardian/alumni
    meta_data = serializers.JSONField()
