
class Point:
    def __init__(self, lat, lng):
        self.lat = lat  # int
        self.lng = lng  # int

class Solution:
    def __init__(self, unmatched, routes):
        self.unmatched = unmatched  # list[Point]
        self.routes = routes  # list[list[Point]]

