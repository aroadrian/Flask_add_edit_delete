from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


def db_connection():
        conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"  
        
        )

        cur = conn.cursor()

         #Delete table if exists
        cur.execute('DROP TABLE IF EXISTS users;')

        # Create table
        cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(150) NOT NULL,
                last_name VARCHAR(150) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                hobbies VARCHAR(50) NOT NULL,
                country VARCHAR(50) NOT NULL
            );
            ''')
        conn.commit()
        cur.close()
        conn.close()