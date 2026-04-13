1. missing importas pylance

solution:

Configuring a Python Environment
Completed with input: {
"resourcePath": "/home/vlad/repos/portfolio/time-tracker"
}

Fetching Python environment information
Completed with input: {
"resourcePath": "/home/vlad/repos/portfolio/time-tracker"
}

`fastapi` is installed in your workspace venv. Pylance is likely using a different interpreter, so it can’t see the package.

Fix:

- In VS Code, open Command Palette → **Python: Select Interpreter** → choose the venv at python.
- Then reload the window (Command Palette → **Developer: Reload Window**).

Quick verify in terminal:

```
/home/vlad/repos/portfolio/time-tracker/.venv/bin/python -c "import fastapi; print(fastapi.__version__)"
```

If that works but Pylance still complains, tell me and I’ll help check your VS Code settings.

# WORKiNG WITH JSON FIELS IN PYTHON

```python
import json
from pathlib import Path

path = Path("data.json")

# 1. READ: Load the file and convert string to a Python Dictionary
data = json.loads(path.read_text())

# 2. MODIFY: Now you can use dictionary methods!
data["new_key"] = "new_value"
data["a"] = 456  # Updating an existing value

# 3. WRITE: Convert the dictionary back to a string and save
path.write_text(json.dumps(data, indent=4))
```

# FIX DATETIME OBJECT NOT JSON-SERIALIZABLE

How to Fix - "datetime.datetime not JSON serializable" in Python?
Last Updated : 23 Jul, 2025
In this article, we are going to learn how to fix the error "datetime.datetime not JSON serializable" in Python.

datetime.datetime is a class in the Python datetime module that represents a single point in time. This class is not natively supported by the JSON (JavaScript Object Notation) format, which means that we cannot serialize a datetime.datetime object directly to a JSON string using the JSON module in Python.

What is JSON serializable?
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy to read and write and easy for machines to parse and generate. It is a way of representing data in a format that can be easily converted to and from JavaScript objects. JSON serialization refers to the process of converting a Python object into a JSON-formatted string. JSON-serializable means an object which can be represented in JSON format. For example, a Python dictionary can be easily converted to a JSON-formatted string using the JSON module:

import json
​
data = {
"name": "John Smith",
"age": 30,
"address": {
"street": "123 Main St",
"city": "Anytown",
"state": "CA",
"zip": "12345"
},
"phoneNumbers": [
{"type": "home", "number": "555-555-5555"},
{"type": "work", "number": "555-555-5555"}
]
}
​
json_data = json.dumps(data)
print(json_data)
Output:

{"name": "John Smith",
"age": 30,
"address": {"street": "123 Main St", "city": "Anytown", "state": "CA", "zip": "12345"},
"phoneNumbers": [{"type": "home", "number": "555-555-5555"},
{"type": "work", "number": "555-555-5555"}]}
To serialize a datetime.datetime object to JSON, you will need to convert it to a format that is compatible with JSON, such as a string.

Serialize a Python datetime.datetime object
If we are trying to serialize a Python datetime.datetime object using the json module and we are getting the error "TypeError: datetime.datetime not JSON serializable", it means that the JSON module does not know how to convert the datetime object to a JSON-serializable format. Let us have a look at an example of this error.

# Importing required module

import json
import datetime

# Store time in "now"

now = datetime.datetime.now()

# Serializing time stored in now

json.dumps(now)
Output:

Traceback (most recent call last):
File "c:\Users\Desktop\geekforgeeks\gfg6.py", line 5, in <module>
json.dumps(now)
File "C:\Users\AppData\Local\Programs\Python\Python39\lib\json\_\_init**.py", line 231, in dumps
return \_default_encoder.encode(obj)
File "C:\Users\AppData\Local\Programs\Python\Python39\lib\json\encoder.py", line 199, in encode
chunks = self.iterencode(o, \_one_shot=True)
File "C:\Users\AppData\Local\Programs\Python\Python39\lib\json\encoder.py", line 257, in iterencode
return \_iterencode(o, 0)
File "C:\Users\AppData\Local\Programs\Python\Python39\lib\json\encoder.py", line 179, in default
raise TypeError(f'Object of type {o.**class**.**name\_\_} '
TypeError: Object of type datetime is not JSON serializable
Method 1: Using the json.dumps() function
The json.dumps() is a function in the json module of Python that is used to convert a Python object into a JSON-formatted string. It takes an object as its argument and returns a string representation of the object in JSON format.

The datetime.datetime object in Python is not directly JSON serializable, meaning it cannot be converted to a JSON-formatted string using json.dumps without additional steps. To overcome this error, you can use the default argument of the json.dumps function to specify a custom function that will be called to handle non-serializable objects.

import json
import datetime
​

# Define a custom function to serialize datetime objects

def serialize_datetime(obj):
if isinstance(obj, datetime.datetime):
return obj.isoformat()
raise TypeError("Type not serializable")
​
​

# Create a datetime object

dt = datetime.datetime.now()
​

# Serialize the object using the custom function

json_data = json.dumps(dt, default=serialize_datetime)
print(json_data)
Output: This will output a JSON-serialized string that represents the datetime object in ISO format (e.g. "2022-12-31T23:59:59.999999"). We can then use this string to send the datetime object over the network or store it in a file.

"2023-01-13T09:45:04.386958"
Method 2: Using the datetime module's strftime() method
The strftime() method of the datetime module in Python is used to format a datetime object into a string representation. The method takes a format string as an argument, which defines the desired output format. The format codes used in the format string are similar to those used in the C library function strftime(). The formatted string can then be used for display, storage, or other purposes.

To use the strftime() method to convert a datetime object to a JSON serializable string, we have to first use the strftime() method to format the datetime object into a string with a desired format, and then pass the resulting string to the json.dumps() function.

# Importing required modules

import json
import datetime
​

# Create a datetime object

dt = datetime.datetime.now()
​

# Convert the datetime object to a string in a specific format

dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
​

# Serialize the string using the json module

json_data = json.dumps(dt_str)
print(json_data)
Output: This will output a JSON-serialized string that represents the datetime object in the format "YYYY-MM-DD HH:MM:SS" (e.g. "2022-12-31 23:59:59").

"2023-01-13 09:49:07"

# JSON DUMPS VS JSON LOADS

The JSON objects are surrounded by curly braces { }. They are written in key and value pairs. In this Answer, we will discuss the difference between the json.loads() and the json.dumps().

The json.loads() takes in a string and returns a python object and the json.dumps() takes in a Python object and returns a JSON string.

As we can see, json.dumps() and json.loads() are opposite of one another.

The json.loads() example
In this example, a string is converted into a Python object, and the key age is accessed in that object:

Ace Editor

```python
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])



```

Run
Code example for the json.loads() method
In this case, it converts the JSON string into a Python dictionary, because the JSON string represents an object with key-value pairs.

The json.dumps() example
In this example, a json object is passed in the json.dumps() function, and its data is extracted and returned in the form of a string:

```python
import json
a = {'lalalala': 3}
myString = json.dumps(a)
print (myString)

```

Ace Editor

Run
Code example for the json.dumps() method
In summary, json.loads() converts JSON strings to Python objects, while json.dumps() converts Python objects to JSON strings. These functions are essential for handling JSON data within Python scripts, facilitating easy conversion and manipulation of structured data.

# ISSUE WITH / vs // FOR TIME TRACKING

You are 90% of the way there, and the "Total Seconds" logic is definitely the right path! However, there is one subtle but major bug in your implementation: **using `round()` instead of floor division (`//`)**.

### The `round()` Problem

In programming, when you're breaking down time, you almost always want to "chop off" the remainder, not round to the nearest whole number.

**Example:** If you have **70 seconds** and you calculate minutes:

- `70 / 60` is `1.16`.
- `round(1.16)` gives you **1 minute**. (Correct so far).
- **But**, if you have **110 seconds**:
- `110 / 60` is `1.83`.
- `round(1.83)` gives you **2 minutes**.
- When you then calculate `110 % 60`, you get **50 seconds**.
- Your code would report the time as **2 minutes and 50 seconds**, which is actually 170 seconds!

### The Fix

Use **Integer Division (`//`)**. This tells Python: "Give me the whole number and ignore the decimal."

```python
def calculate_time_difference(self, dt1, dt2):
    # ... your existing setup code ...

    seconds_t2_overall = hours_dt2 * 3600 + minutes_dt2 * 60 + seconds_dt2
    seconds_t1_overall = hours_dt1 * 3600 + minutes_dt1 * 60 + seconds_dt1

    # Using abs() ensures that if t1 is after t2, you still get a positive duration
    difference_in_seconds = abs(seconds_t2_overall - seconds_t1_overall)

    # Use // for floor division
    hours_overall = difference_in_seconds // 3600

    rest_seconds = difference_in_seconds % 3600
    minutes_overall = rest_seconds // 60
    seconds_overall = rest_seconds % 60

    # Cleaning up the keys (removing colons/spaces makes them easier to use)
    time_entry = {
        "hours": hours_overall,
        "minutes": minutes_overall,
        "seconds": seconds_overall,
    }

    print(time_entry)
    self.time_entry = time_entry
```

### Why this is better:

1.  **Accuracy:** Integer division always rounds down, which is what you need when "extracting" hours and minutes.
2.  **Cleaner Keys:** I removed the `:` and extra spaces from your dictionary keys. It’s a small thing, but `data["hours"]` is much nicer to type than `data["hours:"]`.

**One last edge case:** Since you are using `dt1` and `dt2` (which I assume are `datetime` objects), remember that this logic only works if both times are on the same day. If `dt1` is 11:59 PM and `dt2` is 12:01 AM, the result will be a huge negative number.

If you want to handle multi-day differences, you can just use `(dt2 - dt1).total_seconds()` and then apply your `/ 3600` logic to that result!

# TIME TRACKER - ISSUE WITH CALCULATION / DAY OVERFLOW

This is actually a **very solid first implementation** — but now we need to level it up from _“it works”_ → _“this is backend-engineer quality”_.

I’ll break it down into:

1. ✅ What you did well
2. ⚠️ Problems (important)
3. 🔥 How to fix (clean + professional)
4. 🧠 What interviewers expect

---

# ✅ What you did well

- Good separation into a class (`Timer`) ✔️
- Clear lifecycle:
  - `start_timer()`
  - `stop_timer()`

- Writing to JSON ✔️
- Thinking about edge cases (`start_time is None`) ✔️
- Attempting manual time calculation ✔️

👉 This shows good instincts.

---

# ⚠️ Main problems (important)

## ❌ 1. You should NOT manually calculate time

This is the biggest issue.

```python
difference_in_seconds = seconds_t2_overall - seconds_t1_overall
```

👉 This breaks for:

- crossing midnight ❌
- different days ❌
- timezone issues ❌

---

## ❌ 2. You are ignoring `datetime`'s main feature

Python already solves this:

👉 `timedelta`

---

## ❌ 3. Mixing responsibilities (BIG architecture issue)

Your class does:

- timing logic ❌
- formatting ❌
- persistence (JSON writing) ❌

👉 This violates separation of concerns.

---

## ❌ 4. Printing instead of returning

```python
print(...)
```

👉 Not usable in:

- APIs
- tests
- frontend

---

## ❌ 5. Mutable state (`self.time_entry = {}`)

Not terrible, but:

- unnecessary
- can lead to bugs

---

## ❌ 6. Naming issues

```python
"hours:"
"seconds: "
```

👉 inconsistent + trailing spaces ❌

---

# 🔥 Correct way (professional version)

## 1. Use `timedelta` (THIS IS CRITICAL)

Replace your entire calculation with:

```python
def calculate_duration(self):
    if self.start_time is None or self.end_time is None:
        raise ValueError("Timer not properly started/stopped")

    delta = self.end_time - self.start_time

    total_seconds = int(delta.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
    }
```

👉 This automatically handles:

- day overflow ✅
- correct math ✅

---

## 2. Clean `stop_timer()`

```python
def stop_timer(self):
    if self.start_time is None:
        raise ValueError("Timer was never started")

    self.end_time = dt.now()

    duration = self.calculate_duration()

    return {
        "start_time": self.start_time,
        "end_time": self.end_time,
        "duration": duration,
    }
```

👉 No prints
👉 Returns data (API-ready)

---

## 3. Move JSON writing OUT

Instead of:

```python
write_time_entry(json_data)
```

👉 do this in service layer:

```python
result = timer.stop_timer()
write_time_entry(result)
```

---

## 4. Optional: make it cleaner

```python
def start_timer(self):
    self.start_time = dt.now()
    self.end_time = None
```

---

# 🧱 Final architecture (important for you)

## Timer = logic only

```text
Timer
 ├── start()
 ├── stop()
 └── calculate_duration()
```

## Service = orchestration

```python
def stop_timer_service(timer: Timer):
    result = timer.stop_timer()
    write_time_entry(result)
```

---

# 🧠 Interview-level explanation

If they ask:

> “How do you handle time tracking?”

You say:

> I use Python’s datetime and timedelta to compute durations instead of manual calculations, which avoids issues like day overflow. I separate timing logic from persistence by keeping the Timer class focused on state and duration calculation, while storage is handled in a separate layer.

👉 That’s a **strong answer**

---

# ⚡ Small improvements

## Use ISO format instead of strftime

```python
self.start_time.isoformat()
```

👉 standard + API-friendly

---

## Add type hints

```python
def calculate_duration(self) -> dict:
```

---

## Remove `time` import (unused)

```python
import time ❌
```

---

# 🏁 Final verdict

## Your current code:

👉 Good beginner level

## After fixes:

👉 Solid junior backend level

---

# 🔥 Biggest takeaway

👉 NEVER manually calculate time
👉 ALWAYS use:

```python
delta = end - start
delta.total_seconds()
```

---

If you want next: I can help you turn this into a **proper FastAPI endpoint (`/start`, `/stop`) using this Timer class**, which would be a huge step for your portfolio.
