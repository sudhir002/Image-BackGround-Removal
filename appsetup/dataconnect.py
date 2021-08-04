__author__ = 'Sudhir'
__date__ = "Aug 3 - 2021"


'''
Purpose : Connect to the Database 
'''

from pymongo import MongoClient


def mongodb():
	MONGO_HOST = "localhost"
	client = MongoClient(MONGO_HOST,27017)
	return client.background_removalDB
