#!/usr/bin/python3.6

# Pull the latest Mongo Docker image from Docker Hub and run a Mongo container.
# Also, check out the docs: https://hub.docker.com/_/mongo/
#
# Figure out the host IP of the Mongo container (hint: `docker inspect`)
#
# Check the docs for pymongo: https://api.mongodb.com/python/current/
#
# Write a quick python script with functions that will...
#   create a database in your running Dockerized Mongo instance
#   create a collection
#   insert a document into a collection
#   list all documents in a collection
#   list a single document from a collection (queried by one of its json fields)

from pymongo import MongoClient

#mongodb 3.4
client = MongoClient()
db = client.primer
coll = db.dataset