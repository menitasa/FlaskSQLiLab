# FlaskSQLiLab

FlaskSQLiLab is a deliberately vulnerable Flask web application built specifically for educational purposes. It allows security enthusiasts, penetration testers, and students to practice various SQL injection techniques and better understand web security concepts such as session handling and cookie manipulation.

## ⚠️ Security Disclaimer

**Important:** FlaskSQLiLab is intentionally vulnerable and designed solely for educational and learning purposes. **Never expose or deploy it publicly or use it in a production environment.**

## 📂 Project Structure

```
FlaskSQLiLab/
├── venv/
├── app.py
├── schema.sql
├── users.db
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

## 🚀 Getting Started

### Step 1: Set Up the Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Initialize the Database

```bash
sqlite3 users.db < schema.sql
```

### Step 3: Run the Application

```bash
python app.py
```

Access the application at:
```
http://localhost:5000
```

## 📌 Features & Vulnerabilities

The application contains the following intentionally vulnerable endpoints to practice:

| Endpoint                 | Type of Injection                         | Usage                                 |
|--------------------------|-------------------------------------------|---------------------------------------|
| `/` (Login)              | Error-based SQL Injection                  | Authentication bypass                 |
| `/register`              | Error-based SQL Injection                  | User registration & injection practice|
| `/search`                | Error-based SQL Injection                  | Data extraction                       |
| `/profile/<username>`    | UNION-based SQL Injection                  | Data extraction using UNION queries   |
| `/check_user`            | Blind SQL Injection (Boolean & Time-based) | User enumeration                      |
| `/update_profile`        | Second-order SQL Injection                 | Persistent injection                  |
| `/session-info`          | Session and Cookie Manipulation            | Inspect and modify sessions/cookies   |

## 🎯 Security Challenges

- **Extract Sensitive Data:** Practice injecting malicious payloads to extract usernames and passwords.
- **Modify Cookies:** Experiment by manually modifying the "remember me" cookie to understand cookie vulnerabilities.
- **Session Handling:** Inspect Flask session data to learn how sessions interact with browser cookies.

## 🔧 Technologies Used

- Flask (Python)
- SQLite3
- HTML & CSS

## 📖 Educational Usage

Use this project exclusively in controlled and isolated environments for security training purposes. Always follow ethical guidelines when practicing penetration testing.

---

Happy Hacking!

