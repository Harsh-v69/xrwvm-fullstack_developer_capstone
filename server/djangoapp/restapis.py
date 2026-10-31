import requests
import os
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = "&".join(f"{k}={v}" for k, v in kwargs.items())
    request_url = backend_url + endpoint + ("?" + params if params else "")
    print(f"GET from {request_url}")
    try:
        return requests.get(request_url).json()
    except Exception as err:
        print(f"Network exception occurred: {err}")


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + quote(text)
    try:
        return requests.get(request_url).json()
    except Exception as err:
        print(f"Network exception occurred: {err}")


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        return requests.post(request_url, json=data_dict).json()
    except Exception as err:
        print(f"Network exception occurred: {err}")
