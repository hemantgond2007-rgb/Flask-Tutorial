from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
load_dotenv()
app=Flask(__name__)
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")
DATABASE_URL=(
    f"mysql+pymysql://"
    f"{DB_USERNAME}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_URL
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__="users"
    id=db.Column(
        db.Integer,
        primary_key=True
    )
    name=db.Column(
        db.String(100),
        nullable=False
    )
    email=db.Column(
        db.String(100),
        primary_key=False
    )
    age=db.Column(
        db.Integer
    )
    orders=db.relationship(
        "Order",
        backref="user",
        lazy=True
    )
class Order(db.Model):
    __tablename__="orders"
    id=db.Column(
        db.Integer,
        primary_key=True
    )
    product=db.Column(
        db.String(100),
        nullable=False
    )
    amount=db.Column(
        db.Float,
        nullable=False
    )
    user_id=db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    

@app.route("/")
def home():
    return "Flask applicatin + My SQL is running !"

@app.route("/users",methods=["POST"])
def creat_user():
    data=request.get_json()
    name=data.get("name")
    age=data.get("age")
    email=data.get("email")

    user=User(
        name=name,
        email=email,
        age=age,
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "message":"user create successfully!",
        "user_id":user.id
    }),201
@app.route("/orders",methods=["POST"])
def creat_order():
    data=request.get_json()
    product=data.get("product")
    amount=data.get("amount")
    user_id=data.get("user_id")

    order=Order(
       product=product,
       amount=amount,
       user_id=user_id
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({
        "message":"order create successfully",
        "order_id":order.id
    })
@app.route("/user/<int:user_id>/orders",methods=["GET"])
def user_order(user_id):
    user=db.get_or_404(User,user_id)
    orders=user.orders
    orders_data=[]
    for order in orders:
        orders_data.append({
            "id":order.id,
            "product":order.product,
            "amount":order.amount
        })
    return jsonify({
            "user":user.name,
            "orders":orders_data
        })

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5000)