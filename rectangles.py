from typing import List
import itertools


def check_if_rectangle(lines: List, multiple_coords: List[tuple]) -> bool:
    # COACHES' NOTE: This check could have been a function. 'is_valid' or 'has_surface'.
    if (multiple_coords[0][1] != multiple_coords[2][1] or
            multiple_coords[1][1] != multiple_coords[3][1] or
            multiple_coords[0][0] != multiple_coords[1][0] or
            multiple_coords[2][0] != multiple_coords[3][0]):
            return False
    # COACHES' NOTE: x and y make sense in this context, but I still don't exactly know what they mean. use better names.
    y = multiple_coords[0][0]
    x = multiple_coords[0][1] + 1
    # COACHES' NOTE: could have been a function.
    while x != multiple_coords[1][1]:
        if lines[y][x] == "-" or lines[y][x] == "+":
            x += 1
        else:
            return False
    y = multiple_coords[2][0]
    x = multiple_coords[2][1] + 1
    # COACHES' NOTE: could have been a function...the same one you would've made before.
    while x != multiple_coords[3][1]:
        if lines[y][x] == "-" or lines[y][x] == "+":
            x += 1
        else:
            return False
    y = multiple_coords[0][0] + 1
    x = multiple_coords[0][1]
    # COACHES' NOTE: Again, function.
    while y != multiple_coords[2][0]:
        if lines[y][x] == "|" or lines[y][x] == "+":
            y += 1
        else:
            return False
    y = multiple_coords[1][0] + 1
    x = multiple_coords[1][1]
    # COACHES' NOTE: Take a guess.
    while y != multiple_coords[3][0]:
        if lines[y][x] == "|" or lines[y][x] == "+":
            y += 1
        else:
            return False
    return True


def count(lines="") -> int:
    # COACHES' NOTE: Name could be a bit more explicit 'count_rectangles'.
    rectangles = 0
    if type(lines) != list:
        return rectangles
    
    # COACHES' NOTE: comment does what more properly named variables could have done. unpack what you have in those variables.
    lines_plus_coords = []  # tuples met (y,x)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "+":
                lines_plus_coords.append((y, x))
    save_combinations = [*itertools.combinations(lines_plus_coords, 4)]
    for x in save_combinations:
        if check_if_rectangle(lines, list(x)):
            rectangles += 1
    return rectangles

# COACHES' NOTE: repeated code with small variations, however small, can be a function. Helps a lot with readibility. Also, use more variables to show exactly what we're handling.
