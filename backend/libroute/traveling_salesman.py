import requests
import json
from util import Point
def tsp_random(start, points, dists):
    from random import shuffle
    shuffle(points)
    return [start] + points

def tsp_greedy(start, points, dists):
    INF = float('infinity')
    pts = [start] + points
    best_path = None
    min_cost = INF
    # Run greedy for every start
    for s in range(len(pts)):
        used = set([s])
        path = [s]
        cost = 0
        # Build rest of path
        for _ in range(len(pts) - 1):
            min_add_cost = INF
            min_add = None
            # Find the nearest point
            prev = path[-1]
            for v in range(len(pts)):
                if v in used:
                    continue
                if dists[pts[prev]][pts[v]] < min_add_cost:
                    min_add = v
                    min_add_cost = dists[pts[prev]][pts[v]]
            path.append(min_add)
            used.add(min_add)
            cost += min_add_cost
        cost += dists[start][pts[path[-1]]]
        if cost < min_cost:
            min_cost = cost
            best_path = path
    # Rotate the list so 0 is the first element
    for i in range(len(best_path)):
        if best_path[i] == 0:
            best_path = best_path[i:] + best_path[:i]
            break
    return [pts[p] for p in best_path]


def tsp_osrm(start, points, dists, start_point):
    url = "http://pleaseresqueue.me:5000/trip/v1/driving/"
    url += str(start_point.lat) + "," + str(start_point.lng) + ";"
    for point in points:
        print(point)
        url += str(point.lat) + "," + str(point.lng) + ";"
    url = url[:-1]
    url += "?source=first&steps=false&geometries=polyline&overview=false&annotations=false"
    print(url)
    response = requests.request("GET", url)
    rep = json.loads(response.text)
    ans = []

    for waypoint in rep['waypoints']:
        ans.append(Point(waypoint['location'][0],waypoint['location'][1]))

    return ans

#Use OSRM instead

traveling_salesman = tsp_greedy
