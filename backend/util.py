
class Point:
    def __init__(self, lat, lng, priority=0, weather_sev=0):
        self.lat = float(lat)  # int
        self.lng = float(lng)  # int
        self.priority = int(priority)
        self.weather_sev = int(weather_sev)

    def get_serialisable(self):
        return {
            'lat': self.lat,
            'lng': self.lng
        }

    def scale_with_urgency(self, to_scale, scale_fac=0.1):
        MAX_SUM = 6
        sev_sum = self.priority + self.weather_sev
        scale_by = scale_fac * (sev_sum / MAX_SUM)
        return to_scale * (1 - scale_by)

    def __str__(self):
        return '({}, {})'.format(self.lat, self.lng)

    def __repr__(self):
        return str(self)

class Solution:
    def __init__(self):
        self.unmatched = []  # list[Point]
        self.routes = []  # list[list[Point]]

    def get_list(self):
        f = list(list(k.get_serialisable() for k in r ) for r in self.routes)
        print(f)
        return f

    def __str__(self):
        unmat = 'Unmatched: {}\n'.format(str(self.unmatched))
        routes = 'Routes:\n' + '\n'.join(str(r) for r in self.routes)
        return unmat + routes

    def __repr__(self):
        return str(self)
