### Problem statement:

# Starting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and " 
# prepended to the front of the string referenced by famous_words.

prefix = 'Four score and'

### Solution:

print(prefix + ' ' + famous_words)
print(prefix, famous_words)
print(f'{prefix} {famous_words}')
