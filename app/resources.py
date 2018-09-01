from flask_restplus import Resource, reqparse
from flask import request

from app.models import Question

class QuestionResource(Resource):
    #method that post a question resource
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', help='The title field cannot be blank', required=True, type=str)
        parser.add_argument('body', help='The body field cannot be blank', required=True,type=str)
        data = parser.parse_args()
        json_data = request.get_json(force=True)
        if len(data['title']) < 10:
            return {'message': 'The length of both title should be atleast 10 characters'}, 400
        if len(data['body']) < 20:
            return {'message': 'The length of both body should be atleast 15 characters'}, 400
        question = Question(title=request.json[ 'title' ], body=request.json[ 'body' ])
        saved_question = question.save()
        return {"status": "The length of both title should be atleast 10 characters", "data":saved_question}, 201

    def get(self):
        #method that gets all questions resource
        questions = Question.get_all()
        return {"status": "Success", "data": questions}, 200
