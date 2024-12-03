import mysql.connector
import pandas as pd

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="steve",
        password="password",
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="steve",
        password="password",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user_data (\
        user_id CHAR(16) PRIMARY KEY,\
        name VARCHAR(255) NOT NULL,\
        email VARCHAR(255) NOT NULL,\
        age DECIMAL NOT NULL\
        )"
    )

def insert_data(connection, data):
    df = pd.read_csv(data)
    cursor = connection.cursor()
    for i in range(len(df)):
        cursor.execute(
            "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
            tuple(df.iloc[i])
        )
    connection.commit()