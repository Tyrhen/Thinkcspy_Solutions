"""Chapter 22 Exercise from Think Like a Computer Scientist"""
from unit_tester import test


class Card:
    ranks = [
        "Narf",
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} of {1}".format(self.ranks[self.rank], self.suits[self.suit])

    # P1
    def cmp(self, other):
        trumph_rank = 1
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank and other.rank != trumph_rank:
            return 1
        if self.rank > other.rank and other.rank == trumph_rank:
            return -1
        if self.rank < other.rank and self.rank != trumph_rank:
            return -1
        if self.rank < other.rank and self.rank == trumph_rank:
            return 1

        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __lt__(self, other):
        return self.cmp(other) == -1

    def __ge__(self, other):
        return self.cmp(other) <= 0

    def __gt__(self, other):
        return self.cmp(other) == 1

    def __ne__(self, other):
        return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"

        return s


def test_suite():
    ace = Card(3, 1)
    king = Card(3, 13)
    test((ace > king) == True)


test_suite()