# =========================================================
# PYTHON REQUESTS LIBRARY - BEGINNER NOTES
# =========================================================

# ---------------------------------------------------------
# WHAT IS REQUESTS?
# ---------------------------------------------------------
# Requests is a third-party Python library used to make
# HTTP requests to websites and APIs.
#
# It helps Python communicate with servers on the internet.
#
# Requests is NOT built into Python.
# So we must install it first.
# ---------------------------------------------------------



# =========================================================
# INSTALLATION
# =========================================================

# Create virtual environment
# Run in terminal:

# python -m venv venv


# Activate virtual environment (Windows)
# Run in terminal:

# venv\Scripts\activate


# Install requests library
# Run in terminal:

# python -m pip install requests



# =========================================================
# IMPORT REQUESTS
# =========================================================

import requests

# This imports the requests library into Python.



# =========================================================
# SIMPLE GET REQUEST
# =========================================================

import requests

response = requests.get("https://api.github.com")

print(response)

# Explanation:
#
# requests.get() sends a GET request to the URL.
#
# GET means:
# "Give me data"
#
# response stores the server response.
#
# Expected Output:
# <Response [200]>
#
# 200 means success.



# =========================================================
# STATUS CODE
# =========================================================

import requests

response = requests.get("https://api.github.com")

print(response.status_code)

# Explanation:
#
# status_code gives HTTP response code.
#
# Common Codes:
# 200 = Success
# 404 = Not Found
# 500 = Server Error
# 403 = Forbidden



# =========================================================
# RESPONSE TEXT
# =========================================================

import requests

response = requests.get("https://api.github.com")

print(response.text)

# Explanation:
#
# response.text returns data as a STRING.
#
# Mostly used for:
# HTML
# JSON text
# webpage content



# =========================================================
# RESPONSE CONTENT
# =========================================================

import requests

response = requests.get("https://api.github.com")

print(response.content)

# Explanation:
#
# response.content returns RAW BYTES.
#
# Useful for:
# images
# PDFs
# files
#
# Output starts with b''
# Example:
# b'{ "current_user_url": ... }'



# =========================================================
# CONVERT JSON RESPONSE TO PYTHON DICTIONARY
# =========================================================

import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)

# Explanation:
#
# .json() converts JSON data into Python dictionary.
#
# Very important for APIs.
#
# JSON is the most common API format.



# =========================================================
# CHECK DATA TYPE
# =========================================================

import requests

response = requests.get("https://api.github.com")

data = response.json()

print(type(data))

# Explanation:
#
# Usually API JSON becomes:
# <class 'dict'>



# =========================================================
# ACCESS JSON VALUES
# =========================================================

import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data["current_user_url"])

# Explanation:
#
# Access dictionary values using keys.
#
# data["key_name"]



# =========================================================
# CHECK IF REQUEST SUCCESSFUL
# =========================================================

import requests

response = requests.get("https://api.github.com")

print(response.ok)

# Explanation:
#
# response.ok returns:
# True  -> request successful
# False -> request failed



# =========================================================
# USING HEADERS
# =========================================================

import requests

headers = {
    "User-Agent": "MyPythonApp"
}

response = requests.get(
    "https://api.github.com",
    headers=headers
)

print(response.status_code)

# Explanation:
#
# Headers send extra information to server.
#
# Common uses:
# authentication
# API keys
# browser information
# content type
#
# headers parameter accepts dictionary.



# =========================================================
# SIMPLE POST REQUEST
# =========================================================

import requests

data = {
    "username": "ram",
    "password": "1234"
}

response = requests.post(
    "https://httpbin.org/post",
    data=data
)

print(response.text)

# Explanation:
#
# POST sends data to server.
#
# data= sends form data.
#
# Used in:
# login forms
# form submission
# creating data



# =========================================================
# SEND JSON DATA
# =========================================================

import requests

data = {
    "name": "Ram",
    "age": 21
}

response = requests.post(
    "https://httpbin.org/post",
    json=data
)

print(response.text)

# Explanation:
#
# json= sends JSON body.
#
# Modern APIs mostly use JSON.
#
# Python automatically converts dictionary to JSON.



# =========================================================
# DIFFERENCE BETWEEN data= AND json=
# =========================================================

# data=
# Sends form-encoded data

# json=
# Sends JSON formatted data



# =========================================================
# HANDLE ERRORS
# =========================================================

import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("Success")
else:
    print("Failed")

# Explanation:
#
# Checks if request succeeded.
#
# Good practice for APIs.



# =========================================================
# USING TIMEOUT
# =========================================================

import requests

response = requests.get(
    "https://api.github.com",
    timeout=5
)

print(response.status_code)

# Explanation:
#
# timeout prevents waiting forever.
#
# Here Python waits maximum 5 seconds.



# =========================================================
# COMPLETE BEGINNER EXAMPLE
# =========================================================

import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Current User URL:")
print(data["current_user_url"])

# Explanation:
#
# Step 1:
# Send GET request
#
# Step 2:
# Check status code
#
# Step 3:
# Convert JSON response into dictionary
#
# Step 4:
# Access dictionary values



# =========================================================
# GET VS POST
# =========================================================

# GET
# ----
# Used to FETCH data
#
# Example:
# getting weather
# getting GitHub data


# POST
# ----
# Used to SEND data
#
# Example:
# login forms
# signup forms
# uploading data



# =========================================================
# IMPORTANT TERMS
# =========================================================

# API
# ----
# A way for applications to communicate.


# HTTP
# ----
# Protocol used for communication on internet.


# JSON
# ----
# Data format used by APIs.


# Headers
# -------
# Extra information sent with request.


# Response
# --------
# Data returned from server.



# =========================================================
# FLOW OF REQUEST
# =========================================================

# Python Program
#       ↓
# requests.get()
#       ↓
# Internet/API
#       ↓
# Server Response
#       ↓
# response object
#       ↓
# Use data in Python



# =========================================================
# END OF NOTES
# =========================================================