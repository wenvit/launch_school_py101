### Problem statement:

# Print the following string with the word important replaced by urgent:
advice = "Few things in life are as important as house training your pet dinosaur."

### Solution:

# one way using `replace` method

print(advice.replace('important', 'urgent'))

# another way using `split` and `join` methods

advice_split = advice.split('important')
print('urgent'.join(advice_split))