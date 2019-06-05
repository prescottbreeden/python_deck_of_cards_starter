from Deck import Deck

if __name__ == "__main__":
    print("1: bob")
    print("2: trash panda")
    print("3: chuck norris")
    print("4: van dam")
    choice = input("enter a number from 1 - 4")
    print('your answer was: ' + choice)
    if choice == '3':
        print("go slam a revolving door")

    # bob = Deck()
    # bob.build_deck()
    # bob.shuffle()
    # bob.print_deck()