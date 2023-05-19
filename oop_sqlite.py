import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTEGER)''')
        self.conn.commit()

    def insert_data(self):
        user_data = []
        while True:
            name = input("Enter the name: ")
            age = input("Enter the age: ")
            user_data.append((name, age))
            if input("Do you want to add more data? (y/n)") == 'n':
                break
        self.cursor.executemany('INSERT INTO users VALUES (NULL, ?, ?)', user_data)
        self.conn.commit()
        print('Data inserted successfully.')

    def delete_data(self):
        user_id = input("Enter the id: ")
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()
        print('Data deleted successfully.')

    def update_data(self):
        user_id = input("Enter the id: ")
        user_name = input("Enter the name: ")
        user_age = input("Enter the age: ")
        self.cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (user_name, user_age, user_id))
        self.conn.commit()
        print('Data updated successfully.')

    def view_all_data(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.conn.commit()

    def delete_all_data(self):
        self.cursor.execute('DELETE FROM users')
        self.conn.commit()
        print('All data deleted successfully.')

    def view_single_data(self):
        user_id = input("Enter the id: ")
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = self.cursor.fetchone()
        print(row)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
#directly script run huda chai huncha tara as a module import garey ruun hudena
if __name__ == "__main__":
    database_manager = DatabaseManager('example.db')
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
