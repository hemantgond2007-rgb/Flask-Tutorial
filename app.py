from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def home():
   first_name="Rohan"
   Last_name="Singh"
   course=["python",
           "flask",
           "Django",
           "Fast Api"]
   age=20
   price=500
   return render_template("index.html",first_name=first_name,
                          Last_name=Last_name,
                          course=course,
                          age=age,
                          price=price,

                          
                          )

if __name__=="__main__":
   app.run(debug=True,port=5001)