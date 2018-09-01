from flask import Flask
from flask_restplus import Api

from app.models import Question
from app.resources import QuestionResource
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(QuestionResource, '/api/v1/questions','/api/v1/questions')


def seeding():
    #this method seeds question data
    new_question = Question(title="error sit voluptatem accusantium doloremque laudantium?",body="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium")
    new_question.save()

seeding()
