#!/bin/python3
from getpass import getpass
from email.message import EmailMessage
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

if not EMAIL_ADDRESS:
    EMAIL_ADDRESS = input('Enter an email address:\n')

if not EMAIL_PASSWORD:
    EMAIL_PASSWORD = getpass(f'Enter the password for {EMAIL_ADDRESS}:\n')

msg = EmailMessage()
msg['Subject'] = 'Cool subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'mo0th@example.com'
msg.set_content('Cool content')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
