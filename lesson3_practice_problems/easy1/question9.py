### Problem statement

# Print a new version of the sentence given by advice 
# that ends just before the word house. 
# Don't worry about spaces or punctuation: 
# remove everything starting from the beginning of house 
# to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."

# Expected output:
# Few things in life are as important as

### Solution:

# `find` method returns index of first instance of beginning of 
#     substring 'house'
# use slice operation to get substring of advice starting at index 0 
#    up to but not including index where 'house' begins

# stop = advice.find('house')
# print(repr(advice[:stop]))

# Launch School solution using `split` method

print(advice.split('house')[0])