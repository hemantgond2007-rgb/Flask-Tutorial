
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

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
        greeting="Registration is Successfull"
        if not name:
            return "Name is required"
        if not email:
            return "Email is required"
        if not age:
            return "Age is required"
        if not age.isdigit():
            return "Age Must be a Number"
        return redirect(url_for("success"))
        return render_template("contact.html",greeting=greeting)
    return render_template("contact.html")
@app.route("/success")
def success():
    return "Registration is Success"

if __name__ == "__main__":
    app.run(debug=True,port=5001)
