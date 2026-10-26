
from flask import Flask, render_template,request,redirect,url_for,flash

app = Flask(__name__)


app.secret_key="Change-this-in-prod "

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def hemant():
    return render_template("about.html")
@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=='POST':
        name=request.form.get("username","").strip()
        email=request.form.get("email","").strip()
        age=request.form.get("age","").strip()
        if not name:
            flash("Name is required !","dange")
            return redirect(url_for("contact"))
        if not email:
            flash("Email is required !","danger")
            return redirect(url_for("contact"))
        if not age:
            flash("Age is required !","danger")
            return redirect(url_for("contact"))
        if not age.isdigit():
            return "Age Must be a Number"
        flash("Registration Successfull !","success")
        # return render_template("contact.html")
    return render_template("contact.html")
@app.route("/success")
def success():
    return "Registration is Success"

if __name__ == "__main__":
    app.run(debug=True,port=5001)
