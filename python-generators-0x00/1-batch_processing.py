db_connection = __import__('seed.py').connect_to_prodev()

def stream_users_in_batches(batch_size):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM user_data")
    num_users = cursor.fetchone()[0]
    num_batches = num_users // batch_size
    for i in range(num_batches):
        cursor.execute(f"SELECT * FROM user_data LIMIT {i * batch_size}, {batch_size}")
        users = cursor.fetchall()
        yield users

    cursor.execute(f"SELECT * FROM user_data LIMIT {num_batches * batch_size}, {num_users % batch_size}")
    users = cursor.fetchall()
    yield users

def batch_processing():
    for batch in stream_users_in_batches(10):
        for user in batch:
            if user[3] > 25:
                return user