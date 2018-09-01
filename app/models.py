import uuid

from datetime import datetime

#create a mock database
MOCK_DATABASE = {
    "questions": [ ],

}


class Question:
    '''Class to model a question'''
    def __init__(self, title, body):
        #method to initialize Question class
        self.id = uuid.uuid4()
        self.title = title
        self.body = body
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

    def save(self):
        #method to save a question
        MOCK_DATABASE[ "questions" ].append(self)
        return self.json_dumps()

    @classmethod
    def get_all(cls):
        all_questions = MOCK_DATABASE[ 'questions' ]
        get_all_json = [ ]
        for item in all_questions:
            get_all_json.append(item.json_dumps())
        return get_all_json

    def json_dumps(self):
        #method to return a json object from the question details
        obj = {
            "id": str(self.id),
            "title": self.title,
            "body": self.body,
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified)
        }
        return obj