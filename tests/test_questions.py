import unittest
from app import app
from app.models import Question
from config import TestingConfig


class TestQuestion(unittest.TestCase):

    def setUp(self):

        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_init(self):
        self.new_question = Question(title="how to init python",body="how to init python how to init python how to init python")
        self.assertTrue(type(self.new_question.id), int)
        self.assertEqual(type(self.new_question), Question)