# P1
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
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    # P1
    def cmp(
        self, other
    ):  # Compares two cards (self and another), checks suits first as priority, returns 1 if self is ranked higher and -1 if the inverse is true
        if self.suit > other.suit:  # Check the suits
            return 1
        if self.suit < other.suit:
            return -1

        if self.rank > other.rank:
            if other.rank == 1:
                return -1  # other is Ace (and self is not)
            else:
                return 1
        if self.rank < other.rank:
            if self.rank == 1:
                return 1  # self is Ace (and other is not)
            else:
                return -1

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
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random

        rng = random.Random()
        rng.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break  # Break if out of cards
            card = self.pop()  # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = self.name + "'s Hand"
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        for hand in self.hands:
            print(hand)


# P2 - #P3
import turtle
import random


class TurtleGTX(turtle.Turtle):
    """inherit all the methods from the Turtle parent class"""

    def __init__(self, *args, **kwargs):
        super(TurtleGTX, self).__init__(*args, **kwargs)
        self.color("green")
        self.speed(2)
        print("Time for my GTX turtle!")
        self.mileage = 0
        self.breakdown = random.randrange(2000, 4000)

    def forward(self, x):
        """move forward by a specificed amount unless the total mileage has exceeded the breakdown mileage"""
        if self.mileage > self.breakdown:
            raise ValueError(
                "\nYour car has broken down! Change your tyres! \nbroke down at mile {}".format(
                    self.breakdown
                )
            )

        self.hideturtle()
        self.fd(x)
        self.showturtle()
        self.mileage += abs(x)

    def change_tyre(self):
        """reset mileage back to zero to simulate tyre change"""
        self.mileage = 0
