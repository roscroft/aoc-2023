from functools import cmp_to_key, reduce

def get_input():

    with open("input.txt", "r", encoding="utf-8") as infile:
        return [list(line.strip().split(" = ")) for line in infile]
    
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    route, empty, *rest = get_input()
    route = route[0]
    nodes = {}
    for res in rest:
        sides = res[1].split(", ")
        nodes[res[0]] = (sides[0][1:], sides[1][:-1])
    print(nodes)
    places = list(filter(lambda node: node[2] == "A", nodes))
    print(places)

    counters = []
    for place in places:
        counter = 0
        while place[2] != "Z":
            for step in route:
                counter += 1
                opts = nodes[place]
                if step == "L":
                    place = opts[0]
                elif step == "R":
                    place = opts[1]
                if place[2] == "Z":
                    counters.append(counter)
    print(reduce(lambda x,y: x*y, set(reduce(lambda x,y: x+y, [prime_factors(counter) for counter in counters]))))

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

def pay():
    for place in places:
        def is_done(places):
            zs = len(list(filter(lambda x: x[2] == "Z", places)))
            return len(places) == zs
                                    
        cnter = 0
        while not is_done(places):
            for step in route:
                cnter += 1
                opts = [nodes[place] for place in places]
                if step == "L":
                    places = [opt[0] for opt in opts]
                elif step == "R":
                    places = [opt[1] for opt in opts]
                if is_done(places):
                    print(cnter)


