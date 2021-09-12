import unittest
from app import News_Source

class SourceTest(unittest.TestCase):

    '''
    Test Class to test the behaviour of the News_Source class.
    
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News_Source('BBC-News','BBC News',' Great things happen when we work together.','http://127.0.0.1:5000/news/bbc-news')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_Source))