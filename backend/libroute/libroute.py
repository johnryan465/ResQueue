from util import Point, Solution
from libroute import union_find

def eucl(a, b):
    return (((a.lat - b.lat) ** 2) + ((a.lng - b.lng) ** 2)) ** 0.5

def get_dist_matrix(points):
    dist = [[0] * len(points) for _ in range(len(points))]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist[i][j] = dist[j][i] = eucl(points[i], points[j])
    return dist

def get_clusters(people, vehicle_sizes, dists):
    vsizes = sorted(vehicle_sizes, reverse=True)
    # Node 0 shall be a special node that indicates
    # the cluster has been assigned to a vehicle.
    uf = union_find.UF(len(people) + 1)
    edges = []
    for i in range(1, len(people) + 1):
        for j in range(i + 1, len(people) + 1):
            edges.append((dists[i][j], i, j))
    edges = sorted(edges, reverse=True)
    clusters = []
    while edges and vsizes:
        _, u, v = edges.pop()
        if (uf.is_joined(u, v) or
            uf.is_joined(0, u) or
            uf.is_joined(0, v)):
            continue  # Used in a cluster already or would cause a loop
        uf.join(u, v)
        cluster = uf.get_cluster(u)
        if len(cluster) == vsizes[-1]:
            clusters.append([people[p - 1] for p in cluster])
            vsizes.pop()
            uf.join(0, u)
    unsaved = [people[p - 1] for p in range(1, len(people) + 1) if uf.is_alone(p)]
    return clusters, unsaved

def traveling_salesman(start, points):
    from random import shuffle
    shuffle(points)
    return [start] + points

def get_routes(start, people, vehicle_sizes):
    for vs in vehicle_sizes:
        if vs < 2:
            return None
    dist = get_dist_matrix([start] + people)
    sol = Solution()
    clusters, sol.unsaved = get_clusters(people, vehicle_sizes, dist)
    for clust in clusters:
        sol.routes.append(traveling_salesman(start, clust))
    return sol
