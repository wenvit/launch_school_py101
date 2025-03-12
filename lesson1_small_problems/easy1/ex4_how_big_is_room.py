####### Problem statement

# Build a program that asks the user to enter the 
# length and width of a room, in meters, 
# then prints the room's area in both square meters and 
# square feet.

# Note: 1 square meter == 10.7639 square feet

######### PEDAC ##############

# inputs: length (m), width (m)
# outputs: area in m2, area in ft2

# rules
# user inputs room's length & width, both in meters
# assume valid room dimensions are entered (e.g., positive values > 0)
# room area is calculated in both m2 and ft2

# test cases
# length = 5 m, width = 3 m --> area = 15 m2 or 161.459 ft2
# length = 4 m, width = 4 m --> area = 16 m2 or 172.223 ft2

# data structure
# float

# algorithm
# 1. Ask user to input room length and width in meters; 
#    convert strings returned by `input` function 
#    to float data type and assign to variables 
#   `length_m` and `width_m` 
# 2. Assign variable `area_m2` to result of multiplying `length_m` x `width_m``, 
#    rounded to nearest tenth.
# 3. Assign variable `area_ft2` to result of multiplying `area_m2` x 10.7639 ft2/m2, 
#    rounded to nearest tenth.
# 4. Call `print` function with f-string as argument.
#    f-string interpolates variables `area_m2` and `area_ft2`

# code

# length_m = float(input('Please enter the length of the room in meters:  '))
# width_m = float(input('Please enter the width of the room in meters:  '))

# area_m2 = round(length_m * width_m, 1)
# area_ft2 = round(area_m2 * 10.7639, 1)

# print(f'The area of the room is {area_m2} m2, ' 
#       f'which is equivalent to {area_ft2} ft2.')

#### Launch School solution - instead of rounding, use format specification

# area_m2 = length_m * width_m
# area_ft2 = area_m2 * 10.7639

# print(f'The area of the room is {area_m2:.1f} m2, ' 
#        f'which is equivalent to {area_ft2:.1f} ft2.')

## Further exploration

# Modify the program to let the user specify the measurement type 
# (meters or feet). Compute the area accordingly and print it and 
# its conversion in parentheses.

# algorithm
# 1. Define function `room_area` that calculates the room's area.
#    The function accepts 2 parameters: `length`, `width`
#    and returns the result of `length` multiplied by `width`.
# 2. Ask user to input units of measure: meters or feet;
#    assign `uom` variable to this value.
# 3. Ask user to input length and width dimensions; 
#    convert to float type and assign to `length` and `width` variables.
# 4. Invoke `room_area` and pass `length` and `width` as arguments; 
#    assign return value to `area` variable.
# 5. Invoke `print` function with f-string that interpolates `area`.
# 6.  `if uom == meters` evaluates as truthy, invoke `print` function
#    with f-string that interpolates `area` multiplied by 10.739 
# 7. `else` invoke `print` function with f-string that interpolates 
#    `area` divided by 10.739  

def room_area(length, width):
    return length * width

uom = input('What units of measure are you using? '
            'Please enter meters or feet: ')
length = float(input(f'Please enter the length of the room in {uom}:  '))
width = float(input(f'Please enter the width of the room in {uom}:  '))

area = room_area(length, width)

print(f'The area of the room is {area:.1f} sq {uom} ') 

if uom == 'meters':
    print(f'({area * 10.7639:.1f} sq feet.)')
else:
    print(f'({area / 10.7639:.1f} sq meters).')