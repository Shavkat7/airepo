# Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.

# generate random list
my_list = [2, 3, 4, 15, 6, 6, 32, 432, 2, 4, 15]

unique_elements = []
[unique_elements.append(x) for x in my_list if x not in unique_elements]
print(unique_elements)
