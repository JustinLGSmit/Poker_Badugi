from deck import Deck


class Badugi:
    def __init__(self):

        self.deck = Deck()
        self.deck.shuffle_and_deal(4)
        self.deck.show_hand()

        if self.deck.is_flush() and self.deck.is_straight() and self.deck.high_card() == 14:
            print("Royal Flush!")

        elif self.deck.is_flush() and self.deck.is_straight():
            print("Straight Flush!")

        elif self.deck.is_four_of_kind():
            print("Four of a kind!")

        elif self.deck.is_full_house():
            print("Full House!")

        elif self.deck.is_flush():
            print("Flush!")

        elif self.deck.is_straight():
            print("Straight!")

        elif self.deck.is_three_of_kind():
            print("Three of a kind!")

        elif self.deck.is_two_pair():
            print("Two pairs!")

        elif self.deck.is_pair():
            print("Single Pair!")

        else:
            hc = self.deck.high_card()
            if hc < 11:
                print(f"High Card - {hc}")
            if hc == 11:
                print("High Card - Jack")
            if hc == 12:
                print("High Card - Queen")
            if hc == 13:
                print("High Card - King")
            if hc == 14:
                print("High Card - Ace")
