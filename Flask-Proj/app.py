from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/Home")
def home():
    return render_template('home.html')

@app.route("/About")
def about_info():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)