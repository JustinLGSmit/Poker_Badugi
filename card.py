class Card:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.suit_symbols = {"S": "♠️", "C": "♣️", "H": "♥️", "D": "♦️"}

    # Return value of card
    def value_of_card(self):
        if self.name == "A":
            return int(14)
        if self.name == "K":
            return int(13)
        if self.name == "Q":
            return int(12)
        if self.name == "J":
            return int(11)
        return int(self.name)

    # Return suit of card
    def suit_of_card(self):
        return self.suit

    # Print card to console
    def print_card(self):
        print(f"{self.name}{self.suit_symbols[self.suit]} ", end="")
