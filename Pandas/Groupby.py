import pandas as pd
import numpy as np
from list_data import centers

center_indexes = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 
                3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
                6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9,
                9, 9, 9, 10, 10, 10, 10, 11, 11,
                11, 12, 12, 12, 13, 13, 13, 14,
                14, 14, 14, 15, 15, 15, 15, 16,
                16, 16, 17, 17, 17, 17, 18, 18,
                18, 19, 19, 19, 20, 20, 20, 20,
                21, 21, 21, 21, 22, 22, 22, 22,
                23, 23, 23, 23]

print(len(centers))


np_centers = np.array(centers)

#print(np_centers[:,0])

data = pd.DataFrame({"center_indexes":center_indexes,"centers_x":np_centers[:,0],"centers_y":np_centers[:,1]})

print("data: ",data)

means = data.groupby("center_indexes").mean()

print(means)
