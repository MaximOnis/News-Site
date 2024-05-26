import unittest
from app import app, session
from model import News
from datetime import datetime


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Create a test news item
        self.news_item = News(
            NewsID=1546666666,
            Theme="Sport",
            Title="Test News",
            Text="Test content",
            MediaPath="path/to/image",
            Date=datetime.now()
        )
        session.add(self.news_item)
        session.commit()

    def tearDown(self):
        # Remove the test news item
        session.delete(self.news_item)
        session.commit()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test News', response.data)

    def test_sport_news_page(self):
        response = self.app.get('/templates/sports_news.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test News', response.data)

    def test_news_detail_page(self):
        response = self.app.get('/templates/1546666666')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test News', response.data)

    def test_filter_news_by_date(self):
        response = self.app.post('/', data=dict(
            start_date='2024-01-01',
            end_date='2024-12-31'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test News', response.data)

    def test_no_news_found(self):
        response = self.app.get('/templates/business_news.html')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test News', response.data)

    def test_found_about(self):
        response = self.app.get('/templates/about-us.html')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test News', response.data)


if __name__ == '__main__':
    unittest.main()
