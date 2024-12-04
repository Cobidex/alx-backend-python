#!/usr/bin/python3
seed = __import__('seed')

def lazy_paginate(page_size):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM user_data")
    total_rows = cursor.fetchone()[0]
    total_pages = total_rows // page_size
    for page in range(total_pages + 1):
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {page_size * page}")
        rows = cursor.fetchall()
        yield rows
    cursor.close()
    connection.close()

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows