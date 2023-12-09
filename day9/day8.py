def get_input():
    with open("input.txt", "r", encoding="utf-8") as infile:
        return [[int(x) for x in line.strip().split(" ")] for line in infile]

def is_all_zero(lst):
    return all(map(lambda x: x == 0, lst))

def successive_difs(lst):
    return [lst[idx+1]-lst[idx] for idx, _ in enumerate(lst[:-1])]

def to_bottom(lst):
    if not lst or is_all_zero(lst):
        return 0
    return lst[-1] + to_bottom(successive_difs(lst))

if __name__ == "__main__":
    seqs = get_input()
    # part 1
    print(sum(to_bottom(seq) for seq in seqs))
    # part 2
    seqs = [list(reversed(seq)) for seq in seqs]
    print(sum(to_bottom(seq) for seq in seqs))
