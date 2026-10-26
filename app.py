
from flask import Flask, render_template,re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def hemant():
    return render_template("about.html")
@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True,port=5000)
