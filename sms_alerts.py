#!/usr/bin/python3

import os
from twilio.rest import Client

def send_text(text_body):
	auth_token ='xxxx'
	account_sid ='xxxx'
	client = Client(account_sid, auth_token)
	message = client.messages.create(
                body=text_body,
                from_='+15555555555',
                to='+15555555555'
            )

#send_text()
