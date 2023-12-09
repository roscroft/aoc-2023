from functools import cmp_to_key

order_ = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3','2']
order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3','2','J', ]

def compare_hands(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    hand1_score, hand2_score = max_score(hand1), max_score(hand2)
    if hand1_score < hand2_score:
        return 1
    if hand2_score < hand1_score:
        return -1
    for card1, card2 in zip(hand1, hand2):
        if order.index(card1) < order.index(card2):
            return 1
        if order.index(card2) < order.index(card1):
            return -1
    return 0

def max_score(hand):
    if "J" not in hand:
        return score(hand)
    return min(score(hand.replace("J", card)) for card in order[:-1])

def score(hand):
    def score_check(length, count):
        return len(list(set(hand))) == length and any(hand.count(card) == count for card in hand)
    scores = {(1,5):0, (2,4):1, (2,3):2, (3,3):3, (3,2):4, (4,2):5, (5,1):6}
    return scores[next(filter(lambda x: score_check(*x), scores))]

def get_input():
    with open("input.txt", "r", encoding="utf-8") as infile:
        return [list(line.strip().split(" ")) for line in infile]

if __name__ == "__main__":
    print(sum(int(hand[1])*(idx+1) for idx, hand in enumerate(sorted(get_input(), key=cmp_to_key(compare_hands)))))
