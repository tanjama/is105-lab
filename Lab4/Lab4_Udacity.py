# We import functions so that we can use them even though they are defined elsewhere (standard module)
import random 
import math
import itertools
from collections import defaultdict

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    #This code will Return the top hands (winning hands). It also uses the allmax function which is defined under
    print hands
    print "Winner:"
    return allmax(hands, key = hand_rank)

def allmax(iterable, key=lambda x:x):
    "Return a list of all items equal to the max of the iterable."
    #Iterable is an object that has an __iter__ method which returns an iterator.
    #Iteration is the process of taking one element at a time in a row of elements.
    maxi = max(iterable, key=key)
    #It is a for-loop in the element to get the result.
    return [element for element in iterable if key(element) == key(maxi)]

def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    # Count is the count of each rank.
    # Ranks lists corresponding ranks.
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    # The var group has a list that has all the values in the game.
    # Then it counts the ranks of the groups.
    # The if ranks sentences also makes sure that the problem with the ace in a straight is solved as it
    # can both be a 1 and a 14.
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r, s in hand])) == 1
    return (
        9 if (5, ) == counts else
        8 if straight and flush else
        7 if (4, 1) == counts else
        6 if (3, 2) == counts else
        5 if flush else
        4 if straight else
        3 if (3, 1, 1) == counts else
        2 if (2, 2, 1) == counts else
        1 if (2, 1, 1, 1) == counts else
        0), ranks

def group(items):
    # The list is Count, it will return the highest count first (x)
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

def unzip(pairs):
    # It packs up a list
    return zip(*pairs)

def card_ranks(hand):
    # Returns a list of the ranks, sorted with higher first
    # It also have a sort function incase if the ace problem i mentioned earlier
    ranks = [14 if r == 'A' else
             13 if r == 'K' else
             12 if r == 'Q' else
             11 if r == 'J' else
             10 if r == 'T' else
             int(r)
             for r, s in hand]
    ranks.sort(reverse = True)
    return ranks if ranks != [14, 5, 4, 3, 2] else [5, 4, 3, 2, 1]

def straight_udacity(ranks):
    # Return True if the ordered ranks form a 5-card straight.
    # The sum of the ranks. 
    # the smallest ranks * 5.
    # the value is 5 diffrent cards then True.
    # Example: we have the hand [5, 4, 3, 2, 1] which gives the value 15 - 1*5 = 10,
    # so 10 = 10 and it will retur  true
    return sum(ranks) - min(ranks)*5 == 10
    
def straight(ranks):
	# This is our own code this is to check the time difference between our code and udacitys
	# Checks if we have a straight, a straight can only be if all the cards in the hand
	# Have eather +1 or -1 in rank (value) to the other card in front of it.
	return sorted(ranks, reverse=True)==ranks and len(set(ranks))==len(ranks)

def flush(hand):
	# This is our own code this is to check the time difference between our code and udacitys
	# Checks if we have a flush, flush means that all the card in the hand have the same
	# Colour, which is what this code does. Also have a look on udacitys code.
	return [ e[1] for e in hand] == [hand[1][1] for e in range (len(hand))]

def flush_udacity(hand):
    # It will return True if all the cards have the same suit.
    # Set is doing like we have only uniqe values.
    # If len is longer than 1, then the value is set to false.
    # For is doing like we only have the symbol.
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    # If we have two pair, return the two ranks as a
    # tuple: (highest, lowest); otherwise it should return none
    # For-loop the ranks
    # Set is to find 2 types of symbol
    # If length is longer than 2, then the value is not true
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(result) == 2:
        return (max(result), min(result))

def kind(n, ranks):
    # Return the first rank that this hand has exactly n of
    # Return None if there is no n-of-a-kind in the hand
    # Here is the value of all the cards in decks
    # We want to loop in the symbols
    # That means SHDC
    for r in set(ranks):
        if ranks.count(r) == n:
            return r
    return None
  
deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']


# This gives five cards to the players.
# It is one of the cards in the deck.
# Random shuffels the deck.
# A iter is itering the deck.
# returns a list containing the decks that i simliar to the hands. 
def deal(numhands, n = 5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Return a list of numhands hands consisting of n cards each"
    random.shuffle(deck)
    deck = iter(deck)
    return [[next(deck) for card in range(n)] for hand in range(numhands)]


def test():
    "Test cases for the functions in the poker-program."
    # Making different kinds of variabels so that you have something to test.
    # Making many diffent kinds of variabels so we can use them.
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
    s3 = "TC JC QC KS AS".split() # 10-A straight    
    tp = "5S 5D 9H 9C 6S".split() # two pair
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([s1, s2]) == [s2]
    assert poker([s1, tp]) == [s1]
    
    # Python's assert statement helps you find bugs more quickly.
    # Python's assert statement helps you to solve problems with less pain.
    # assert hand_rank(sf) == (8, 10)
    # assert hand_rank(fk) == (7, 9, 7)
    # assert hand_rank(fh) == (6, 10, 7)
    # assert hand_rank(s1) == (4, 5)
    # assert hand_rank(s3) == (4, 14)    

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]

    # Ace-high beats 7-high:
    assert (card_ranks(['AS', '2C', '3D', '4H', '6S']) >
            card_ranks(['2D', '3S', '4C', '6H', '7D']))
    # 5-straight loses to 6-straight:
    assert (card_ranks(['AS', '2C', '3D', '4H', '5S']) <
            card_ranks(['2D', '3S', '4C', '5H', '6D']))

    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(tpranks) == (9, 5)
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)    

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    return 'tests pass'
    
# The names of the plays you can make in poker 
# using a List to contain the hand names
hand_names = [
    'High Card',
    'Pair',
    '2 Pair',
    '3 Kind',
    'Straight',
    'Flush',
    'Full House',
    '4 Kind',
    'Straight Flush',
    ]
    
# This prints the chance to win.
# It gives out 700 000 hands.
# Counts how many that are playing. 
def hand_percentages(n = 700*1000):
    "Sample n random hands and print a table of percentages for each type of hand"
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %6.3f'%(hand_names[i], 100.*counts[i]/n))

def all_hand_percentages():
    "Print an exhaustive table of frequencies for each type of hand"
    counts = [0]*9
    n = 0
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    for hand in itertools.combinations(deck, 5):
        n += 1
        ranking = hand_rank(hand)[0]
        counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %7d %6.3f'%(hand_names[i], counts[i], 100.*counts[i]/n))

def shuffle1(deck):
    # O(N**2)
    # Incorrect distribution
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2(deck):
    # O(N**2)
    # Incorrect distribution?    
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2a(deck):
    # http://forums.udacity.com/cs212-april2012/questions/3462/better-implementation-of-shuffle2
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        j = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle3(deck):
    # O(N)
    # Incorrect distribution    
    N = len(deck)
    for i in range(N):
        j = random.randrange(N)
        deck[i], deck[j] = deck[j], deck[i]

def shuffle(deck):
    # Knuth method
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i]        

def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1./factorial(len(deck))  ## expected count
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** bad ***'))
    print '    ',
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" % (item, count*100./n),
    print

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc','ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)

if __name__ == '__main__':
	# Find out if our code is faster then udacitys code. Our was faster in one point while
	# udacitys code was faster then the other.
	import timeit
	print(timeit.timeit("straight([9, 8, 7, 6, 5])", setup="from __main__ import straight"))
	print(timeit.timeit("straight_udacity([9, 8, 7, 6, 5])", setup="from __main__ import straight_udacity"))
	print(timeit.timeit("flush('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush"))
	print(timeit.timeit("flush_udactiy('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush_udactiy"))

# The ammount of hands we want to deal out, aka the ammount of players
print poker(deal(4))
