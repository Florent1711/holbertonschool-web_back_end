#!/usr/bin/env python3
"""returns the list of school having a specific topic"""


from pymongo import MongoClient

# Connect to the default host and port for MongoDB
client = MongoClient('localhost', 27017)

# Connect to the 'logs' database
db = client.logs

# Access the 'nginx' collection
collection = db.nginx

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of logs for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({'method': method}) for method in methods}

# Count the number of logs where method is GET and path is /status
status_check = collection.count_documents({'method': 'GET', 'path': '/status'})

# Print the stats
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check} status check")
