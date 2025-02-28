import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Secret key for flash messages and sessions
app.secret_key = 'your_secret_key'

# Database setup (Replace with your PostgreSQL database URL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/postgres'  # Adjust this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# User Model for SQLAlchemy
class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']
        
        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Check if the username or email already exists
        existing_user = User.query.filter((User.email == email)).first()

        if existing_user:
            flash("Username or Email already taken!", 'danger')
            return redirect(url_for('register'))

        # Create a new user instance
        new_user = User(first_name=first_name, last_name=last_name, age=age, email=email, password=hashed_password)

        # Add and commit the user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("User registered successfully!", 'success')
        return redirect(url_for('index'))

    return render_template('register.html')


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