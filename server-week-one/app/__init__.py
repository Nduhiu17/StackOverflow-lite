from flask import Flask
from flask_restplus import Api


from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)


