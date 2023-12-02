import re
from functools import reduce

def compose(*func):
    def compose_(f, g):
        return lambda x : f(g(x))
    return reduce(compose_, func, lambda x : x)

MAX_ALLOWED = [12, 13, 14]

def parse(line):
    matches = re.findall(r'Game (\d+): (.*)', line)
    print(matches)
    game_id = matches[0][0]
    marbles = matches[0][1]
    marble_list = marbles.split("; ")

    rgb = [0,0,0]
    for draw in marble_list:
        amounts = draw.split(", ")
        for amount in amounts:
            number, color = amount.split(" ")
            number = int(number)
            if color == "red":
                rgb[0] = max(rgb[0], number)
            if color == "green":
                rgb[1] = max(rgb[1], number)
            if color == "blue":
                rgb[2] = max(rgb[2], number)

    if rgb[0] > MAX_ALLOWED[0] or rgb[1] > MAX_ALLOWED[1] or rgb[2] > MAX_ALLOWED[2]:
        return 0
    return int(game_id)

def parse2(line):
    matches = re.findall(r'Game (\d+): (.*)', line)
    game_id = matches[0][0]
    marbles = matches[0][1]
    marble_list = marbles.split("; ")

    rgb = [0,0,0]
    for draw in marble_list:
        amounts = draw.split(", ")
        for amount in amounts:
            number, color = amount.split(" ")
            number = int(number)
            if color == "red":
                rgb[0] = max(rgb[0], number)
            if color == "green":
                rgb[1] = max(rgb[1], number)
            if color == "blue":
                rgb[2] = max(rgb[2], number)

    return rgb[0]*rgb[1]*rgb[2]


def regex_search_1(line):
    return re.findall(r'\d', line)

def regex_search_2(line):
    return re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

def digit_dict(digit):
    return {"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}.get(digit, digit)

def matches(input_file, regex_search):
    return list(map(regex_search, input_file))

def exts(match):
    return [match[0], match[-1]]

def nums(digits):
    return map(digit_dict, digits)

def num(vals):
    return int("".join(vals))

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as infile:
        print(sum(parse(line) for line in infile))
    with open("input.txt", "r", encoding="utf-8") as infile:
        print(sum(parse2(line) for line in infile))
        
#    with open("input.txt", "r", encoding="utf-8") as infile:
#        print(sum(compose(num, nums, exts)(line) for line in matches(infile, regex_search_2)))
