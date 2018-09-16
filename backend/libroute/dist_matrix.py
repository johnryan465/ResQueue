
def eucl(a, b):
    return (((a.lat - b.lat) ** 2) + ((a.lng - b.lng) ** 2)) ** 0.5

def get_dist_matrix(points):
    dist = [[0] * len(points) for _ in range(len(points))]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist[i][j] = dist[j][i] = eucl(points[i], points[j])
    return dist

