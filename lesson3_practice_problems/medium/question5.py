### Problem statement:

# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))


# Bonus question: How can you reliably test if a value is nan?

### Solution:

# This will print: False

import math
print(math.isnan(nan_value))