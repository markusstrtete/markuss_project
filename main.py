import os
import json
import uuid
import random
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "e12345678"  

USERS_FILE = 'users.json'  
MOTIVATION_FILE = 'motivation.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def show_register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        else:
            users = []
    except json.decoder.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        users = []

    name = request.form['name']
    surname = request.form['surname']
    username = request.form['username']
    password = request.form['password']

    if len(username) < 8 or len(password) < 8:
        error_message = "Lietotājvārdam un parolei jābūt vismaz 8 rakstzīmju garumā."
        return render_template('register.html', error_message=error_message)

    if any(user['username'] == username for user in users):
        error_message = "Lietotājvārds jau eksistē. Lūdzu, izvēlieties citu."
        return render_template('register.html', error_message=error_message)

    user_id = str(uuid.uuid4())

    hashed_password = generate_password_hash(password)

    users.append({
        'id': user_id,
        'name': name,
        'surname': surname,
        'username': username,
        'password': hashed_password
    })

    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

    return render_template('dashboard.html', username=username)

@app.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        with open(USERS_FILE, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print(f"User data file '{USERS_FILE}' not found.")
        return "Internal server error. Please try again later."

    username = request.form['username']
    password = request.form['password']

    user = next((user for user in users if user['username'] == username), None)

    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        return redirect(url_for('dashboard'))
    else:
        error_message = "Nederīgs lietotājvārds vai parole. Lūdzu, mēģiniet vēlreiz."
        return render_template('login.html', error_message=error_message)

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('dashboard.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/motivation', methods=['GET', 'POST'])
def motivation():
    text_data = load_text_data()

    if request.method == 'POST':
        motivation_data = load_motivation_data()
        random_motivation = random.choice(motivation_data['motivations'])
        return render_template('motivation.html', text=text_data, random_motivation=random_motivation)

    return render_template('motivation.html', text=text_data)

def load_text_data():
    if os.path.exists('text.json'):
        with open('text.json', 'r') as file:
            text_data = json.load(file)
    else:
        text_data = {}
    return text_data

def load_motivation_data():
    if os.path.exists(MOTIVATION_FILE):
        with open(MOTIVATION_FILE, 'r') as file:
            motivation_data = json.load(file)
    else:
        motivation_data = {}
    return motivation_data

@app.route('/plan')
def plan():
    text_data = {
        "project": "Your Project Name",
        "header": "Welcome to Your Project!",
        "button_register": "Register",
        "button_login": "Login"
        # Add other text data as needed
    }
    return render_template('plan.html', text=text_data)

@app.route('/week_one')
def week_one():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_one.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_two')
def week_two():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_two.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_three')
def week_three():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_three.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_four')
def week_four():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_four.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_five')
def week_five():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_five.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_six')
def week_six():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_six.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_seven')
def week_seven():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_seven.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_eight')
def week_eight():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_eight.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_nine')
def week_nine():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_nine.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_ten')
def week_ten():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_ten.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_eleven')
def week_eleven():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_eleven.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_twelve')
def week_twelve():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twelve.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/week_thirteen')
def week_thirteen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirteen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_fourteen')
def week_fourteen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_fourteen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_fifteen')
def week_fifteen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_fifteen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_sixteen')
def week_sixteen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_sixteen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_seventeen')
def week_seventeen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_seventeen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_eighteen')
def week_eighteen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_eighteen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_nineteen')
def week_nineteen():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_nineteen.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty')
def week_twenty():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_one')
def week_twenty_one():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_one.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_two')
def week_twenty_two():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_two.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_three')
def week_twenty_three():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_three.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_four')
def week_twenty_four():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_four.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_five')
def week_twenty_five():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_five.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_six')
def week_twenty_six():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_six.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_seven')
def week_twenty_seven():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_seven.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_eight')
def week_twenty_eight():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_eight.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_twenty_nine')
def week_twenty_nine():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_twenty_nine.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty')
def week_thirty():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_one')
def week_thirty_one():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_one.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_two')
def week_thirty_two():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_two.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_three')
def week_thirty_three():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_three.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_four')
def week_thirty_four():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_four.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_five')
def week_thirty_five():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_five.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_six')
def week_thirty_six():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_six.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_seven')
def week_thirty_seven():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_seven.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_eight')
def week_thirty_eight():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_eight.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_thirty_nine')
def week_thirty_nine():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_thirty_nine.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty')
def week_forty():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_one')
def week_forty_one():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_one.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_two')
def week_forty_two():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_two.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_three')
def week_forty_three():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_three.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_four')
def week_forty_four():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_four.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_five')
def week_forty_five():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_five.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_six')
def week_forty_six():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_six.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_seven')
def week_forty_seven():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_seven.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_eight')
def week_forty_eight():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_eight.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_forty_nine')
def week_forty_nine():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_forty_nine.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_fifty')
def week_fifty():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_fifty.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_fifty_one')
def week_fifty_one():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_fifty_one.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
@app.route('/week_fifty_two')
def week_fifty_two():
    if 'user_id' in session:
        user_id = session['user_id']
        try:
            with open(USERS_FILE, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            print(f"User data file '{USERS_FILE}' not found.")
            return "Internal server error. Please try again later."

        user = next((user for user in users if user['id'] == user_id), None)

        if user:
            return render_template('week_fifty_two.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

@app.route('/learning')
def learning():
    return render_template('learning.html')

@app.route('/exams')
def exams():
    return render_template('exams.html')

UPLOAD1_FOLDER = 'uploads/task1'
UPLOAD2_FOLDER = 'uploads/task2'
UPLOAD3_FOLDER = 'uploads/task3'

if not os.path.exists(UPLOAD1_FOLDER):
    os.makedirs(UPLOAD1_FOLDER)
if not os.path.exists(UPLOAD2_FOLDER):
    os.makedirs(UPLOAD2_FOLDER)
if not os.path.exists(UPLOAD3_FOLDER):
    os.makedirs(UPLOAD3_FOLDER)

@app.route('/submitted1', methods=['POST'])
def submitted1():
    if 'user_id' in session:
        user_id = session['user_id']
        username = get_username_by_id(user_id)
        user_folder = os.path.join(UPLOAD1_FOLDER, username)
        
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        if has_user_submitted_file(user_folder):
            return render_template('already.html')

        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('selectfile')) 

        filename = file.filename
        filepath = os.path.join(user_folder, filename)
        file.save(filepath)
        return redirect(url_for('submitted1_html'))  # Redirect to submitted1.html
    else:
        return redirect(url_for('login'))

@app.route('/submitted2', methods=['POST'])
def submitted2():
    if 'user_id' in session:
        user_id = session['user_id']
        username = get_username_by_id(user_id)
        user_folder = os.path.join(UPLOAD2_FOLDER, username)
        
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        if has_user_submitted_file(user_folder):
            return render_template('already.html')

        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('selectfile')) 

        filename = file.filename
        filepath = os.path.join(user_folder, filename)
        file.save(filepath)
        return redirect(url_for('submitted2_html'))  # Redirect to submitted2.html
    else:
        return redirect(url_for('login'))

@app.route('/submitted3', methods=['POST'])
def submitted3():
    if 'user_id' in session:
        user_id = session['user_id']
        username = get_username_by_id(user_id)
        user_folder = os.path.join(UPLOAD3_FOLDER, username)
        
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        if has_user_submitted_file(user_folder):
            return render_template('already.html')

        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('selectfile')) 

        filename = file.filename
        filepath = os.path.join(user_folder, filename)
        file.save(filepath)
        return redirect(url_for('submitted3_html'))  # Redirect to submitted3.html
    else:
        return redirect(url_for('login'))

@app.route('/submitted1.html')
def submitted1_html():
    return render_template('submitted1.html')

@app.route('/submitted2.html')
def submitted2_html():
    return render_template('submitted2.html')

@app.route('/submitted3.html')
def submitted3_html():
    return render_template('submitted3.html')

def has_user_submitted_file(user_folder):
    return len(os.listdir(user_folder)) > 0

def get_username_by_id(user_id):
    with open('users.json', 'r') as file:
        users = json.load(file)
    user = next((user for user in users if user['id'] == user_id), None)
    return user['username'] if user else None

@app.route('/selectfile')
def selectfile():
    return render_template('selectfile.html')

@app.route('/task_one')
def task1():
    return render_template('task_one.html')

@app.route('/task_two')
def task2():
    return render_template('task_two.html')

@app.route('/task_three')
def task3():
    return render_template('task_three.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
