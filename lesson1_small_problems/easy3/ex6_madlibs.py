######## Problem statement

# Madlibs is a simple game where you create a story template 
# with "blanks" for words. You, or another player, then 
# construct a list of words and place them into the story, 
# creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun,
# a verb, an adverb, and an adjective, and injects them 
# into a story that you create.

########## PEDAC ############

# inputs: user inputs noun, verb, adverb, adjective
# outputs: madlib story

# test case
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly

# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

# data structure
# dictionary

# algorithm
# 1. Use `dict` constructor function to create empty dictionary object
#    and assign to variable `madlib`
# 2. Use `input` function to ask user to enter a noun, verb, adjective, 
#    and adverb, using each of these descriptors as key names in `madlib`
#    with user inputs as values assigned to those keys
# 3. Use `print` function with f-string argument to interpolate the values
#    associated with `madlib` keys

# code

madlib = {}

madlib['noun'] = input('Enter a noun: ')
madlib['verb'] = input('Enter a verb: ')
madlib['adjective'] = input('Enter an adjective: ')
madlib['adverb'] = input('Enter an adverb: ')

print(f"Do you {madlib['verb']} your {madlib['adjective']} " 
      f"{madlib['noun']} {madlib['adverb']}? That's hilarious!")
print(f"The {madlib['adjective']} {madlib['noun']} {madlib['verb']}s " 
      f"{madlib['adverb']} over the lazy dog.")
print(f"The {madlib['noun']} {madlib['adverb']} "
      f"{madlib['verb']}s up to Joe's {madlib['adjective']} turtle.")