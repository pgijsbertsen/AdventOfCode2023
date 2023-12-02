import re


# Read input
input = open("inputs/input.txt", "r")

max_cubes = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
    }

def puzzle1():
    idsum = 0
    for line in input:
        game = line.split(":")
        gamenum = int(game[0].split()[1])
        draws = game[1].split(";")
        for draw in draws:
            cubes = draw.split(",")
            for cube in cubes:
                if int(cube.split()[0]) > max_cubes[cube.split()[1]]:
                    break
            else:
                continue
            break
        else:
            idsum += gamenum
    return(idsum)

result = puzzle1()
print('Result: ', result)