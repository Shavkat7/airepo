# Generate Random Set: Create a set with a specified number of random integers within a certain range.

import random

random_set = set(random.randint(1, 100) for _ in range(10))
print(random_set)