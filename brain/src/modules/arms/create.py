import sqlite3

def create_arm(data):
    try:
        connection = sqlite3.connect('clients.db')
        cursor = connection.cursor()

        verifyDuplicates = cursor.execute(f"SELECT * FROM kns_arms where name='{data['name']}'").fetchall()
        if len(verifyDuplicates) <= 0:
            cursor.execute(f"INSERT INTO kns_arms (name,description) VALUES ('{data['name']}','{data['description']}');")
            connection.commit()
        connection.close()
    except NameError:
        return NameError