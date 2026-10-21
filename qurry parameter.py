from flask import Flask
from uuid import UUID
app = Flask(__name__)
@app.route("/")
def home():
    return "Home page"

@app.route("/id/<int:amount>")
def id(amount):
    return f"id is : {amount}"

@app.route("/user/<string:name>")
def user(name):
    return f"User name is: {name}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"amount is: {amount}"


@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)

if __name__=="__main__":
   app.run(debug=True, port=5001)