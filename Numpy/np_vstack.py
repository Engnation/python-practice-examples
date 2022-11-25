import numpy as np

arr_1_row_1 =     [1,2,3,4,5,6,7,8,9,10,11]
arr_1_row_2 =     [11,10,9,8,7,6,5,4,3,2,31]

np_arr_1_row_1 = np.array(arr_1_row_1)
np_arr_1_row_2 = np.array(arr_1_row_2)

#print("arr 1: ",arr_1)

A = np.zeros((2,11))

A[0] = np_arr_1_row_1
A[1] = np_arr_1_row_2
 
print("A :",A," and A shape: ",A.shape)

for i in range(10):

    A_inst = np.random.rand(2,11)

    print("A instance: ",A_inst, " and A instance shape: ",A_inst.shape)
    A = np.vstack((A,A_inst))
    
print("A final: ",A)


