from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET, TOKEN_URI


def gmail_client():
    credentials = Credentials(token=None,
                              refresh_token=REFRESH_TOKEN,
                              token_uri=TOKEN_URI,
                              client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET)

    if credentials.expired:
        credentials.refresh(Request())

    client = build('gmail', 'v1', credentials=credentials)
    return client
