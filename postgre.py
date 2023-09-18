import psycopg
import csv 
import uuid
import string
import random
import os
from password_generator import PasswordGenerator

conn = psycopg.connect("postgres://fcmyqzlp:lGTV9BNw__XkNHIu_W0xNe7ahiOjDq4z@rain.db.elephantsql.com/fcmyqzlp")
cur = conn.cursor()
conn.autocommit = True

pwo = PasswordGenerator()
pwo.minlen = 10
pwo.maxlen = 16

cur.execute("""CREATE TABLE IF NOT EXISTS Users (
            id serial PRIMARY KEY,
            user_id text,
            password text,
            is_available boolean
                )
            """)


for i in range(150):
    
    username = uuid.uuid4()
    password = str(pwo.generate())
    cur.execute(f""" INSERT INTO Users (user_id, password, is_available) VALUES ('{username}', '{password}', TRUE)""")
    if not os.path.isfile("users.csv"):
        with open("users.csv", "a+", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["S.No", "UserId", "Password", "IsAvailable"])
            writer.writerow([i+1, username, password, "Available"])
            continue
        
    with open("users.csv", "a+", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([i+1, username, password, "Available"])
    
    
        