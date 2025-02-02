# Project Description
This is a stage 0 task for the HNG12 internship program

this app is a simple api with a single endpoint (the base uri) that returns
a json dictionary with my email, the current utc time in ISO8601 format, and this github repo url

## Setup Instructions
- install the requirments using "pip install -r requirements.txt"
- run "uvicorn app:app --reload" to run the app locally

## Endpoint
endpoint: '/'
response: {'email': <email>, 'current_time': <current time in iso8601 format>, 'github_url': <the url of the repo it is hosted on>}

You can hire proficent python developers on
* https://hng.tech/hire/python-developers
