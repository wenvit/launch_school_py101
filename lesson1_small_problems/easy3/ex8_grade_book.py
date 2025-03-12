###### Problem statement

# Write a function that determines the mean (average) 
# of the three scores passed to it, and returns the 
# letter associated with that grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

############# PEDAC ###############

# inputs: 3 scores (numbers)
# outputs: average score and associated letter grade

# rules
# Tested values are all between 0 and 100. 
# There is no need to check for negative values or values greater than 100.

# test cases 
# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# algorithm

# 1. Define `get_grade` function with 3 parameters: 
#    `score1`, `score2`, `score3` (numbers)
# 2. Calculate average of 3 scores and assign to variable
#    `avg_score`
# 3. Use `if/elif/else` conditionals to determine letter grade
#    associated with average score

def get_grade(score1, score2, score3):
    avg_score = (score1 + score2 + score3) / 3
    print(avg_score)

    if avg_score >= 90: 
        return 'A'
    elif avg_score >= 80:
        return 'B'
    elif avg_score >= 70:
        return 'C'
    elif avg_score >= 60:
        return 'D'
    return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
