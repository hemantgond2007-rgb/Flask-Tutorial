from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def home():
   is_loged_in=True
   marks=75
   return render_template("index.html",is_loged_in=is_loged_in,
                          marks=marks)

if __name__=="__main__":
   app.run(debug=True,port=5001)