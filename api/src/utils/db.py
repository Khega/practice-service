import mysql.connector

def db_get_data(query):
    db_config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "root",
        "database": "mysqlsampledatabase",
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()
        conn.close()
