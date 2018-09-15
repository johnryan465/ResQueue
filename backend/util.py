
class Point:
    def __init__(self, lat, lng):
        self.lat = lat  # int
        self.lng = lng  # int

class Solution:
    def __init__(self, unmatched, routes):
        self.unmatched = unmatched  # list[Point]
        self.routes = routes  # list[list[Point]]

class UF:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def _get_root(self, i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def is_joined(self, a, b):
        return self._get_root(a) == self._get_root(b)

    def join(self, a, b):
        a, b = self._get_root(a), self._get_root(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


