from flask import Flask, request, redirect, url_for, session, render_template, make_response
import sqlite3, os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        user = conn.execute(query).fetchone()

        if user:
            session['username'] = user['username']
            resp = make_response(redirect(url_for('dashboard')))

            if 'remember' in request.form:
                remember_value = user['username']
                resp.set_cookie('remember_me', remember_value, max_age=3600*24*7)

                # Intentionally vulnerable SQL injection point
                query_update = f"UPDATE users SET remember_token = '{remember_value}' WHERE username = '{username}'"
                conn.execute(query_update)
                conn.commit()

            conn.close()
            return resp

        conn.close()
        return "Invalid credentials!", 401

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        conn.execute(query)
        conn.commit()
        conn.close()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
    elif 'remember_me' in request.cookies:
        remember_cookie = request.cookies.get('remember_me')

        conn = get_db_connection()
        # Intentionally vulnerable SQL injection
        query = f"SELECT username FROM users WHERE remember_token='{remember_cookie}'"
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            session['username'] = user['username']
            username = user['username']
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

    conn = get_db_connection()
    users = conn.execute("SELECT username, password FROM users").fetchall()
    conn.close()

    return render_template('dashboard.html', username=username, users=users)


@app.route('/logout')
def logout():
    session.pop('username', None)
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('remember_me')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
