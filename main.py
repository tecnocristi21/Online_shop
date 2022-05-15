import sqlite3
try:
    sqlite_connection=sqlite3.connect('shop.db')
    cursor=sqlite_connection.cursor()
    print('Succsessfully conneced o SQLite')
    data=cursor.execute("Select * from Product")
    for row in data:
        print(row)
    cursor.close()
except sqlite3.Error as error:
    print('Error while connection sqlite',error)