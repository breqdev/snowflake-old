from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return ""


@app.route("/snowflake")
def snowflake():
    return ""


if __name__ == "__main__":
    app.run()
