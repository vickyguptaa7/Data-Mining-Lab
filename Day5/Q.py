import random

# We will use this list to store the dataset
DATASET = []

# Number of clusters
K = 3

# Number of Features
F = 2


# File Read
def GetDataPointsFromFile(filePath):
    file = open(filePath, 'r')
    for line in file:
        data_point = line.split()
        if (len(data_point) == 0):
            continue
        DATASET.append((float(data_point[1]), float(data_point[2])))


GetDataPointsFromFile("Dataset.txt")
print(DATASET)
# Number of points in the dataset
N = len(DATASET)

# Select K points as cluster center
points = []
for i in range(K):
    points.append([random.uniform(0, 10), random.uniform(0, 10)])

print("\n\n------------------------------------------- POINTS -------------------------------------------\n\n")
print(points)

# Find the Euclidean Distance and assign to the data point to the nearest cluster


def assignClusters(points):
    new_cluster = {}
    for d_indx in range(N):
        min_distance = 1e9
        cluster_index = 0
        for k_index in range(K):
            distance = 0
            # print(points[k_index])
            # for f_index in range(F):
            # print(points, k_index, f_index)
            distance += (DATASET[d_indx][0] -
                         points[k_index][0])**2+(DATASET[d_indx][1]-points[k_index][1])**2

            if (distance < min_distance):
                min_distance = distance
                cluster_index = k_index

        if new_cluster.get(cluster_index) == None:
            new_cluster[cluster_index] = []
        new_cluster[cluster_index].append(d_indx)

    return new_cluster


# # Find the means of the clusters and update the cluster center
def updateClusterCenter(clusters,points):
    new_points = []
    for cluster_index in range(K):
        # when there is no point in the cluster then we will not update the cluster center 
        if(clusters.get(cluster_index) == None):
            new_points.append(points[cluster_index])
            continue

        sum = [0]*F
        for d_indx in clusters[cluster_index]:
            for f_index in range(F):
                sum[f_index] += DATASET[d_indx][f_index]

        for f_index in range(F):
            sum[f_index] /= len(clusters[cluster_index])
            sum[f_index] = (sum[f_index])

        new_points.append(sum)

    return new_points


# print("\n\n------------------------------------------- RESULTS -------------------------------------------\n\n")
while (True):
    clusters = assignClusters(points)
    new_points = updateClusterCenter(clusters,points)
    if (new_points == points):
        for cluster_index in clusters:
            print("POINTS : ", new_points[cluster_index], "\n\n", "CLUSTER ",
                  cluster_index, " : ", clusters[cluster_index], "\n")
            for d_indx in clusters[cluster_index]:
                print(DATASET[d_indx],"\n")
        print("\n\n")
        break
    points = new_points

# print("\n\n")
