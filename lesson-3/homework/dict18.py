# Create Default Dictionary: Create a dictionary that provides a default value for missing keys.

from collections import defaultdict

default_dict = defaultdict(lambda: "default value")
default_dict["a"] = 1
print(default_dict["b"])