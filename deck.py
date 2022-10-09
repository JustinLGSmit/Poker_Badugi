from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.hand = []

        names = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("S", "C", "H", "D")

        # Test hand to check hand rank methods
        # card1 = Card("A", "D")
        # card2 = Card("K", "D")
        # card3 = Card("Q", "D")
        # card4 = Card("J", "D")
        # card5 = Card("10", "D")
        # self.hand = [card1, card2, card3, card4, card5]

        # Create deck of cards
        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)
                # card.print_card()

    def shuffle_and_deal(self, card_count):
        # Randomize deck and add cards to hand
        print("Shuffling...Shuffling...Shuffling...")
        random.shuffle(self.cards)
        for _ in range(card_count):
            self.hand.append(self.cards.pop())

    def show_hand(self):
        # print contents of hand to the console
        print("Your hand: ", end="")
        for card in self.hand:
            card.print_card()
        print()
        print("You have: ", end="")

    def hand_distribution(self):
        # create card distribution of whole deck
        dist = {i: 0 for i in range(1, 15)}
        for card in self.hand:
            dist[card.value_of_card()] += 1
            dist[1] = dist[14]

        # print card distribution to console
        # for d in dist:
        #     print(f"{d} : {dist[d]}")

        return dist

    def is_four_of_kind(self):
        dist = self.hand_distribution()
        for d in dist:
            if dist[d] == 4:
                return True
        return False

    def is_full_house(self):
        dist = self.hand_distribution()
        pair = False
        three_of_kind = False
        for d in dist:
            if dist[d] == 2:
                pair = True
            if dist[d] == 3:
                three_of_kind = True
        if pair and three_of_kind:
            return True
        return False

    def is_flush(self):
        num_suit = 0
        test_card = self.hand[0]
        for card in self.hand:
            if card.suit == test_card.suit:
                num_suit += 1
        if num_suit == 5:
            return True
        return False

    def is_straight(self):
        dist = self.hand_distribution()
        counter = 0
        for d in dist:
            if dist[d] == 0:
                counter = 0
            if dist[d] == 1:
                counter += 1
            if counter == 5:
                return True
        return False

    def is_three_of_kind(self):
        dist = self.hand_distribution()
        for d in dist:
            if dist[d] == 3:
                return True
        return False

    def is_two_pair(self):
        dist = self.hand_distribution()
        pairs = []
        for d in dist:
            if d > 1 and dist[d] == 2 and d not in pairs:
                pairs.append(d)
        if len(pairs) == 2:
            return True
        return False

    def is_pair(self):
        dist = self.hand_distribution()
        for d in dist:
            if dist[d] == 2:
                return True
        return False

    def high_card(self):
        high_card = 0
        dist = self.hand_distribution()
        for d in dist:
            if dist[d] > 0:
                high_card = d
        return high_card

