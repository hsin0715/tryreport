from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "new world"


@app.route("/ok")
def ok():
    return "ok"


@app.route("/yes")
def yes():
    return "yes"


if __name__ == '__main__':
    app.run()
