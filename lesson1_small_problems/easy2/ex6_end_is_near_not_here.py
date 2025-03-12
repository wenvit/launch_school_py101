##### Problem statement

# Write a function that returns the next to last word in the string argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two words.

############ PEDAC ###############

# inputs: input string of at least 2 words
# output: next to last word in string

# rules
# assume input string always contains at least 2 words
# words are any sequence of non-blank characters

# test cases
# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# data structure
# list returned by `split` method

# algorithm
# 1. Define function `penultimate` with a parameter of `words`
# 2. Within function, invoke `split` method on `words` and 
#    assign returned list to variable `words_list`
# 3. Return `words_list[-2]`

# def penultimate(words):
#     words_list = words.split()
#     return words_list[-2]

# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Further Exploration
# Our solution ignored two edge cases since we explicitly 
# stated that you didn't have to handle them: 
# strings that contain no words or just one word.

# Suppose we need a function that retrieves the middle
#  word of a phrase/sentence. What edge cases need 
# to be considered? How would you handle those edge 
# cases without ignoring them? Write a function that 
# returns the middle word of a phrase or sentence. 
# It should handle all of the edge cases you thought of.

# Edge cases
# To return the middle word, the phrase needs to be composed of
# at least 3 words. 
# It also needs to contain an odd number of words.

# algorithm
# 1. Define function `middle_word` with a parameter of `words`
# 2. Invoke `split` method on `words` and assign return value
#    to `words_list`
# 3. Use `len` function with `words_list` as argument, assign
#    return value to `words_count`
# 4. If `words_count < 3` or `words_count % 2 == 0`, 
#    return with error message
# 5. else return words_list[words_count // 2]

def middle_word(words):
    words_list = words.split()

    if len(words_list) < 3 or len(words_list) % 2 == 0:
        return ("Phrase must be at least 3 words long and "
                "be composed of an odd number of words.")
    return words_list[len(words_list) // 2]

print(middle_word('Hi'))
print(middle_word('Hey there'))
print(middle_word('What is up?')) # is
print(middle_word('What will happen when I enter a longer sentence?')) # I
