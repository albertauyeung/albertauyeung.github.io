---
layout: article
title:  "Date/Time in Python"
tags: [python]
---

## The `datetime` Module

With the help of the `pytz` module:

```python
from datetime import datetime
from datetime import timedelta
from pytz import timezone

# Print current date/time
now = datetime.now()   # Get current date/time
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Parse a date/time String into a Python object
timestring = "2020-01-01 15:32:11"
timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

# Convert between epoch time and date/time object
epoch_time = 1580092848  # seconds since epoch
o = datetime.fromtimestamp(epoch_time)
print(o.strftime("%Y-%m-%d %H:%M:%S"))  # prints "2020-01-27 10:40:48"

```


## The `Arrow` Module

```bash
$ pip3 install -U arrow
```

```python
import arrow

# Get current date/time
arrow.utcnow()  # Get current UTC time
arrow.now()     # Get system time
arrow.now('Asia/Hong_Kong')   # Get local time

# Converting between epoch time and arrow object
a = arrow.get(1580092848)

# Format date/time string
a.format('YYYY-MM-DD HH:mm:ss')  # prints '2020-01-27 02:40:48'

# Time shifting
b = a.shift(day=+3)
b.date    # datetime.date(2020, 1, 30)
```
