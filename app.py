from flask import Flask, request, redirect, url_for, session, render_template, render_template_string, make_response
import sqlite3, os
from flask import jsonify

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

@app.route('/check_user', methods=['GET', 'POST'])
def check_user():
    if request.method == 'POST':
        username = request.form['username']
        conn = get_db_connection()
        query = f"SELECT COUNT(*) FROM users WHERE username='{username}'"
        print(f"[LOG] Executed Query: {query}")  # Logs injected queries explicitly
        user_count = conn.execute(query).fetchone()[0]

        if user_count > 0:
            message = f"User '{username}' exists!"
        else:
            message = f"User '{username}' does not exist!"

        print(f"[DEBUG] Query executed: {query}")  # Clearly show injection attempts in console
        return render_template_string("<p>" + message + "</p><a href='/check_user'>Try again</a>")

    return render_template('check_user.html')

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


@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'username' not in session:
        return jsonify(error="Unauthorized. Please log in first."), 401

    if request.method == 'POST':
        new_username = request.form['new_username']
        conn = get_db_connection()

        # Intentionally vulnerable query (Second-order SQL Injection)
        query = f"UPDATE users SET username='{new_username}' WHERE username='{session['username']}'"
        conn.execute(query)
        conn.commit()

        # Fetch updated user data
        updated_user = conn.execute(f"SELECT * FROM users WHERE username='{new_username}'").fetchone()
        conn.close()

        if updated_user:
            session['username'] = updated_user['username']
            user_data = {
                "id": updated_user["id"],
                "username": updated_user["username"],
                "password": updated_user["password"],
                "remember_token": updated_user["remember_token"]
            }
            return jsonify(message="Profile updated successfully!", user=user_data)

        return jsonify(error="Failed to update profile."), 400

    return render_template('update_profile.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        username = request.form['username']
        conn = get_db_connection()
        query = f"SELECT id, username, password FROM users WHERE username LIKE '%{username}%'"
        rows = conn.execute(query).fetchall()
        conn.close()

        results = [dict(row) for row in rows]

        return jsonify(users=results)

    return render_template('search.html')


@app.route('/session-info')
def session_info():
    session_data = dict(session)
    cookie_data = request.cookies.get('remember_me', 'Not set')

    return jsonify({
        'session_data': session_data,
        'remember_me_cookie': cookie_data
    })


@app.route('/profile/<username>')
def profile(username):
    conn = get_db_connection()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    user = conn.execute(query).fetchone()
    conn.close()

    if user:
        user_data = {
            "id": user["id"],
            "username": user["username"],
            "password": user["password"],
            "remember_token": user["remember_token"]
        }
        return jsonify(user=user_data)
    else:
        return jsonify(error="User not found"), 404

@app.route('/logout')
def logout():
    session.pop('username', None)
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('remember_me')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
