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
            scaled_dist = people[i - 1].scale_with_urgency(dists[i][j])
            scaled_dist = people[j - 1].scale_with_urgency(scaled_dist)
            edges.append((scaled_dist, i, j))
    edges = sorted(edges, reverse=True)
    clusters = []
    cluster = []
    while edges and vsizes:
        _, u, v = edges.pop()
        if (uf.is_joined(u, v) or
            uf.is_joined(0, u) or
            uf.is_joined(0, v)):
            continue  # Used in a cluster already or would cause a loop
        uf.join(u, v)
        cluster = uf.get_cluster(u)
        print(cluster)
        print(vsizes[-1])
        print(len(edges))
        if len(cluster) == vsizes[-1]:
            clusters.append(cluster[:])
            vsizes.pop()
            uf.join(0, u)

    if len(cluster) > 0:
        clusters.append(cluster[:])
        
    unsaved = [p for p in range(1, len(people) + 1) if uf.is_alone(p)]
    print("clusters:" + str(len(clusters)))
    return clusters, unsaved

def get_routes(start, people, vehicle_sizes):
    for vs in vehicle_sizes:
        if vs < 2:
            return None
    dist = dist_matrix.get_dist_matrix([start] + people)
    clusters, unsaved_ind = get_clusters(people, vehicle_sizes, dist)
    sol = Solution()
    sol.unsaved = [people[k - 1] for k in unsaved_ind]
    print(people)
    for clust_ind in clusters:
        print(3)
        print(clust_ind)
        cluster_points = [people[idx-1] for idx in clust_ind]
        route = traveling_salesman.tsp_osrm(0, cluster_points, dist, start)
        sol.routes.append(route)
    return sol
