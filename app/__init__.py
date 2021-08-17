from flask import Flask


app = Flask(__name__, static_folder="./static")
app.config["SECRET_KEY"] = "1894634d971c90919080fe90c85882da"


from app import routes