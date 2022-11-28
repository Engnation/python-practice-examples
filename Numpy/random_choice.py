import numpy as np
import random

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

#print("lenght of points: ",points.shape)

random.randint(0, points.shape[0])

batch_size = 9

random_indexes = np.random.choice(points.shape[0], batch_size, replace=False)

#random_indexes = np.random.randint(points.shape[0],size=batch_size) # replaces but shouldn't

#made_up_rnd_inxs = [5,7,3,2]

made_up_rnd_inxs = random_indexes

subset = points[made_up_rnd_inxs,:]

print(subset)
