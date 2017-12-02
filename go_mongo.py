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
import pprint
import datetime

def main():
    client = MongoClient()
    db = client.test_database
    collection = db.test_collection

    post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    posts = db.posts

    post_id = posts.insert_one(post).inserted_id
    print('PostID: ',post_id)
    print('Collections: ',db.collection_names(include_system_collections=False))
    pprint.pprint(posts.find_one())
    pprint.pprint(posts.find_one({"author": "Mike"}))
    pprint.pprint(posts.find_one({"author": "Jessica"}))
    pprint.pprint(posts.find_one({"_id": post_id}))

    print('Print all posts in collection')
    for post in posts.find():
        pprint.pprint(post)

if __name__ == "__main__": main()
