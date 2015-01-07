from flask import Flask

app = Flask(__name__)
app.config.from_obejct('config')

from app import views
