import sqlite3
conn = sqlite3.connect('example.db')


while(1):
    
    print("1. Insert data", "2. Delete data", "3. Update data", "4. View data", "5. Delete all data","6. View Single data","7. Exit", sep="\n")
    x=int(input("Enter the option: "))
        
    if (x==1):
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER)''')
        user_data=[]
        while(1):
            name=input("Enter the name: ")
            age=input("Enter the age: ")
            user_data.append((name,age))
            if(input("Do you want to add more data? (y/n)")=='n'):
                break
        cursor.executemany('INSERT INTO users VALUES (NULL, ?, ?)', user_data)
        conn.commit()
        print('Data inserted successfully.')
    elif(x==2):    
        cursor = conn.cursor()
        user_id=input("Enter the id")
        cursor.execute('DELETE FROM  users WHERE id = ?', (user_id,))
        conn.commit()
        print('Data deleted successfully.')
        
    elif(x==3):
        cursor = conn.cursor()
        user_id=input("Enter the id: ")
        user_name=input("Enter the name: ")
        user_age=input("Enter the age: ")
        cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (user_name, user_age, user_id))
        conn.commit()
        print('Data updated successfully.')
    elif(x==4):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.commit()
        
    elif(x==5):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users')
        conn.commit()
        print('All data deleted successfully.')
    elif(x==6):
        cursor = conn.cursor()
        user_id=input("Enter the id")
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row= cursor.fetchone()
        print(row)
        conn.commit()
    else:
        exit()
    
conn.close()
