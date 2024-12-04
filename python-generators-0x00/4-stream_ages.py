#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    cursor.close()
    connection.close()

def get_avarage_age():
    ages = stream_user_ages()
    total = 0
    count = 0
    for age in ages:
        total += age
        count += 1
    return total / count