from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from src.gmail_service import refresh_token, token_uri, client_id, client_secret


def gmail_client():
    credentials = Credentials(token=None,
                              refresh_token=refresh_token,
                              token_uri=token_uri,
                              client_id=client_id,
                              client_secret=client_secret)

    if credentials.expired:
        credentials.refresh(Request())

    client = build('gmail', 'v1', credentials=credentials)
    return client
