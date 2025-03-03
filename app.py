import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Secret key for flash messages and sessions
app.secret_key = os.urandom(24)

# Database setup (Replace with your PostgreSQL database URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://team_mang:admin@localhost:5432/event_app'  # Adjust this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Register the blueprint for registration
from register import register_blueprint
app.register_blueprint(register_blueprint)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

#from flask import Flask, render_template, request
#import psycopg2
#from templates.model import db_connection



#app = Flask(__name__)

#para matawag pala yung function na db_connect sa model.py

#db_connection()

## Database connection function
#def get_db_connection():
#    try:
 #       conn = psycopg2.connect(
   #         host="localhost",
    #        database="postgres",
    #        user="postgres",
     #       password="admin"
      #  )
      #  return conn
    #except psycopg2.Error as e:
      #  print(f"Error connecting to the database: {e}")
      #  return None



# Check if the Database is Created
#@app.route('/', methods=['GET', 'POST'])
#def create():
 #   if request.method == 'GET':
 #       conn = get_db_connection()
  #      if conn:
  #          cur = conn.cursor()
  #          cur.close()
  #          conn.close()
  #      return render_template('create.html')

   # if request.method == 'POST':  
   #     hobby = request.form.getlist('hobbies')
   #     hobbies = ",".join(map(str, hobby))
   #     first_name = request.form['first_name']
   #    last_name = request.form['last_name']
   #     email = request.form['email']
    #    password = request.form['password']
    #    gender = request.form['gender']
     #   country = request.form['country']

        # Database connection and insertion
     #   conn = get_db_connection()
      #  if conn:
      #      cur = conn.cursor()
      #      cur.execute(
      #          '''INSERT INTO users (first_name, last_name, email, password, gender, hobbies, country)
      #            VALUES (%s, %s, %s, %s, %s, %s, %s)''',
      #          (first_name, last_name, email, password, gender, hobbies, country)
       #     )
       #     conn.commit()
       #     cur.close()
       #     conn.close()
        
       # return render_template('index.html') 
#if __name__ == '__main__':
    #app.run(debug=True)  # Run the app in debug modes