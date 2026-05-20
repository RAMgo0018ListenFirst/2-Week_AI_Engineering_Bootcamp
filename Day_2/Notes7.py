# ============================================================
# SECURE COMMUNICATION + PERFORMANCE IN PYTHON REQUESTS
# COMPLETE BEGINNER NOTES
# ============================================================

# Requests library:
# Used to send HTTP requests in Python

# HTTPS:
# Secure version of HTTP

# TLS/SSL:
# Encryption technology used in HTTPS
# Protects passwords, tokens, banking info, etc.

# ============================================================
# 1. SIMPLE SECURE HTTPS REQUEST
# ============================================================

import requests

response = requests.get("https://api.github.com")

print(response.status_code)

# Explanation:
# - HTTPS uses TLS encryption
# - Requests automatically verifies the server certificate
# - If certificate is valid, connection becomes secure


# ============================================================
# 2. CUSTOM CERTIFICATE VERIFICATION
# ============================================================

import requests

response = requests.get(
    "https://internal-api.company.com",
    verify="/path/to/company-ca.pem"
)

print(response.status_code)

# Explanation:
# - Some companies use private certificates
# - verify parameter tells Requests:
#   "Trust this certificate too"
# - Useful in corporate/internal systems


# ============================================================
# 3. DISABLING CERTIFICATE VERIFICATION (DANGEROUS)
# ============================================================

import requests

response = requests.get(
    "https://api.github.com",
    verify=False
)

print(response.status_code)

# Explanation:
# - verify=False disables security checks
# - Requests shows InsecureRequestWarning
# - Dangerous because attackers can fake servers
# - Vulnerable to Man-in-the-Middle attacks
# - NEVER use in production


# ============================================================
# 4. REQUEST TIMEOUT
# ============================================================

import requests

response = requests.get(
    "https://api.github.com",
    timeout=3
)

print(response.status_code)

# Explanation:
# - timeout=3 means:
#   Wait maximum 3 seconds
# - Prevents application from hanging forever
# - VERY IMPORTANT in real applications


# ============================================================
# 5. VERY SMALL TIMEOUT (CAUSES ERROR)
# ============================================================

import requests

response = requests.get(
    "https://api.github.com",
    timeout=0.001
)

print(response.status_code)

# Possible Error:
# requests.exceptions.ConnectTimeout

# Explanation:
# - 0.001 second is too small
# - Connection could not be established in time


# ============================================================
# 6. CONNECT TIMEOUT + READ TIMEOUT
# ============================================================

import requests

response = requests.get(
    "https://api.github.com",
    timeout=(3, 5)
)

print(response.status_code)

# Explanation:
# timeout=(3, 5)

# 3 seconds:
# Time allowed to establish connection

# 5 seconds:
# Time allowed to receive response data

# This is better than single timeout value


# ============================================================
# 7. HANDLING TIMEOUT EXCEPTION
# ============================================================

import requests
from requests.exceptions import Timeout

try:

    response = requests.get(
        "https://api.github.com",
        timeout=(3, 5)
    )

except Timeout:

    print("Request timed out")

else:

    print("Request successful")

# Explanation:
# - try block runs risky code
# - except catches timeout errors
# - else runs if no exception occurs
# - Makes program safer


# ============================================================
# 8. NORMAL REQUESTS WITHOUT SESSION
# ============================================================

import requests

response1 = requests.get("https://api.github.com")
response2 = requests.get("https://api.github.com")
response3 = requests.get("https://api.github.com")

print(response1.status_code)

# Explanation:
# - Each request creates a NEW connection
# - TLS handshake happens every time
# - Slower performance


# ============================================================
# 9. USING SESSION OBJECT
# ============================================================

import requests

with requests.Session() as session:

    response1 = session.get("https://api.github.com")

    response2 = session.get("https://api.github.com")

    print(response1.status_code)
    print(response2.status_code)

# Explanation:
# - Session reuses connections
# - Faster than normal requests
# - Saves network overhead
# - Connection pooling improves performance

# with statement:
# Automatically closes session resources


# ============================================================
# 10. STORING HEADERS IN SESSION
# ============================================================

import requests

with requests.Session() as session:

    session.headers = {
        "Authorization": "Bearer MY_TOKEN"
    }

    response = session.get("https://api.github.com")

    print(response.status_code)

# Explanation:
# - Session stores common headers
# - Every request automatically uses them
# - Useful for authentication


# ============================================================
# 11. SESSION WITH AUTHENTICATION
# ============================================================

import requests

with requests.Session() as session:

    session.auth = ("username", "password")

    response = session.get("https://httpbin.org/basic-auth/user/pass")

    print(response.status_code)

# Explanation:
# - session.auth stores login credentials
# - Credentials reused across requests
# - No need to pass auth every time


# ============================================================
# 12. RETRY FAILED REQUESTS
# ============================================================

import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(

    total=2,

    status_forcelist=[
        429,
        500,
        502,
        503,
        504
    ]
)

adapter = HTTPAdapter(
    max_retries=retry_strategy
)

session = requests.Session()

session.mount("https://", adapter)

response = session.get("https://api.github.com")

print(response.status_code)

# Explanation:
# Retry object:
# Defines retry behavior

# total=2:
# Retry maximum 2 times

# status_forcelist:
# Retry only for these status codes

# 429 = Too Many Requests
# 500 = Internal Server Error
# 502 = Bad Gateway
# 503 = Service Unavailable
# 504 = Gateway Timeout

# HTTPAdapter:
# Applies retry configuration

# session.mount():
# Attaches adapter to all HTTPS requests


# ============================================================
# 13. HANDLING RETRY ERRORS
# ============================================================

import requests

from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=2
)

adapter = HTTPAdapter(
    max_retries=retry_strategy
)

with requests.Session() as session:

    session.mount("https://", adapter)

    try:

        response = session.get(
            "https://api.github.com"
        )

        print(response.status_code)

    except RetryError as err:

        print("Retry failed")
        print(err)

# Explanation:
# - RetryError happens if all retries fail
# - try-except prevents program crash


# ============================================================
# 14. COMPLETE PRODUCTION STYLE EXAMPLE
# ============================================================

import requests

from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout
from urllib3.util.retry import Retry

# Retry configuration
retry_strategy = Retry(

    total=3,

    status_forcelist=[
        429,
        500,
        502,
        503,
        504
    ]
)

# Transport adapter
adapter = HTTPAdapter(
    max_retries=retry_strategy
)

# Session object
session = requests.Session()

# Attach adapter
session.mount("https://", adapter)

try:

    response = session.get(

        "https://api.github.com",

        timeout=(3, 5)
    )

    print("Status Code:", response.status_code)

except Timeout:

    print("Request timed out")

# Features included:
# - HTTPS security
# - TLS certificate verification
# - Connection reuse
# - Retry system
# - Timeout handling


# ============================================================
# IMPORTANT INTERVIEW POINTS
# ============================================================

# HTTPS:
# Secure version of HTTP

# TLS/SSL:
# Encryption used in HTTPS

# verify parameter:
# Controls certificate verification

# verify=False:
# Disables security checks (dangerous)

# timeout:
# Prevents app from waiting forever

# Session:
# Reuses connections for better performance

# Retry:
# Automatically retries failed requests

# HTTPAdapter:
# Configures retry and connection behavior


# ============================================================
# BEST PRACTICES
# ============================================================

# GOOD:
requests.get(url, timeout=5)

# BAD:
requests.get(url)

# GOOD:
# Use Session for multiple requests

# GOOD:
# Use retries for unstable APIs

# GOOD:
# Keep certificate verification enabled

# BAD:
verify=False

# NEVER use verify=False in production


# ============================================================
# END OF NOTES
# ============================================================