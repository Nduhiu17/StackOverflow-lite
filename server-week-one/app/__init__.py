from flask import Flask
from flask_restplus import Api

from app.resources import QuestionResource
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(QuestionResource, '/api/v1/questions','/api/v1/questions')



