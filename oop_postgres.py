import psycopg2
import os
from dotenv import load_dotenv
import time
load_dotenv()
password = os.getenv("PASSWORD")



class DatabaseManager:
    def __init__(self, database_name):
        self.conn = psycopg2.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        start_time=time.time()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id SERIAL PRIMARY KEY,
                            name TEXT,
                            age INTEGER)''')
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to create table is {end_time-start_time} seconds")
        

    def insert_data(self):
        start_time=time.time()
        user_data = []
        while True:
            name = input("Enter the name: ")
            age = input("Enter the age: ")
            user_data.append((name, age))
            if input("Do you want to add more data? (y/n)") == 'n':
                break
        self.cursor.executemany('INSERT INTO users (name, age) VALUES (%s, %s)', user_data)
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to insert data is {end_time-start_time} seconds")
     

    def delete_data(self):
        start_time=time.time()
        user_id = input("Enter the id: ")
        self.cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to delete data is {end_time-start_time} seconds")
      

    def update_data(self):
        start_time=time.time()
        user_id = input("Enter the id: ")
        user_name = input("Enter the name: ")
        user_age = input("Enter the age: ")
        self.cursor.execute('UPDATE users SET name = %s, age = %s WHERE id = %s', (user_name, user_age, user_id))
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to update data is {end_time-start_time} seconds")

    def view_all_data(self):
        start_time=time.time()
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to view all data is {end_time-start_time} seconds")
        
    def delete_all_data(self):
        start_time=time.time()
        self.cursor.execute('DELETE FROM users')
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to delete all data is {end_time-start_time} seconds")

    def view_single_data(self):
        start_time=time.time()
        user_id = input("Enter the id: ")
        self.cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        row = self.cursor.fetchone()
        print(row)
        self.conn.commit()
        end_time=time.time()
        print(f"Time taken to view single data is {end_time-start_time} seconds")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    database_manager = DatabaseManager(f'dbname=postgres user=postgres password= {password} host=localhost port=5432')
    while True:
        print("1. Insert data", "2. Delete data", "3. Update data", "4. View all data", "5. Delete all data",
              "6. View single data", "7. Exit", sep="\n")
        x = int(input("Enter the option: "))

        if x == 1:
            database_manager.create_table()
            database_manager.insert_data()
        elif x == 2:
            database_manager.delete_data()
        elif x == 3:
            database_manager.update_data()
        elif x == 4:
            database_manager.view_all_data()
        elif x == 5:
            database_manager.delete_all_data()
        elif x == 6:
            database_manager.view_single_data()
        else:
            database_manager.close_connection()
            exit()
