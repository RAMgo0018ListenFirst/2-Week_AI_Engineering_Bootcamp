# ============================================
# PYTHON REQUESTS LIBRARY - GET REQUEST NOTES
# ============================================

# --------------------------------------------
# 1. INSTALL REQUESTS LIBRARY
# --------------------------------------------

# Run this command in terminal:

# pip install requests


# --------------------------------------------
# 2. IMPORT REQUESTS
# --------------------------------------------

import requests

# requests is a Python library used to send HTTP requests
# like GET, POST, PUT, DELETE etc.


# --------------------------------------------
# 3. MAKE YOUR FIRST GET REQUEST
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response)

# requests.get() sends a GET request to the URL
# response stores the server response
# Output:
# <Response [200]>

# 200 means request successful


# --------------------------------------------
# 4. CHECK STATUS CODE
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response.status_code)

# .status_code gives the HTTP status code

# Common status codes:
# 200 = Success
# 404 = Not Found
# 403 = Forbidden
# 500 = Server Error


# --------------------------------------------
# 5. USE IF CONDITION WITH STATUS CODE
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("Success!")

elif response.status_code == 404:
    print("Not Found")

# Checks whether request was successful or not


# --------------------------------------------
# 6. SHORTCUT USING BOOLEAN RESPONSE
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

if response:
    print("Success!")

else:
    print("Error")

# response becomes True for status codes 200-399
# response becomes False for status codes 400-599


# --------------------------------------------
# 7. RAISE ERROR AUTOMATICALLY
# --------------------------------------------

import requests

response = requests.get("https://api.github.com/invalid")

response.raise_for_status()

# raise_for_status() automatically raises error
# if status code is between 400-599


# --------------------------------------------
# 8. HANDLE ERRORS USING TRY-EXCEPT
# --------------------------------------------

import requests
from requests.exceptions import HTTPError

URLS = [
    "https://api.github.com",
    "https://api.github.com/invalid"
]

for url in URLS:

    try:

        response = requests.get(url)

        response.raise_for_status()

    except HTTPError as http_err:

        print(f"HTTP Error Occurred: {http_err}")

    except Exception as err:

        print(f"Other Error Occurred: {err}")

    else:

        print("Success!")

# try:
# Code that may cause error

# except:
# Handles the error

# else:
# Runs only if no error occurs


# --------------------------------------------
# 9. ACCESS RESPONSE CONTENT AS BYTES
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response.content)

# .content gives raw byte data

# Example output:
# b'{"current_user_url":"https://api.github.com/user"}'


# --------------------------------------------
# 10. CHECK TYPE OF CONTENT
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(type(response.content))

# Output:
# <class 'bytes'>


# --------------------------------------------
# 11. ACCESS RESPONSE AS STRING
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response.text)

# .text converts bytes into readable string


# --------------------------------------------
# 12. CHECK TYPE OF TEXT
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(type(response.text))

# Output:
# <class 'str'>


# --------------------------------------------
# 13. SET ENCODING
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

response.encoding = "utf-8"

print(response.text)

# Encoding converts bytes into readable text
# UTF-8 is most common encoding


# --------------------------------------------
# 14. CONVERT JSON RESPONSE INTO DICTIONARY
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)

# .json() converts JSON response into Python dictionary


# --------------------------------------------
# 15. CHECK TYPE OF JSON DATA
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

data = response.json()

print(type(data))

# Output:
# <class 'dict'>


# --------------------------------------------
# 16. ACCESS SPECIFIC VALUE FROM JSON
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data["current_user_url"])

# Access dictionary values using keys


# --------------------------------------------
# 17. VIEW RESPONSE HEADERS
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response.headers)

# Headers contain metadata like:
# content type
# server info
# cache info
# encoding


# --------------------------------------------
# 18. ACCESS SPECIFIC HEADER
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response.headers["Content-Type"])

# Example Output:
# application/json; charset=utf-8


# --------------------------------------------
# 19. HEADERS ARE CASE INSENSITIVE
# --------------------------------------------

import requests

response = requests.get("https://api.github.com")

print(response.headers["Content-Type"])

print(response.headers["content-type"])

# Both work the same


# --------------------------------------------
# 20. COMPLETE BEGINNER PROGRAM
# --------------------------------------------

import requests
from requests.exceptions import HTTPError

url = "https://api.github.com"

try:

    response = requests.get(url)

    response.raise_for_status()

    print("Status Code:")
    print(response.status_code)

    print("\nResponse Text:")
    print(response.text)

    print("\nJSON Data:")
    data = response.json()
    print(data)

    print("\nSpecific JSON Value:")
    print(data["current_user_url"])

    print("\nHeaders:")
    print(response.headers)

except HTTPError as http_err:

    print("HTTP Error:", http_err)

except Exception as err:

    print("Other Error:", err)


# --------------------------------------------
# IMPORTANT METHODS SUMMARY
# --------------------------------------------

# requests.get(url)
# Sends GET request

# response.status_code
# Gives status code

# response.content
# Gives raw bytes

# response.text
# Gives string/text data

# response.json()
# Converts JSON into dictionary

# response.headers
# Gives response headers

# response.raise_for_status()
# Raises error for bad requests


# --------------------------------------------
# REAL WORLD USES OF REQUESTS LIBRARY
# --------------------------------------------

# APIs
# Chatbots
# Weather Apps
# AI Applications
# Automation
# Web Scraping
# Backend Development
# Data Fetching