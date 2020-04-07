import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://alan:1234@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
        self.new_question = {
            "question": "Are tests working?",
            "answer": "Yes",
            "difficulty": 1,
            "category": 3
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each successful operation and for expected errors.
    """
    # @app.route("/categories", methods=["GET"])
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['categories'])

    # @app.route("/questions", methods=["GET"])
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'] > 0 )
        self.assertTrue(data['categories'])

    # @app.route("/questions/<int:qid>", methods=["DELETE"])
    def test_delete_question(self):
        res = self.client().delete('/questions/1')
        self.assertEqual(res.status_code, 200)

    # @app.route("/questions", methods=["POST"])
    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)

        self.assertEqual(res.status_code, 200)

    # # @app.route("/questions/search", methods=["POST"])
    def test_questions_search(self):
        res = self.client().post('/questions/search', json={"searchTerm": "largest lake in Africa"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], 1)

    # @app.route("/categories/<int:cid>/questions", methods=["GET"])
    def test_questions_per_category(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'] > 0)

    # # @app.route("/quizzes", methods=["POST"])
    def test_quizz_play(self):
        res = self.client().post('/quizzes', json={"previous_questions": [], "quiz_category": {"type": "Science", "id": 5}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question'])

    # @app.errorhandler(404)
    def test_404_on_get_questions(self):
        res = self.client().get('/questions?page=500')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False )

    # @app.errorhandler(405)
    def test_405_on_add_questions_per_category(self):
        res = self.client().post('/categories/5/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)

    # @app.errorhandler(422)
    def test_422_on_quizz_play(self):
        res = self.client().post('/quizzes', json={'previous_questions': [], 'id': 5})
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()