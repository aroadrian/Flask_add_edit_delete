from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app import db
from model import User  # Import the User model from the main app

# Define the Blueprint
register_blueprint = Blueprint('register', __name__)

# Route for the registration page
@register_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']

        # Ensure the age is an integer (with a fallback to None if invalid)
        try:
            age = int(age)
        except ValueError:
            age = None  # You can handle this with a validation message if necessary

        # Hash the password using pbkdf2:sha256
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email is already taken!", 'danger')
            return redirect(url_for('register.register'))

        # Create a new user instance
        new_user = User(first_name=first_name, last_name=last_name, age=age, email=email, password=hashed_password)

        # Add and commit the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("User registered successfully!", 'success')
        return redirect(url_for('index'))  # Redirect to the homepage

    return render_template('register.html')