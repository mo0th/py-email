#!/bin/python3
from getpass import getpass
from email.message import EmailMessage
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_TARGET = os.environ.get('EMAIL_TARGET')

if not EMAIL_ADDRESS:
    EMAIL_ADDRESS = input("Enter the sender's email address:\n")

if not EMAIL_PASSWORD:
    EMAIL_PASSWORD = getpass(f'Enter the password for {EMAIL_ADDRESS}:\n')

if not EMAIL_ADDRESS:
    EMAIL_TARGET = input("Enter the target email address:\n")

msg = EmailMessage()
msg['Subject'] = 'Cool subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_TARGET
msg.set_content('Cool content')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
