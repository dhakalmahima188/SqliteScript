import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("PASSWORD")

conn = psycopg2.connect(database="postgres", user="postgres", password=password, host="localhost", port="5432")


cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS destination_user
                    (id SERIAL PRIMARY KEY,
                    name TEXT,
                    age INTEGER)''')

insert_query = "INSERT INTO destination_user (name, age) SELECT name, age FROM users"
cursor.execute(insert_query)
cursor.execute("SELECT * FROM destination_user")
rows = cursor.fetchall()
print(rows)


conn.commit()


cursor.close()
conn.close()
