from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Let's Play Podball!"