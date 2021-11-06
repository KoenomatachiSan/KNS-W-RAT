import sqlite3

def check_database_kns():
    try:
        connection = sqlite3.connect('./clients.db')
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kns_keep_alive (

            name VARCHAR (100) DEFAULT NULL,
            operational_system VARCHAR (100) DEFAULT NULL,
            operational_system_version VARCHAR (100) DEFAULT NULL,
            operational_system_processor VARCHAR (100) DEFAULT NULL,
            general VARCHAR (255) DEFAULT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP

        );
        """)

        
        connection.close()
    except NameError:
        return NameError