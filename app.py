from flask import Flask, render_template, request, redirect, url_for, session
from app.bank_app import BankApp

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Initialize the BankApp instance
bank_app = BankApp()

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    login_msg = bank_app.login(username, password)
    
    if login_msg == "Login successful":
        session['user'] = username  # Store the username in session
        return redirect(url_for('dashboard'))
    
    return render_template('login.html', message="Invalid username or password.")

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user' in session:
        user_info = bank_app.show_account_info()
        return render_template('dashboard.html', account_info=user_info)
    
    return redirect(url_for('home'))

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)  # Remove user from session
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)