---
layout: article
title:  "Connecting to MongoDB in Python"
tags: [python, mongodb]
---

```bash
$ python -m pip install pymongo
```

```python
from pymongo import MongoClient

MONGO_HOST = 'localhost'
MONGO_PORT = 30000
MONGO_DATABASE = 'db'
MONGO_USERNAME = 'username'
MONGO_PASSWORD= 'password'

client = MongoClient(
    MONGO_HOST, MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource=MONGO_DATABASE,
    authMechanism='SCRAM-SHA-256'
)
db = client[MONGO_DATABASE]

results = db["my_collection"].find()
```

Reference: [https://api.mongodb.com/python/current/tutorial.html](https://api.mongodb.com/python/current/tutorial.html)
