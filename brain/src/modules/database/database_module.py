import sqlite3

def check_database_kns():
    try:
        connection = sqlite3.connect('clients.db')
        cursor = connection.cursor()


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kns_arms (

            name VARCHAR (100) DEFAULT NULL UNIQUE,
            description VARCHAR (100) DEFAULT NULL UNIQUE,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP

        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kns_arms_keep_alive (

            name VARCHAR (100) DEFAULT NULL,
            id_arm INT (10) DEFAULT NULL,
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