# Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = {k: v for k, v in my_dict.items() if v > 2}
print(filtered_dict)