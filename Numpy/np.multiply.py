import numpy as np

M1 = np.array([[-0.4583,	0.2947,	0.0139,	-0.004],
        [0.0509,	0.0546,	0.541,	0.0524],
        [-0.109,	-0.1784,	0.0443,	-0.5968]])

X = np.array([[1.2323],[1.4421],[0.4506],[1]])

#x = np.multiply(X.T,M1)
x = np.dot(M1,X)

print("x: ",x)



