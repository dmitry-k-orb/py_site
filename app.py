from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    perem = "Вася"
    return render_template('index.html', perem=perem)

@app.route("/about")
def about():
    return "Hello on About page"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
