# ============================================
# CUSTOMIZE REQUEST HEADERS IN PYTHON REQUESTS
# ============================================

# The requests library allows us to send HTTP requests easily.
# We can customize requests using:
# 1. params  -> query parameters in URL
# 2. headers -> extra instructions sent to server

# --------------------------------------------
# FULL PROGRAM
# --------------------------------------------

import requests

# Sending GET request to GitHub API
response = requests.get(
    "https://api.github.com/search/repositories",

    # Query string parameters
    # q = search query
    params={"q": '"real python"'},

    # Custom HTTP headers
    headers={
        "Accept": "application/vnd.github.text-match+json"
    },
)

# Convert JSON response into Python dictionary
json_response = response.json()

# Get first repository from results
first_repository = json_response["items"][0]

# Print matching text information
print(first_repository["text_matches"][0]["matches"])


# ============================================
# EXPLANATION
# ============================================

# 1. import requests
# ------------------
# Imports the requests library used for HTTP requests.


# 2. requests.get()
# -----------------
# Sends a GET request to the given URL.

# URL:
# https://api.github.com/search/repositories

# This GitHub API endpoint searches repositories.


# 3. params={}
# ------------
# Adds query parameters to URL.

# Example:
# params={"q": '"real python"'}

# Final URL becomes:
# https://api.github.com/search/repositories?q="real python"

# q means search query.


# 4. headers={}
# -------------
# Sends custom HTTP headers to server.

# Example:
# headers={
#     "Accept": "application/vnd.github.text-match+json"
# }

# The Accept header tells server:
# "Please send response in this format."


# ============================================
# WHAT IS AN HTTP HEADER?
# ============================================

# Headers provide extra information to server.

# Common headers:

# Accept
# -> tells server what type of response we want

# Authorization
# -> used for login/authentication tokens

# User-Agent
# -> tells server about our app/browser


# ============================================
# WHY THIS ACCEPT HEADER?
# ============================================

# "application/vnd.github.text-match+json"

# This is a special GitHub media type.

# It tells GitHub:
# "Include text matching information in response."

# Without this header:
# text_matches field will NOT appear.

# With this header:
# GitHub returns matching text and positions.


# ============================================
# response.json()
# ============================================

# Converts JSON response into Python dictionary.

# JSON from server:
# {
#   "items": [...]
# }

# becomes Python dictionary.


# ============================================
# ACCESSING DATA
# ============================================

# json_response["items"]
# -> gets repository list

# [0]
# -> gets first repository

# ["text_matches"]
# -> gets matching text information

# ["matches"]
# -> gets actual matched text data


# ============================================
# SAMPLE OUTPUT
# ============================================

# [{'text': 'Real Python', 'indices': [23, 34]}]

# Meaning:
# Text "Real Python" was found
# between character positions 23 and 34.


# ============================================
# DIFFERENCE BETWEEN params AND headers
# ============================================

# params
# -------
# Sent in URL
# Used for searching/filtering

# Example:
# params={"q": "python"}

# becomes:
# ?q=python


# headers
# --------
# Sent separately behind the scenes
# Used for metadata/instructions

# Example:
# headers={"Accept": "application/json"}


# ============================================
# REAL WORLD HEADER EXAMPLES
# ============================================

# JSON response header
headers = {
    "Accept": "application/json"
}

# Authentication header
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

# User-Agent header
headers = {
    "User-Agent": "MyPythonApp"
}


# ============================================
# COMPLETE FLOW
# ============================================

# Python Program
#       ↓
# requests.get()
#       ↓
# Send GET request
#       ↓
# Add query parameters
#       ↓
# Add custom headers
#       ↓
# Server processes request
#       ↓
# Server returns JSON response
#       ↓
# response.json()
#       ↓
# Convert JSON → Python dictionary
#       ↓
# Extract needed data
#       ↓
# Print result