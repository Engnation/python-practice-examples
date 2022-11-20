a_b_threshold = 0.05

list_of_ellipses = [((1731.255126953125, 1040.44287109375), (183.77664184570312, 185.61965942382812), 30.424091339111328),
                         ((1731.2470703125, 1040.424072265625), (183.37071228027344, 185.1951141357422), 30.2407169342041),
                          ((1732.8038330078125, 1040.8201904296875), (79.78182983398438, 80.47626495361328), 18.944616317749023),
                           ((1732.7706298828125, 1040.835205078125), (79.3960952758789, 80.08189392089844), 19.5440616607666)]

diff_list = [1.843017578125, 1.82440185546875, 0.6944351196289062, 0.6857986450195312]

largest_axis_list = [185.61965942382812, 185.1951141357422, 80.47626495361328, 80.08189392089844]

pre_multiplied_largest_axis_list = [item * a_b_threshold for item in largest_axis_list]
print('pre multiplied largest axis list: ',pre_multiplied_largest_axis_list)

#a_b_ratio_filtered_ellipses = [x for x in list_of_ellipses if diff_list > a_b_threshold*largest_axis_list]
a_b_ratio_filtered_ellipses = [x for x in list_of_ellipses if y for y in diff_list > z for z in pre_multiplied_largest_axis_list]

print("a/b ratio filtered ellipses: ",a_b_ratio_filtered_ellipses)

