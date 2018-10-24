import unittest
import pytrails
from datetime import datetime
from setupLogging import setupLogging
import logging
logger = logging.getLogger(__name__)

class PyTrailsTest(unittest.TestCase):
    def setUp(self):
        setupLogging()
        self.trails = pytrails.PyTrails('test\loc.json', 'json')
    def test(self):
        from_date = datetime(2018, 10, 13)
        to_date = datetime(2018, 10, 18)
        logger.info('get points from ' + str(from_date) + ' to ' + str(to_date))
        points = self.trails.getPoints(from_date, to_date)
        totalPoints = sum(1 for i in points)
        logger.info('total points ' + str(totalPoints))
        self.assertEqual(6555, totalPoints)
