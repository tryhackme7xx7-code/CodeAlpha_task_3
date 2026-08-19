import os
from flask import Flask, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key is loaded from an environment variable.
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("FLASK_SECRET_KEY is not configured")

# Store a password hash instead of a plaintext password.
USERS = {
    "admin": generate_password_hash("ChangeThisPassword!")
}


@app.route("/")
def home():
    return """
    <h1>CodeAlpha Secure Coding Review</h1>
    <p>Secure Login Application</p>
    <a href="/login">Login</a>
    """


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return "Username and password are required.", 400

        stored_hash = USERS.get(username)

        if stored_hash and check_password_hash(stored_hash, password):
            session["username"] = username
            return redirect(url_for("dashboard"))

        return "Invalid username or password.", 401

    return """
    <h1>Login</h1>

    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>

        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>
    """


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return """
    <h1>Dashboard</h1>
    <p>Login successful.</p>
    <a href="/logout">Logout</a>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
