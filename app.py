
from flask import Flask, render_template,request

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
        name=request.form.get("username")
        email=request.form.get("email")
        massage=request.form.get("massage")
        return render_template("contact.html",name=name)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)
