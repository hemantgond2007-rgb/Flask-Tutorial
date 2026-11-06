

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)


@app.route("/")
def home():
    return "Flask + SQLite is working"


@app.route("/created-user", methods=["POST"])
def created_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    user = User(
        name=name,
        email=email,
        age=age
    )
    
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user_id": user.id
    })

@app.route("/get_users",methods=["GET"])
def get_users():
    users=User.query.all()
    users_data=[]
    for user in users:
        users_data.append({
            "id":user.id,
            "name":user.name,
            "email":user.email,
            "age":user.age
        })
    return jsonify(users_data)
@app.route("/users/<int:id>")
def get_user(id):
    user=db.get_or_404(User,id)
    return jsonify({
        "id":user.id,
        "name":user.name,
        "email":user.email,
        "age":user.age
    })
@app.route("/users/<int:id>",methods=["PATCH"])
def updated_user(id):
    data=request.get_json()
    user=db.get_or_404(User,id)
    if "name" in data:
        user.name=data["name"]
    if "email" in data:
            user.email=data["email"]
    if "age" in data:
            user.age=data["age"]
    db.session.commit()
    return jsonify({
         "massgae":"user updated successfully",
         "user":{
              "id":user.id,
              "name":user.name,
              "email":user.email,
              "age":user.age
         }
    })
@app.route("/user/<int:id>",methods=["DELETE"])
def delete_user(id):
    user=db.get_or_404(User,id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({
         "message":"user delete successfully !"
    })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5002)
