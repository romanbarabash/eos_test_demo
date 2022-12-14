import base64
import email
import re
from email import policy
from typing import List

from retrying import retry

from config import GMAIL_USER_ID
from src.gmail_service.gmail_client import gmail_client
from src.gmail_service.retry_condition import is_list_empty


class MailBodyParser:

    def __init__(self, body):
        self._body = body

    def get_mail_verification_code(self):
        base64_payload = self._body.get_payload()
        mail_decoded = base64.b64decode(base64_payload)
        return re.findall(r'\d{2}-\d{2}', str(mail_decoded))[0]


class MailMessage:

    def __init__(self):
        self.user_id = GMAIL_USER_ID
        self.client = gmail_client()

    def get_messages(self) -> List[dict]:
        messages = self.client.users().messages().list(userId=self.user_id, labelIds=['INBOX']).execute()
        return messages["messages"]

    def get_mime_message(self, msg_id):
        message = self.client.users().messages().get(userId=self.user_id, id=msg_id, format='raw').execute()
        msg_byte = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
        return email.message_from_bytes(msg_byte, policy=policy.default)

    @retry(stop_max_attempt_number=10, wait_fixed=5000, retry_on_result=is_list_empty)
    def get_mime_messages_by_field(self, field, value):
        mime_messages = [self.get_mime_message(msg['id']) for msg in self.get_messages()]
        return [msg for msg in mime_messages if msg.get(field) == value]
