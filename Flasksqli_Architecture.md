# FlaskSQLiLab Architecture and Logic Explanation

**Built and created by Meni – Cybersecurity Lead | 🛡️ CISO | ☁️ CloudSec | 🌐 NetSec (CCNP) | 🔍 Web Pentester | ✍️ Writer** | [X Profile](https://x.com/MeniTasa)

## Overview
FlaskSQLiLab is a deliberately vulnerable Flask web application designed for security enthusiasts and penetration testers to practice SQL injection techniques and understand web security principles including session management, cookie handling, encryption, and backend operations.

## Application Architecture

### Backend (Flask & Python)
The backend logic is built using Python with the Flask web framework, serving HTTP requests, managing routes, and handling user interactions. Flask's simplicity allows clear demonstration of vulnerabilities.

### Database (SQLite3)
SQLite3 is used due to its simplicity and ease of deployment. It stores user credentials, tokens, and other data. The database intentionally lacks input sanitization to illustrate SQL injection vulnerabilities clearly.

### Frontend (HTML & CSS)
The frontend uses straightforward HTML templates styled with basic CSS to provide an intuitive user interface, closely resembling a real-world web application.

## Logic and Components

### Session Handling
Sessions are managed through Flask's session mechanism, storing user login states securely on the server-side. However, the application intentionally mismanages sessions to demonstrate vulnerabilities like session hijacking and fixation.

### Cookie Management
Cookies, particularly the "remember me" cookie, are insecurely handled to explicitly expose cookie-based SQL injection risks. Cookies store plaintext data directly used in database queries, making them susceptible to manipulation.

### Encryption (or Lack Thereof)
The app intentionally avoids proper encryption and hashing methods, storing passwords and sensitive data in plaintext. This practice clearly illustrates the risks of poor cryptographic practices.

## Vulnerabilities and Their Implementation

| Endpoint                 | Injection Technique                        | Explanation & Usage                   |
|--------------------------|--------------------------------------------|---------------------------------------|
| `/` (Login)              | Error-based SQL Injection                   | Authentication bypass                 |
| `/register`              | Error-based SQL Injection                   | Malicious user creation               |
| `/search`                | Error-based SQL Injection                   | Data extraction                       |
| `/profile/<username>`    | UNION-based SQL Injection                   | UNION queries for additional data     |
| `/check_user`            | Blind SQL Injection (Boolean & Time-based)  | Blind enumeration                     |
| `/update_profile`        | Second-order SQL Injection                  | Stored injection                      |
| `/dashboard`             | Cookie-based SQL Injection                  | Cookie manipulation and injection     |
| `/session-info`          | Session and Cookie Manipulation             | Inspect and modify sessions/cookies   |

## Educational Objectives
- Understand and exploit SQL injection vulnerabilities.
- Observe the consequences of insecure session handling and cookie management.
- Recognize the critical need for encryption and proper database input sanitization.

## Ethical Considerations
FlaskSQLiLab must only be used within controlled, isolated educational environments. Always adhere to ethical hacking practices and refrain from deploying such vulnerable configurations publicly or in production.

---

Happy Ethical Hacking!

