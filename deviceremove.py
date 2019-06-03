#!/usr/bin/python
import pymongo
from pymongo import MongoClient
import pprint
import json

MONGO_HOST = raw_input("Enter IP of your Mongo DB: ")
device_mac = raw_input("Enter MAC Address - lowercase: ")

client = pymongo.MongoClient(MONGO_HOST, 27117)

db = client['ace']
results = (db.device.remove({ 'mac' : device_mac }))
pprint.pprint(results)
