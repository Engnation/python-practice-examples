from list_data import my_list
import numpy as np


my_list.sort()

sorted = np.array(my_list)

np.savetxt("sorted_list.csv", sorted, delimiter=",")

