import requests
from urllib.parse import urljoin
import os
from dotenv import load_dotenv
load_dotenv()

class Requester:
    def __init__(self) -> None:
        self.root = "https://cloud.lambdalabs.com/api/v1/"
        self.api_key = os.getenv('api_key')

    def get(self, endpoint):
        url = urljoin(
            self.root,
            endpoint
        )
        return requests.get(
            url,
            auth=(self.api_key, '')
        ).json()
        
    def post(self, endpoint, payload):
        url = urljoin(
            self.root,
            endpoint
        )
        return requests.post(
            url,
            json=payload,
            auth=(self.api_key, '')
        ).json()