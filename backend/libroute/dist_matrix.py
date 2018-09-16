import requests

OSRM_REQ = (
    'http://pleaseResQueue.me:5000' +
    '/table/v1/car/{}'
)

def format_points(points):
    return ';'.join('{},{}'.format(p.lng, p.lat) for p in points)

def osrm_dist_matrix(points):
    req = OSRM_REQ.format(format_points(points))
    print(req)
    resp = requests.get(req)
    if resp.status_code != 200:
        print("Status code {}".format(resp.status_code))
        return None
    jresp = resp.json()
    if jresp['code'] != 'Ok':
        print('Response code not okay: {}'.format(jresp))
        return None
    print(jresp['durations'])
    return jresp['durations']

def eucl(a, b):
    return (((a.lat - b.lat) ** 2) + ((a.lng - b.lng) ** 2)) ** 0.5

def eucl_dist_matrix(points):
    dist = [[0] * len(points) for _ in range(len(points))]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist[i][j] = dist[j][i] = eucl(points[i], points[j])
    return dist

get_dist_matrix = osrm_dist_matrix

