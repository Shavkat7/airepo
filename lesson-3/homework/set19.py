# Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged_set = set(list1).union(set(list2))
print(merged_set)