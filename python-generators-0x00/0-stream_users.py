connect_db = __import__('seed').connect_db

def stream_users():
    connection = connect_db.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    
    cursor.close()
    connection.close()