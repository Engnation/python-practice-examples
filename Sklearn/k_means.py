from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
               [10, 2], [10, 4], [10, 0]])

X_data = np.genfromtxt('image_ 1_list_of_inner_circle_centers.csv', delimiter=',')

kmeans = KMeans(n_clusters=24, random_state=0).fit(X_data)

print("labels: ",kmeans.labels_)

print("predict: ",kmeans.predict([[0, 0], [12, 3]]))

print("centers: ",kmeans.cluster_centers_)
