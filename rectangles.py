from typing import List
import itertools


def check_if_rectangle(lines: List, multiple_coords: List[tuple]) -> bool:
    if (multiple_coords[0][1] != multiple_coords[2][1] or
            multiple_coords[1][1] != multiple_coords[3][1] or
            multiple_coords[0][0] != multiple_coords[1][0] or
            multiple_coords[2][0] != multiple_coords[3][0]):
            return False
    y = multiple_coords[0][0]
    x = multiple_coords[0][1] + 1
    while x != multiple_coords[1][1]:
        if lines[y][x] == "-" or lines[y][x] == "+":
            x += 1
        else:
            return False
    y = multiple_coords[2][0]
    x = multiple_coords[2][1] + 1
    while x != multiple_coords[3][1]:
        if lines[y][x] == "-" or lines[y][x] == "+":
            x += 1
        else:
            return False
    y = multiple_coords[0][0] + 1
    x = multiple_coords[0][1]
    while y != multiple_coords[2][0]:
        if lines[y][x] == "|" or lines[y][x] == "+":
            y += 1
        else:
            return False
    y = multiple_coords[1][0] + 1
    x = multiple_coords[1][1]
    while y != multiple_coords[3][0]:
        if lines[y][x] == "|" or lines[y][x] == "+":
            y += 1
        else:
            return False
    return True


def count(lines="") -> int:
    rectangles = 0
    if type(lines) != list:
        return rectangles

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
