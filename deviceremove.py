#!/usr/bin/python
import pymongo
from pymongo import MongoClient
import pprint
import json

MONGO_HOST = raw_input("Enter IP of your Mongo DB: ")
MONGO_DB = raw_input("Enter the name of your DB: ")
device_mac = raw_input("Enter MAC Address - lowercase: ")
#device_mac = raw_input("Enter your MAC Address: ")
#MONGO_PORT = raw_input("Enter your port: ")

client = pymongo.MongoClient('127.0.0.1', 27117)

db = client['ace']
results = (db.device.remove({ 'mac' : device_mac }))
pprint.pprint(results)
