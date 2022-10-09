from poker import Poker
from badugi import Badugi

game_is_on = True
game_choice = 0

while game_is_on:
    print("Choose one of the following. Enter 1 or 2 (3 to quit)")
    game_choice = input("1. Poker  2. Badugi ")
    if game_choice == "1":
        print()
        poker = Poker()
    elif game_choice == "2":
        print()
        badugi = Badugi()
    elif game_choice == "3":
        print("Good bye")
        game_is_on = False
    else:
        print("Invalid selection")
    print()




