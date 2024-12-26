# Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
value_to_count = 1
occurrences = list(my_dict.values()).count(value_to_count)
print(occurrences)