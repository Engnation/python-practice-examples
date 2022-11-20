list_of_tuples = [((20,33),(33,42),1),((22,23),(33,43),2),((25,28),(27,29),3),((21,30),(32,39),4)]

print(list_of_tuples[0][2])
print(list_of_tuples[1][2])
print(list_of_tuples[2][2])
print(list_of_tuples[3][2])

desired_elements = [x[2] for x in list_of_tuples]

print(desired_elements)