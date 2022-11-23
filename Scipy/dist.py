from scipy.spatial import distance
import numpy as np

centers =  np.array([[0,0],
                    [0,1],	
                    [0,2],	
                    [1,0],	
                    [1,1],
                    [1,2]])

dist_map = np.zeros([len(centers),len(centers)])
i = 0
for center in centers:
    print("center: ",center)
    c = np.array([center])
    distances = distance.cdist(c,centers,metric='euclidean')
    print("distances: ",i," ",distances)
    print("shape of distances: ",distances.shape)
    dist_map[i] = distances
    #np.savetxt("distance_" + str(i) + "_.csv", distances, delimiter=",")
    i = i + 1
np.savetxt("distance_map.csv",dist_map , delimiter=",")
print("shape of array: ",centers.shape)

'''
dist_map = np.zeros([len(centers),len(centers)])
    #print("centers: ",centers)
    print("dist map shape: ",dist_map.shape)
    i = 0
    for center in centers:
        
        c = np.array([center])
        #print("center: ",c, "shape: ",c.shape)
        distances = distance.cdist(c,centers,metric='euclidean')
        print('distances shape: ',distances.shape)
        dist_map[i] = distances
        np.savetxt("distance_map.csv",dist_map , delimiter=",")
        i+=1
'''