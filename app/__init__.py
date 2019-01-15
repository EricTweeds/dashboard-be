from flask import Flask
import os

app = Flask(__name__)

from app import server

port = int(os.environ.get("PORT", 3030))
app.run(host='0.0.0.0', port=port)