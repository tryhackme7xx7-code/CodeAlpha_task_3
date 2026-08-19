from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)


app.secret_key = "my-secret-key-123"


USERS = {
    "admin": "admin123"
}


@app.route("/")
def home():
    return """
    <h1>CodeAlpha Secure Coding Review</h1>
    <p>Welcome to the Login Application</p>
    <a href="/login">Login</a>
    """


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        
        if username in USERS and USERS[username] == password:
            session["username"] = username
            return redirect(url_for("dashboard"))

        return """
        <h3>Invalid username or password</h3>
        <a href="/login">Try again</a>
        """

    return """
    <h1>Login</h1>

    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Password:</label><br>
        <input type="password" name="password"><br><br>

        <button type="submit">Login</button>
    </form>
    """


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]

    return f"""
    <h1>Dashboard</h1>
    <p>Welcome, {username}!</p>
    <p>You are successfully logged in.</p>
    <a href="/logout">Logout</a>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
