#!/usr/bin/env python3
""" This function provides some stats about Nginx logs stored in MongoDB """


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    status_check = nginx_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{nginx_collection.count_documents({})} logs\nMethods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE", "/status"]:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}") if method != "/status" else print(
            f"{status_check} status check")
