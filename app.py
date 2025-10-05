from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "9f1d1b5c43b2f3a91a9d76bb22e3d1f0"  

# --- Database connection ---
db = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="Harsha@123",     
    database="login"  
)
cursor = db.cursor()

# --- Default route: always go to login page ---
@app.route('/')
def index():
    return redirect(url_for("login"))

# --- Register Route ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            return " Passwords do not match!"

        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, password))
        db.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')

# --- Login Route ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()

        if user:
            session["user"] = user[1]  # store username in session
            return redirect(url_for("home"))  # go to home page
        else:
            return " Invalid email or password."

    # If already logged in, skip login and go to home
    if "user" in session:
        return redirect(url_for("home"))

    return render_template('login.html')

# --- Home Route ---
@app.route('/home')
def home():
    if "user" in session:  # only if logged in
        return render_template("home.html", user=session["user"])
    return redirect(url_for("login"))

# --- Logout Route ---
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
