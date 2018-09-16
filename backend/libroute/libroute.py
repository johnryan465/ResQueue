from util import Point, Solution
try:
    import union_find
    import traveling_salesman
    import dist_matrix
except ImportError:
    from libroute import union_find
    from libroute import traveling_salesman
    from libroute import dist_matrix

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
            clusters.append(cluster[:])
            vsizes.pop()
            uf.join(0, u)
    unsaved = [p for p in range(1, len(people) + 1) if uf.is_alone(p)]
    return clusters, unsaved

def get_routes(start, people, vehicle_sizes):
    for vs in vehicle_sizes:
        if vs < 2:
            return None
    dist = dist_matrix.get_dist_matrix([start] + people)
    clusters, unsaved_ind = get_clusters(people, vehicle_sizes, dist)
    sol = Solution()
    sol.unsaved = [people[k - 1] for k in unsaved_ind]
    for clust_ind in clusters:
        route = traveling_salesman.traveling_salesman(0, clust_ind, dist)
        sol.routes.append([start] + [people[k - 1] for k in route[1:]])
    return sol

