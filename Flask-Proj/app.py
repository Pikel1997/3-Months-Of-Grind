from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/Home")
def home():
    return "<h1>Hello, Bruh this is the home page</h1>"

@app.route("/About")
def about_info():
    return "<h1>About Us</h1>"


if __name__ == '__main__':
    app.run(debug=True)