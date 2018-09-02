import json
import unittest
from app import app
from app.models import Answer
from config import TestingConfig


class TestAnswer(unittest.TestCase):
    '''class to test an answer'''

    def setUp(self):
        # setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_init(self):
        # test that an answer is initialized
        self.new_answer = Answer(body="This is how to init python how to init python how to init python")
        self.assertTrue(type(self.new_answer.id), int)
        self.assertEqual(type(self.new_answer), Answer)

    def test_question_posted(self):
        # method to test an answer can be posted
        new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
        response = self.client.post('/api/v1/question/anwsers', data=json.dumps(new_answer),headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_post_short_answer_body(self):
        # test cant post with a short answer body
        new_answer = {'body': 'short body'}
        response = self.client.post('/api/v1/question/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)