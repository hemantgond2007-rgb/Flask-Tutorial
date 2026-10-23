
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        "python",
        "flask",
        "React",
        "Django"
    ]
    student={
        "Name":"Rohan",
        "City":"Utter Pradesh",
        "Country":"India"
    }

    return render_template("index.html", course=courses,student=student)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
