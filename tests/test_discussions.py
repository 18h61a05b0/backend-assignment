import unittest
from app import create_app, db

class DiscussionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_discussion(self):
        # First, create a user to associate with the discussion
        self.client.post('/users/signup', json={
            'name': 'John Doe',
            'mobile': '1234567890',
            'email': 'john@example.com',
            'password': 'password'
        })
        
        response = self.client.post('/discussions', json={
            'user_id': 1,
            'text': 'This is a test discussion',
            'image': 'test.jpg',
            'hashtags': '#test'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Discussion created successfully', str(response.data))

if __name__ == '__main__':
    unittest.main()
