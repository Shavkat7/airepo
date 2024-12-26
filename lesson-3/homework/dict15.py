# Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.

keys = ["a", "b", "c"]
values = [1, 2, 3]
paired_dict = dict(zip(keys, values))
print(paired_dict)