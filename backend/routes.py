from flask import Blueprint, request, jsonify
import json
import pymongo
import os
import sys
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS, cross_origin

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


client = pymongo.MongoClient("mongodb://localhost:27017/todo")
db = client["todo"]
collection = db["list"]

indexRoute = Blueprint("index", __name__)
createRoute = Blueprint("create", __name__)
updateRoute = Blueprint("update", __name__)
deleteRoute = Blueprint("delete", __name__)


@indexRoute.route("/api/list")
@cross_origin()
def index():
    items = []
    cursor = collection.find({})
    for document in cursor:
        items.append({"_id" : JSONEncoder().encode(document["_id"]), "name": document["name"], "project": document["project"], "description": document["description"]})
    return jsonify(data=items)

@createRoute.route("/api/create", methods=["POST"])
@cross_origin()
def create():
    print(request.json, flush=True)
    name = request.json.get("name")
    project = request.json.get("project")
    description = request.json.get("description")

    item = {
        "name" : name,
        "project" : project,
        "description" : description   
    }
    
    collection.insert_one(item)

    return jsonify(data=item)


@updateRoute.route("/api/update/<id>", methods=["POST"])
@cross_origin()

def update(id):
    print(request.json, flush=True)
    
    itemid= request.json.get("_id")
    name = request.json.get("name"),
    project = request.json.get("project"),
    description = request.json.get("description")
    updatedItem = {
        "name": name,
        "description": description,
        "project" : project,
    }
    collection.update_one({"_id": ObjectId(itemid)}, {"$set": updatedItem})
    print()
    return jsonify(data = "update response")

