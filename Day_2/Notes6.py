# =========================================================
# INSPECTING PREPARED REQUESTS & AUTHENTICATION IN REQUESTS
# =========================================================

# The Requests library automatically prepares an HTTP request
# before sending it to the server.
#
# This prepared request contains:
# 1. URL
# 2. Headers
# 3. Body/Data
# 4. Authentication info
#
# You can inspect all of these using:
# response.request


# =========================================================
# 1. INSPECTING A PREPARED REQUEST
# =========================================================

import requests

# Sending POST request with JSON data
response = requests.post(
    "https://httpbin.org/post",
    json={"key": "value"}
)

# ---------------------------------------------------------
# PRINT THE PREPARED REQUEST OBJECT
# ---------------------------------------------------------

print(response.request)

# Output:
# <PreparedRequest [POST]>

# Explanation:
# Requests internally creates a PreparedRequest object
# before sending the request.


# ---------------------------------------------------------
# CHECK REQUEST HEADERS
# ---------------------------------------------------------

print(response.request.headers)

# Explanation:
# Headers contain extra information sent to server.
# Requests automatically adds many headers.


# ---------------------------------------------------------
# CHECK CONTENT-TYPE HEADER
# ---------------------------------------------------------

print(response.request.headers["Content-Type"])

# Output:
# application/json

# Explanation:
# Since we used json={},
# Requests automatically:
# 1. Converts dictionary → JSON
# 2. Adds Content-Type header


# ---------------------------------------------------------
# CHECK FINAL URL
# ---------------------------------------------------------

print(response.request.url)

# Output:
# https://httpbin.org/post

# Explanation:
# This is the exact URL being requested.


# ---------------------------------------------------------
# CHECK REQUEST BODY
# ---------------------------------------------------------

print(response.request.body)

# Output:
# b'{"key": "value"}'

# Explanation:
# HTTP sends data as bytes.
# Requests converts JSON data into bytes automatically.


# =========================================================
# 2. BASIC AUTHENTICATION USING auth=
# =========================================================

# Some APIs require login credentials.
# Requests provides auth= parameter for authentication.

response = requests.get(
    "https://httpbin.org/basic-auth/user/passwd",
    auth=("user", "passwd")
)

print(response.status_code)

# Output:
# 200

# Explanation:
# auth=("user","passwd") tells Requests to:
# 1. Create Basic Authentication header
# 2. Encode credentials
# 3. Send them automatically


# ---------------------------------------------------------
# CHECK AUTHORIZATION HEADER
# ---------------------------------------------------------

print(response.request.headers["Authorization"])

# Output:
# Basic dXNlcjpwYXNzd2Q=

# Explanation:
# Requests automatically creates:
#
# Authorization: Basic <base64 encoded credentials>
#
# user:passwd becomes:
# dXNlcjpwYXNzd2Q=


# =========================================================
# 3. HOW auth= WORKS INTERNALLY
# =========================================================

# Internally Requests does this:

from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://httpbin.org/basic-auth/user/passwd",
    auth=HTTPBasicAuth("user", "passwd")
)

print(response.status_code)

# Output:
# 200

# Explanation:
# auth=("user","passwd")
# is shorthand for:
#
# HTTPBasicAuth("user","passwd")


# =========================================================
# 4. ACCESSING GITHUB API WITHOUT AUTHENTICATION
# =========================================================

response = requests.get("https://api.github.com/user")

print(response.status_code)

# Output:
# 401

# Explanation:
# 401 means:
# Unauthorized
#
# GitHub requires authentication for this endpoint.


# =========================================================
# 5. TOKEN AUTHENTICATION
# =========================================================

# Example token
token = "YOUR_GITHUB_TOKEN"

response = requests.get(
    "https://api.github.com/user",
    auth=("", token)
)

print(response.status_code)

# Explanation:
# Requests treats this as Basic Authentication.
#
# Empty username:
# ""
#
# Password:
# token


# ---------------------------------------------------------
# CHECK AUTHORIZATION HEADER
# ---------------------------------------------------------

print(response.request.headers["Authorization"])

# Output will look like:
# Basic abcdefghijk....

# Explanation:
# Requests encodes:
# :YOUR_GITHUB_TOKEN
#
# using Base64 encoding.


# =========================================================
# 6. CUSTOM TOKEN AUTHENTICATION CLASS
# =========================================================

from requests.auth import AuthBase

class TokenAuth(AuthBase):

    # Constructor
    def __init__(self, token):
        self.token = token

    # Automatically called before request is sent
    def __call__(self, request):

        # Add Authorization header
        request.headers["Authorization"] = f"Bearer {self.token}"

        return request


# =========================================================
# 7. USING CUSTOM TOKEN AUTHENTICATION
# =========================================================

token = "YOUR_GITHUB_TOKEN"

response = requests.get(
    "https://api.github.com/user",
    auth=TokenAuth(token)
)

print(response.status_code)

# Output:
# 200


# ---------------------------------------------------------
# CHECK AUTHORIZATION HEADER
# ---------------------------------------------------------

print(response.request.headers["Authorization"])

# Output:
# Bearer YOUR_GITHUB_TOKEN

# Explanation:
# Our custom authentication class adds:
#
# Authorization: Bearer TOKEN
#
# This is modern token authentication style.


# =========================================================
# 8. HOW CUSTOM AUTH CLASS WORKS
# =========================================================

# class TokenAuth(AuthBase)
#
# We inherit from AuthBase so Requests knows
# this class handles authentication.


# ---------------------------------------------------------
# __init__()
# ---------------------------------------------------------

# def __init__(self, token):
#
# Stores token inside object.


# ---------------------------------------------------------
# __call__()
# ---------------------------------------------------------

# def __call__(self, request):
#
# Requests automatically calls this function
# before sending request.
#
# We modify request headers here.


# =========================================================
# 9. COMPLETE FLOW OF REQUESTS
# =========================================================

# Your Python Code
#        ↓
# Requests Library
#        ↓
# PreparedRequest Created
#        ↓
# Headers Added
#        ↓
# Authentication Added
#        ↓
# JSON Converted to Bytes
#        ↓
# Request Sent to Server
#        ↓
# Response Returned


# =========================================================
# IMPORTANT TERMS
# =========================================================

# PreparedRequest
# Final HTTP request created by Requests.

# Headers
# Extra information sent with request.

# Authorization Header
# Header used for authentication.

# Basic Authentication
# Uses username/password.

# Bearer Authentication
# Uses token.

# Base64 Encoding
# Converts text into encoded format.


# =========================================================
# BASIC AUTHENTICATION HEADER FORMAT
# =========================================================

# Authorization: Basic BASE64(username:password)


# =========================================================
# BEARER TOKEN HEADER FORMAT
# =========================================================

# Authorization: Bearer YOUR_TOKEN


# =========================================================
# WHY USE auth= ?
# =========================================================

# Without auth= you would manually need to:
#
# 1. Create username:password string
# 2. Convert to bytes
# 3. Base64 encode it
# 4. Add Authorization header
# 5. Handle formatting
#
# Requests automates everything.


# =========================================================
# END OF NOTES
# =========================================================