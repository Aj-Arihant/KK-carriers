from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/services/')
def services():
    return render_template("services.html")


@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
