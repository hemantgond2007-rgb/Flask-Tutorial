
from flask import Flask, render_template,request,redirect,url_for,flash

app = Flask(__name__)


app.secret_key="Change-this-in-prod "

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404
@app.errorhandler(500)
def internal_server_handler(error):
    return render_template("500.html"),500
@app.route("/test")
def test():
    result = 10/0
    return str(result)
if __name__ == "__main__":
    app.run(debug=False,port=5002)
