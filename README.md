# Student Login System

A simple full project using Python + Flask + MySQL for user signup, login, and welcome page.

## Project Structure

```
ln-sql/
│
├── app.py               ← main Flask backend
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── home.html
└── README.md
```

## Setup

### 1. Create a MySQL Database

Run the following SQL commands in MySQL shell:

```sql
CREATE DATABASE studentdb;
USE studentdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);
```

### 2. Install Dependencies

```bash
pip install flask mysql-connector-python
```

### 3. Update app.py

In `app.py`, replace `"your_mysql_password_here"` with your actual MySQL root password.

### 4. Run the App

```bash
python app.py
```

Then open your browser to `http://127.0.0.1:5000/`

## Features

- User signup
- User login
- Welcome page after login

Note: Passwords are stored in plain text. For production, add encryption.
