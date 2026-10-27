
from flask import Flask, render_template,request,redirect,url_for,flash,session
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")

@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method=="POST":
        file=request.files.get("file")
        if not file:
            return "Please select file!"
        if file.filename=="":
            return "Please select file!"
        file.save(os.path.join("uploads",file.filename))
        return "file uploaded"
    return render_template("upload.html")
@app.route("/login")
def  login():
    session["username"]="Mohit"
    return "Login successfull !"

@app.route("/dashboard")
def dashboard():
    username=session.get("username",None)
    if not username:
        return"login first please !"
    return f"Welocome {username}"

@app.route("/logout")
def logout():
      session.pop("username", None)
      return "Logout successful!"

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
    app.run(debug=True,port=5001)
