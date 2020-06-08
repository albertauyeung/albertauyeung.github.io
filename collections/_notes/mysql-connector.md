---
layout: article
title:  "Connecting to MySQL Database in Python"
tags: [python, mysql]
---

```bash
$ pip install mysql-connector-python
```

```python
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(
    user='metabase',
    password="metabase",
    database='personal',
    auth_plugin='mysql_native_password')
cursor = cnx.cursor()

add_item = ("""
    INSERT INTO items
    (name, descriptions)
    VALUES
    (%s, %s)
""")

data = ("item001", "some descriptions")
cursor.execute(add_item, data)

# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()
```
