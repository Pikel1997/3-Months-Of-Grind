from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Pikel Juice',
        'title': 'Post 1',
        'content': 'First post ever!!',
        'date_posted': 'April 13, 2022',
    },
    {
        'author': 'Jikel Puice',
        'title': 'Post 2',
        'content': 'Second post ever!!',
        'date_posted': 'April 14, 2022',
    },
]


@app.route("/")
@app.route("/Home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/About")
def about_info():
    return render_template('about.html', title="About Us")


if __name__ == '__main__':
    app.run(debug=True)
