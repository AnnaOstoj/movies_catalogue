from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main/')
def homepage():
    movies = ["Anna", "Adam", "Amber", "Fika", "Anna 2", "Adam 2", "Amber 2", "Fika 2"]
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)