from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect("/payment")
    return render_template("register.html")


@app.route("/payment", methods=["GET", "POST"])
def payment():
    if request.method == "POST":
        return redirect("/dashboard")
    return render_template("payment.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/dashboard")
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/tasks")
def tasks():
    return render_template("tasks.html")


@app.route("/wallet")
def wallet():
    return render_template("wallet.html")


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        return redirect("/dashboard")
    return render_template("withdraw.html")


@app.route("/support")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run(debug=True)
