# ============================================
# ADDING QUERY STRING PARAMETERS IN REQUESTS
# ============================================

# Query parameters are extra values added to a URL
# to customize the GET request.

# Example:
# https://api.github.com/search/repositories?q=language:python&sort=stars

# Everything after ? is called the query string.


# ============================================
# IMPORT REQUESTS
# ============================================

import requests

# Imports the Requests library.
# Requests helps us send HTTP requests easily.


# ============================================
# BASIC GET REQUEST WITH QUERY PARAMETERS
# ============================================

response = requests.get(
    "https://api.github.com/search/repositories",

    # params adds query string parameters automatically
    params={
        "q": "language:python",   # Search repositories written in Python
        "sort": "stars",          # Sort by stars
        "order": "desc"           # Descending order (highest first)
    }
)

# Final URL created automatically:
# https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc


# ============================================
# CONVERT RESPONSE TO JSON
# ============================================

json_response = response.json()

# .json() converts JSON data into a Python dictionary.


# ============================================
# ACCESS REPOSITORY LIST
# ============================================

popular_repositories = json_response["items"]

# "items" contains the list of repositories.


# ============================================
# LOOP THROUGH FIRST 3 REPOSITORIES
# ============================================

for repo in popular_repositories[:3]:

    # repo is one dictionary containing repository data

    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}\n")


# ============================================
# EXPLANATION OF F-STRING SYNTAX
# ============================================

# f""

# f-string lets us insert variables directly into strings.

# Example:

name = "Ram"
print(f"My name is {name}")

# Output:
# My name is Ram


# ============================================
# ACCESSING DICTIONARY VALUES
# ============================================

# repo is a dictionary.

# Example dictionary:

student = {
    "name": "Ram",
    "age": 20
}

print(student["name"])

# Output:
# Ram


# In the GitHub example:

repo["name"]

# means:
# Get the value stored under key "name"


# ============================================
# DIFFERENT WAYS TO PASS params
# ============================================


# --------------------------------------------
# 1. USING DICTIONARY (MOST COMMON)
# --------------------------------------------

requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": "language:python",
        "sort": "stars",
        "order": "desc"
    }
)

# Clean and easy to read.



# --------------------------------------------
# 2. USING LIST OF TUPLES
# --------------------------------------------

requests.get(
    "https://api.github.com/search/repositories",
    params=[
        ("q", "language:python"),
        ("sort", "stars"),
        ("order", "desc")
    ]
)

# Useful when order matters
# or duplicate keys are needed.



# --------------------------------------------
# 3. USING BYTES
# --------------------------------------------

requests.get(
    "https://api.github.com/search/repositories",
    params=b"q=language:python&sort=stars&order=desc"
)

# Less commonly used.


# ============================================
# PRINT FINAL URL
# ============================================

response = requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": "language:python",
        "sort": "stars"
    }
)

print(response.url)

# Output:
# https://api.github.com/search/repositories?q=language:python&sort=stars


# ============================================
# WHY USE params?
# ============================================

# Without params:

requests.get(
    "https://api.github.com/search/repositories?q=language:python"
)

# Harder to manage.


# Better way:

requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python"}
)

# Requests automatically:
# - adds ?
# - adds &
# - encodes special characters


# ============================================
# IMPORTANT CONCEPT
# ============================================

# GET requests usually:
# - retrieve data
# - do NOT modify server data

# Query parameters help:
# - search data
# - filter data
# - sort data


# ============================================
# QUICK SUMMARY
# ============================================

# requests.get() -> sends GET request

# params={} -> adds query parameters to URL

# response.json() -> converts JSON into Python dictionary

# json_response["items"] -> accesses repository list

# repo["name"] -> gets dictionary value

# f"" -> inserts variables into strings


# ============================================
# COMPLETE MINI PROJECT
# ============================================

import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={
        "q": "language:python",
        "sort": "stars",
        "order": "desc"
    }
)

data = response.json()

repositories = data["items"]

for repo in repositories[:5]:

    print(f"Repository Name : {repo['name']}")
    print(f"Description     : {repo['description']}")
    print(f"Stars           : {repo['stargazers_count']}")
    print("-" * 40)
