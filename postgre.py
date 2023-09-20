# import psycopg
# import csv 
# import uuid
# import string
# import random
# import os
# from password_generator import PasswordGenerator

# conn = psycopg.connect("postgres://fcmyqzlp:lGTV9BNw__XkNHIu_W0xNe7ahiOjDq4z@rain.db.elephantsql.com/fcmyqzlp")
# cur = conn.cursor()
# conn.autocommit = True

# pwo = PasswordGenerator()
# pwo.minlen = 10
# pwo.maxlen = 16

# cur.execute("""CREATE TABLE IF NOT EXISTS Users (
#             id serial PRIMARY KEY,
#             user_id text,
#             password text,
#             is_available boolean
#                 )
#             """)


# for i in range(150):
    
#     username = uuid.uuid4()
#     password = str(pwo.generate())
#     cur.execute(f""" INSERT INTO Users (user_id, password, is_available) VALUES ('{username}', '{password}', TRUE)""")
#     if not os.path.isfile("users.csv"):
#         with open("users.csv", "a+", newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow(["S.No", "UserId", "Password", "IsAvailable"])
#             writer.writerow([i+1, username, password, "Available"])
#             continue
        
#     with open("users.csv", "a+", newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow([i+1, username, password, "Available"])
    
    
        
        
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google_auth_httplib2
import os
import datetime
from datetime import date as datee
from random import randint, choices
import string
import uuid
import base64
import socket
from httplib2 import socks
import httplib2
import inspect
import proxyscrape

try:
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(host='localhost', port=50001)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
except Exception as e:
    print(e)
    
#=======================================================================================================================
current_time = datetime.datetime.now()
date = str(current_time.day) + "-" + str(current_time.month) + "-" + str(current_time.year)
newMessage = MIMEMultipart()
#=======================================================================================================================
# [Invoice Number and Subject]
#=======================================================================================================================
invoiceNo = randint(1000000, 9999999)
transaction_id = randint(10000000000, 99999999999)
rand_string = ''.join(choices(string.ascii_uppercase, k=5))
num = randint(111111111, 999999999)
subject = "Here will be the subject"
# subject = subjectWord
num = randint(111111111, 999999999)
newMessage['Subject'] = subject
newMessage['From'] = f"Hi<syedmuhammad1111@gmail.com>"
#newMessage['From'] = name
newMessage['To'] = "Mirsadur@gmail.com"
# newMessage['bcc'] = ",".join(email)
transaction_id = randint(100000000, 999999999)
random_id = randint(100000000, 999999999)
xyz_id = (uuid.uuid4())


# socket.socket = socks.socksocket
# socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "47.56.110.204", 8989)
# p = httplib2.ProxyInfo(proxy_type=socks.PROXY_TYPE_SOCKS5, proxy_host="103.48.68.36", proxy_port=82)
# theHttp = httplib2.Http(proxy_info = p, timeout=30)

# print(inspect.signature(build))
# collector = proxyscrape.create_collector('default', 'http')  # Create a collector for http resources
# proxy = collector.get_proxy()  # Retrieve a united states proxy
http = httplib2.Http(proxy_info=httplib2.ProxyInfo(
            socks.PROXY_TYPE_HTTP, "212.145.210.146", 80
))
authorized_http = google_auth_httplib2.AuthorizedHttp(creds, http=http)
try:
    service = build('gmail', 'v1', http=authorized_http)
    # with open(file, 'rb') as f:
    #     payload = MIMEBase('application', 'octet-stream', Name=file)
    #     # payload = MIMEBase('application', 'pdf', Name=pdfname)
    #     payload.set_payload(f.read())
    # #=======================================================================================================================
    #     # enconding the binary into base64
    #     encoders.encode_base64(payload)
    # #=======================================================================================================================
    #     # add header with pdf name
    #     payload.add_header('Content-Decomposition',
    #                     'attachment', filename=file)
    #     newMessage.attach(payload)
    #=======================================================================================================================
    # mailserver = smtplib.SMTP_SSL('mail.privateemail.com', 465)
    # mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # mailserver.login(emailId, password)
    # mailserver.sendmail(emailId, email, newMessage.as_string())
    encoded_message = base64.urlsafe_b64encode(newMessage.as_bytes()).decode()

    create_message = {
        'raw': encoded_message
    }
    #=======================================================================================================================
    # mailserver.quit()
    send_message = (service.users().messages().send
                    (userId="me", body=create_message).execute())
    print(F'Message Id: {send_message["id"]}')
    #=======================================================================================================================
    # os.remove(file)
    # os.remove("html_code_1.html")
    #=======================================================================================================================

    #=======================================================================================================================
    # except UnboundLocalError as fileerror:
    #     print(fileerror)
    # remove_email(emailId, password)
    #=======================================================================================================================
    # except smtplib.SMTPResponseException as e:
    #     print(e)
    #     error_code = e.smtp_code
    #     error_message = e.smtp_error
    #     print(f"send to {email} by {emailId} failed")

    #     print(f"error code: {error_code}")
    #     print(f"error message: {error_message}")
except HttpError as error:
    print(F'An error occurred: {error}')
    send_message = None
    # os.remove(file)
    # os.remove("html_code_1.html")
