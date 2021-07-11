from flask import Flask
from pathlib import Path


app = Flask(__name__, static_folder="./static")


from app import routes