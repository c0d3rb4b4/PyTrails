import json
from datetime import datetime
from itertools import takewhile
import logging
logger = logging.getLogger(__name__)

class PyTrails:
    """The Location Data loader class"""
    points = None
    data = None

    def __init__(self, location_file, type):
        if type == 'json':
            logger.info('Loading JSON file ' + location_file)
            self.data = self.loadJSON(location_file)
            logger.info('Reading points')
            self.points = self.readPointsJSON()
        elif type == 'gpx':
            logger.info('Loading GPX file')
            self.data = self.loadJSON(location_file)
            logger.info('Reading points')
            self.points = self.readPointsJSON()
        elif type == 'kml':
            logger.info('Loading KML file')
            self.data = self.loadKML(location_file)
            logger.info('Reading points')
            self.points = self.readPointsKML()
        else:
            return

    def loadJSON(self, location_file):
        with open(location_file) as f:
            return json.load(f)

    def loadGPX(self, location_file):
        raise NotImplementedError

    def loadKML(self, location_file):
        raise NotImplementedError

    def parseJSON(self, point):
        new_point = {}
        for ( k, v ) in point.items():
            if (k == 'latitudeE7') or (k == 'longitudeE7'):
                new_point[k[:len(k)-2]] = v / 10.0 ** 7.0
            elif k == 'timestampMs':
                new_point[k[:len(k)-2]] = datetime.fromtimestamp( float(v) / 1000.0)
            else:
                new_point[k] = v
        return new_point

    def readPointsJSON(self):
        for point in self.data['locations']:
            yield self.parseJSON(point)

    def readPointsGPX(self):
        raise NotImplementedError

    def readPointsKML(self):
        raise NotImplementedError

    def getPoints(self, from_datetime, to_datetime):
        return (point for point in self.points if (point['timestamp'] >= from_datetime) if (point['timestamp'] <= to_datetime) )
