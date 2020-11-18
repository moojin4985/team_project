from flask import flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=true, port=9000)