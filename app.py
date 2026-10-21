from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Home page"
@app.route("/users")
def users():
    return "welcome to users"
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"

@app.route("/contact")
def contact():
    return "welcome to  contact"
if __name__=="__main__":
    app.run(debug=True)