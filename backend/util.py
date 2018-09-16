
class Point:
    def __init__(self, lat, lng):
        self.lat = int(lat)  # int
        self.lng = int(lng)  # int

    def get_serialisable(self):
        return {
            'lat': self.lat,
            'lng': self.lng
        }

    def __str__(self):
        return '({}, {})'.format(self.lat, self.lng)

    def __repr__(self):
        return str(self)

class Solution:
    def __init__(self):
        self.unmatched = []  # list[Point]
        self.routes = []  # list[list[Point]]

    def __str__(self):
        unmat = 'Unmatched: {}\n'.format(str(self.unmatched))
        routes = 'Routes:\n' + '\n'.join(str(r) for r in self.routes)
        return unmat + routes

    def __repr__(self):
        return str(self)
