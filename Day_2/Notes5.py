# ============================================================
# PYTHON REQUESTS - HTTP METHODS COMPLETE NOTES
# ============================================================

# HTTP methods are used to communicate with servers/APIs.
# Different methods perform different actions.

# ============================================================
# SAMPLE SERVER DATA
# ============================================================

# Imagine this data exists on a server/database.

user = {
    "id": 1,
    "name": "Ram",
    "email": "ram@gmail.com"
}

# ============================================================
# 1. GET METHOD
# ============================================================

# GET is used to READ/FETCH data from a server.
# It does NOT change server data.

# Example:
#
# Before GET:
# {
#     "id": 1,
#     "name": "Ram",
#     "email": "ram@gmail.com"
# }
#
# After GET:
# SAME DATA (No changes)

import requests

response = requests.get("https://httpbin.org/get")

print(response.status_code)   # Prints status code
print(response.text)          # Prints response body

# Common Uses:
# - Fetch user profile
# - Get weather data
# - Load website content


# ============================================================
# 2. POST METHOD
# ============================================================

# POST is used to CREATE/ADD new data.

# Suppose database BEFORE POST:

# [
#     {"id": 1, "name": "Ram"}
# ]

# We send this new data:

# {
#     "name": "Aman",
#     "email": "aman@gmail.com"
# }

response = requests.post(
    "https://httpbin.org/post",
    json={
        "name": "Aman",
        "email": "aman@gmail.com"
    }
)

print(response.json())

# Database AFTER POST:

# [
#     {"id": 1, "name": "Ram"},
#     {"id": 2, "name": "Aman"}
# ]

# POST adds NEW data.


# ============================================================
# 3. PUT METHOD
# ============================================================

# PUT replaces ENTIRE existing data.

# Original Data:

# {
#     "id": 1,
#     "name": "Ram",
#     "email": "ram@gmail.com"
# }

# We send:

# {
#     "name": "Rohit"
# }

response = requests.put(
    "https://httpbin.org/put",
    json={
        "name": "Rohit"
    }
)

print(response.json())

# Result AFTER PUT:

# {
#     "name": "Rohit"
# }

# Notice:
# - email removed
# - id removed

# PUT means:
# "Replace old object completely with new object."


# ============================================================
# 4. PATCH METHOD
# ============================================================

# PATCH updates ONLY SPECIFIC fields.

# Original Data:

# {
#     "id": 1,
#     "name": "Ram",
#     "email": "ram@gmail.com"
# }

# We send:

# {
#     "name": "Rohit"
# }

response = requests.patch(
    "https://httpbin.org/patch",
    json={
        "name": "Rohit"
    }
)

print(response.json())

# Result AFTER PATCH:

# {
#     "id": 1,
#     "name": "Rohit",
#     "email": "ram@gmail.com"
# }

# Only "name" changed.
# Other fields stayed same.

# PATCH means:
# "Update only selected fields."


# ============================================================
# PUT vs PATCH
# ============================================================

# PUT:
# Replaces FULL object.

# PATCH:
# Updates PARTIAL object.


# ============================================================
# 5. DELETE METHOD
# ============================================================

# DELETE removes data from server/database.

# Database BEFORE DELETE:

# [
#     {"id": 1, "name": "Ram"},
#     {"id": 2, "name": "Aman"}
# ]

response = requests.delete(
    "https://httpbin.org/delete"
)

print(response.status_code)

# Database AFTER DELETE:

# [
#     {"id": 2, "name": "Aman"}
# ]

# User with id=1 removed.


# ============================================================
# 6. HEAD METHOD
# ============================================================

# HEAD returns ONLY headers.
# No actual response body/data.

response = requests.head(
    "https://httpbin.org/get"
)

print(response.headers)

# Example headers:

# Content-Type: application/json
# Content-Length: 120

# Uses:
# - Check content type
# - Check file size
# - Check if URL exists


# ============================================================
# 7. OPTIONS METHOD
# ============================================================

# OPTIONS asks server:
# "What operations are allowed here?"

response = requests.options(
    "https://httpbin.org/get"
)

print(response.headers)

# Example response:

# Allow: GET, POST, PUT, DELETE

# Means these methods are supported.


# ============================================================
# RESPONSE OBJECT
# ============================================================

# Every request returns a Response object.

response = requests.get("https://httpbin.org/get")

# Common Response Properties:

print(response.status_code)   # HTTP status code
print(response.text)          # Response as text
print(response.json())        # Response as JSON
print(response.headers)       # Headers dictionary
print(response.url)           # Final URL


# ============================================================
# IMPORTANT STATUS CODES
# ============================================================

# 200 -> Success
# 201 -> Created
# 400 -> Bad Request
# 401 -> Unauthorized
# 404 -> Not Found
# 500 -> Server Error


# ============================================================
# DIFFERENCE BETWEEN data= AND json=
# ============================================================

# data=
# Sends form data.

response = requests.post(
    "https://httpbin.org/post",
    data={
        "name": "Ram"
    }
)

# json=
# Sends JSON data.

response = requests.post(
    "https://httpbin.org/post",
    json={
        "name": "Ram"
    }
)

# When using json=
# Requests automatically:
#
# 1. Converts dictionary to JSON
# 2. Adds header:
#
# Content-Type: application/json


# ============================================================
# requests.request()
# ============================================================

# All methods internally use requests.request()

response = requests.request(
    "GET",
    "https://httpbin.org/get"
)

print(response.status_code)

# But normally we use:
#
# requests.get()
# requests.post()
# requests.put()
#
# because they are easier to read.


# ============================================================
# EASY REAL-LIFE ANALOGY
# ============================================================

# GET    -> Read notebook
# POST   -> Add new page
# PUT    -> Rewrite whole page
# PATCH  -> Correct one line
# DELETE -> Remove page


# ============================================================
# QUICK SUMMARY
# ============================================================

# GET
# Read data

# POST
# Create new data

# PUT
# Replace entire data

# PATCH
# Update some fields only

# DELETE
# Remove data

# HEAD
# Get headers only

# OPTIONS
# Check allowed methods
# ============================================================