from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def home():
   name="Rohan"
   course="Flask"
   return render_template("index.html",name=name,course=course)

if __name__=="__main__":
   app.run(debug=True,port=5001)