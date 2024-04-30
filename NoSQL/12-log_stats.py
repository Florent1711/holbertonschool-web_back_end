#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

# Connect to the MongoDB client
client = MongoClient('localhost', 27017)

# Select the 'logs' database and 'nginx' collection
db = client['logs']
collection = db['nginx']

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of documents for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({'method': method}) for method in methods}

# Count the number of documents with method=GET and path=/status
status_count = collection.count_documents({'method': 'GET', 'path': '/status'})

# Display the results
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\t{method}: {method_counts[method]}")
print(f"Documents with method=GET and path=/status: {status_count}")
