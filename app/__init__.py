from flask import Flask
import os

app = Flask(__name__)

from app import server

port = int(os.environ.get("PORT", 33507))
app.run(debug=True, port=port)