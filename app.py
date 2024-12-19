import json
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.github import make_github_blueprint, github
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import hashlib

app = Flask(__name__)
app.secret_key = "d8b3cc8ff96741aa4b4f213a9b8e57ff"  # Replace with a secure key

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load models, scaler, and label encoder
logreg_chd = joblib.load('logreg_chd_model.pkl')
logreg_disease = joblib.load('logreg_disease_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

USERS_FILE = 'users.json'
REVIEWS_FILE = "static/reviews.json"
DATA_FILE = "data.json"


# Load existing user data
def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
# Save users' data to file
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)
# Load existing data
def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error("Data file is empty or corrupted. Returning empty data.")
    return []
# Save new data to the file
def save_data(new_entry):
    data = load_data()
    data.append(new_entry)
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Load reviews from file
def read_reviews():
    if os.path.exists(REVIEWS_FILE):
        with open(REVIEWS_FILE, "r") as file:
            return json.load(file)
    return []


# Write reviews to file
def write_reviews(reviews):
    with open(REVIEWS_FILE, "w") as file:
        json.dump(reviews, file, indent=4)


# Load users at app startup
users_db = load_users()

@app.route('/save_data', methods=['POST'])
def save_data_route():
    """Endpoint to save user data."""
    data = request.get_json()
    if data.get('save') == 'yes':
        entry = {
            "name": data.get("name"),
            "result": data.get("result"),
        }
        save_new_data(entry)  # Call the renamed helper function
        logging.info(f"Saved data: {entry}")
    return jsonify({"message": "Data saved successfully!"}), 200

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/data')
def database():
    """Display stored data."""
    data = load_data()
    return render_template('data.html', data=data)


@app.route('/predictor')
def predictor():
    return render_template('predictor.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle predictions."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        required_fields = ['age', 'sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}'}), 400

        features = [
            float(data.get('age')),
            float(data.get('sex_male')),
            float(data.get('cigsPerDay')),
            float(data.get('totChol')),
            float(data.get('sysBP')),
            float(data.get('glucose'))
        ]

        input_data = np.array(features).reshape(1, -1)
        input_data_scaled = scaler.transform(input_data)

        chd_prediction = logreg_chd.predict(input_data_scaled)[0]
        disease_prediction = "No Heart Disease Detected"
        if chd_prediction == 1:
            disease_prediction = label_encoder.inverse_transform(
                logreg_disease.predict(input_data_scaled)
            )[0]

        result = f"Person {'Has' if chd_prediction == 1 else 'Does Not have'} Heart Disease with {disease_prediction}"
        
        response = {'TenYearCHD': int(chd_prediction), 'DiseaseType': disease_prediction, 'result': result}
        return jsonify(response), 200

    except ValueError as e:
        logging.error(f"Value error: {e}")
        return jsonify({'error': 'Invalid input format'}), 400
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({'error': 'Internal server error occurred'}), 500


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form and review submissions."""
    reviews = read_reviews()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            logging.info(f"Contact message received from {name}: {message}")
            flash("Your message has been received!", "info")

        reviewer = request.form.get('reviewer')
        review_text = request.form.get('review-text')
        rating = request.form.get('rating')

        if reviewer and review_text and rating:
            try:
                rating = int(rating)
                if 1 <= rating <= 5:
                    review_entry = {"name": reviewer, "review": review_text, "rating": rating}
                    reviews.append(review_entry)
                    write_reviews(reviews)
                    flash("Thank you for your review!", "success")
            except ValueError:
                flash("Invalid rating value!", "danger")

        return redirect(url_for('contact'))

    top_reviews = sorted(reviews, key=lambda x: x['rating'], reverse=True)[:3]
    return render_template('contact.html', reviews=top_reviews)


@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    """Handle user data submission."""
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        result = data.get('result')  # Ensure 'result' is captured correctly

        if name and result:
            new_entry = {"name": name, "result": result}
            save_data(new_entry) 
            return jsonify({"message": "Data saved successfully!"}), 200
        return jsonify({"error": "Missing 'name' or 'result'."}), 400

    # Display stored data
    stored_data = load_data() if os.path.exists(DATA_FILE) else []
    return render_template('data.html', data=stored_data)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users_db and check_password_hash(users_db[email]["password"], password):
            session["user"] = email
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password.", "danger")
    
    return render_template("login.html")

@app.route("/oauth_login")
def oauth_login():
    if google.authorized:
        resp = google.get("/oauth2/v2/userinfo")
        user_info = resp.json()
        session["user"] = user_info["email"]
        flash("Logged in using Google!", "success")
    elif github.authorized:
        resp = github.get("/user")
        user_info = resp.json()
        session["user"] = user_info["login"]
        flash("Logged in using GitHub!", "success")
    else:
        flash("OAuth login failed. Please try again.", "danger")
        return redirect(url_for("login"))
    
    return redirect(url_for("home"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        errors = []
        # Validation
        if not username or len(username) < 3:
            errors.append("Username must be at least 3 characters long.")
        if not email or "@" not in email or "." not in email:
            errors.append("Invalid email format.")
        if email in users_db:
            errors.append("Email already registered.")
        if not password or len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password):
            errors.append("Password must contain at least one number.")
        elif not any(char.isalpha() for char in password):
            errors.append("Password must contain at least one letter.")
        if password != confirm_password:
            errors.append("Passwords do not match.")

        if errors:
            for error in errors:
                flash(error, "danger")
            return redirect(url_for("signup"))

        # Save new user to database
        users_db[email] = {
            "username": username,
            "password": generate_password_hash(password)
        }
        save_users(users_db)  # Persist data to file
        flash("Signup successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        flash("Please log in to access the dashboard.", "warning")
        return redirect(url_for("login"))
    
    user_email = session["user"]
    username = users_db[user_email]["username"]
    return render_template("dashboard.html", username=username, email=user_email)

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    """Endpoint to fetch logged-in user's information."""
    if 'user' in session:
        user_email = session['user']
        if user_email in users_db:
            user_data = users_db[user_email]
            return jsonify({
                'email': user_email,
                'username': user_data['username']
            }), 200
        else:
            return jsonify({'error': 'User not found in database'}), 404
    return jsonify({'error': 'User not logged in'}), 401


if __name__ == '__main__':
    app.run(debug=True)
