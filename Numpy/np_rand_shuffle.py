import numpy as np
#import random

points = np.array([[11,4],
                [3,5],
                [-3,4],
                [2,12],
                [4,5],
                [3,-1],
                [4,5],
                [6,7],
                [6,3],
                [9,2],
                [5,7],
                [6,2],
                [3,8],
                [2,4],
                [2,8]])

ratio = 0.4
pts_len = points.shape[0]
points_to_shuffle = pts_len*ratio
#print("points to shuffle: ",points_to_shuffle)
subset = points[0:int(points_to_shuffle)]
#rint("subset: ",subset)

np.random.shuffle(subset)

#print("shuffled portion of points: ",subset)

points[0:int(points_to_shuffle)] = subset

print("shuffled points: ",points)