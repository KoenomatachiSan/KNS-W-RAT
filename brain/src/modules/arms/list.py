import sqlite3

def list_arm():
    response = []
    try:
        connection = sqlite3.connect('./clients.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM kns_arms;")
        for linha in cursor.fetchall():
            response.append({
                'name': str(linha[0]),
                'description': str(linha[1]),
                'created_at': str(linha[2]),
            })
            
        connection.close()
        return response
    except NameError:
        return NameError