import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('BBC SPORT',"Sala hits 100th Goal in Liverpool win",'https://www.bbc.com/sport/football/58437041','Sports')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))