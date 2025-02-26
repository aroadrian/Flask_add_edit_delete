from flask import Flask, render_template, request
from templates.model import db_connection
import psycopg2


app = Flask(__name__)

#para matawag pala yung function na db_connect sa model.py

db_connection()

#Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="admin"  )
    return conn


get_db_connection()

# Check if the Database is Created
@app.route('/', methods = ['GET','POST'])
def create():
     if request.method == 'GET':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.close()
        conn.close()
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug modes