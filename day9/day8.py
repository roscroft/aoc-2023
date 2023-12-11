import operator
from functools import reduce

def get_input():
    with open("input.txt", "r", encoding="utf-8") as infile:
        return [[int(x) for x in line.strip().split(" ")] for line in infile]

def successive_difs(lst):
    return list(map(lambda x: x[1]-x[0], zip(lst, lst[1:])))

def to_bottom(lst):
    if all(map(lambda x: x == 0, lst)):
        return 0
    return lst[-1] + to_bottom(successive_difs(lst))

if __name__ == "__main__":
    seqs = get_input()
    # part 1
    print(sum(to_bottom(seq) for seq in seqs))
    # part 2
    print(sum(to_bottom(list(reversed(seq))) for seq in seqs))
