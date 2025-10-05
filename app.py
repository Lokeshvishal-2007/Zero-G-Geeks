from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="prathiksha@2007",
    database="studentdb"
)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        return render_template('home.html', name=username)
    else:
        return "❌ Invalid credentials"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return redirect('/')
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
