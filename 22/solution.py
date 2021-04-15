with open('input.txt', 'r') as f:
    data = f.read()

def count_score(deck):
    return sum(x*y for x,y in zip(reversed(deck), range(1,len(deck)+1)))

def parse_input(data):
    p1_raw, p2_raw = data.split('\n\n')
    p1_deck = [int(x) for x in p1_raw.splitlines()[1:]]
    p2_deck = [int(x) for x in p2_raw.splitlines()[1:]]
    return p1_deck, p2_deck


p1_deck, p2_deck = parse_input(data)
while p1_deck and p2_deck:
    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)
    if p1_card > p2_card:
        p1_deck += [p1_card, p2_card]
    else:
        p2_deck += [p2_card, p1_card]

winning_deck = p1_deck or p2_deck
print("Part 1:", count_score(winning_deck))


def play_game(d1, d2):
    configurations = set()
    configurations.add((tuple(d1),tuple(d2)))
    while d1 and d2:
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if (tuple(d1),tuple(d2)) in configurations:
            return "d1", d1

        configurations.add((tuple(d1),tuple(d2)))
        if c1 <= len(d1) and c2 <= len(d2):
            winner, deck = play_game(d1[:c1].copy(), d2[:c2].copy())
            if winner == "d1":
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]
        else:
            if c1 > c2:
                d1 += [c1, c2]
            else:
                d2 += [c2, c1]
    
    return ("d1",d1) if d1 else ("d2",d2)

p1_deck, p2_deck = parse_input(data)
_, winning_deck_2 = play_game(p1_deck, p2_deck)

print("Part 2:", count_score(winning_deck_2))