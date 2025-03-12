### Problem statement:

# Determine whether the following dictionary of people 
# and their age contains an entry for 'Spot':

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

### Solution:

print(ages.get('Spot', 'Key not found')) # one way
print('Spot' in ages) # simpler

