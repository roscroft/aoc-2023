import re
from functools import reduce

def compose(*func):
    def compose_(f, g):
        return lambda x : f(g(x))
    return reduce(compose_, func, lambda x : x)

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
        print(sum(compose(num, nums, exts)(line) for line in matches(infile, regex_search_1)))
    with open("input.txt", "r", encoding="utf-8") as infile:
        print(sum(compose(num, nums, exts)(line) for line in matches(infile, regex_search_2)))
