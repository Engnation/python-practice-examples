import numpy as np

arr = np.array([[11,4],
                [3,5],
                [-3,4],
                [2,12],
                [4,5],
                [3,-1]])

x_max = 10
y_max = 10
x_min = 0
y_min = 0

u = arr[:,0]
v = arr[:,1]

print("u: ",u)
print("v: ",v)

clipped_u = np.clip(arr[:,0],x_min,x_max)
clipped_v = np.clip(arr[:,1],y_min,y_max)

arr[:,0] = clipped_u
arr[:,1] = clipped_v

print("clipped array: ",arr)