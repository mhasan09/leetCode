import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in range(1, 14):
                self.cards.append(Card(j, i))

    def show(self):
        for i in self.cards:
            i.show()

    def shuffle(self):
        for i in reversed(range(0, len(self.cards))):
            random_card = random.randint(0, i)
            self.cards[i], self.cards[random_card] = self.cards[random_card], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self,name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for i in self.hand:
            i.show()


deck = Deck()
deck.shuffle()
player = Player("Jamal")
player.draw(deck).draw(deck)
player.show_hand()