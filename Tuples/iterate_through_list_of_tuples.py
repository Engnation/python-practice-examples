list_of_tuples = [((20,33),(33,42),12),((22,23),(33,43),11),((25,28),(27,29),13),((21,30),(32,39),14)]

max_cutoff = 12.5
min_cutoff = 11.5

new_list_of_tuples = [x for x in list_of_tuples if x[2] > min_cutoff and x[2] < max_cutoff]

print("new list of tuples: ",new_list_of_tuples) 