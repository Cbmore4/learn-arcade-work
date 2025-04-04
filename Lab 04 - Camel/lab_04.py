import random

def camel_game():
    print("Welcome to the Camel Game!")
    print("You have stolen a camel from a rich man and escape by making your way across the goo lagoon desert!")
    print("The rich mans guards want the camel back and are chasing you down! Survive your desert trek and outrun the guards!.\n")

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    drinks = 3

    while True:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop and rest.")
        print("E. Status check.")
        print("Q. Quit.")
        choice = input("Your choice? ").lower()

        if choice == 'q':
            print("You quit the game. No wait, COME BACKK!")
            break
        elif choice == 'a':
            if drinks > 0:
                drinks -= 1
                thirst = 0
                print("You take a drink. Gotta lova that H20!")
            else:
                print("BRROOOO You are out of water!")
        elif choice == 'b':
            miles = random.randint(5, 12)
            miles_traveled += miles
            thirst += 1
            camel_tiredness += 1
            natives_distance += random.randint(7, 14)
            print(f"You traveled {miles} miles.")
        elif choice == 'c':
            miles = random.randint(10, 20)
            miles_traveled += miles
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            natives_distance += random.randint(7, 14)
            print(f"You traveled {miles} miles.")
        elif choice == 'd':
            camel_tiredness = 0
            print("The camel is happy and chillin like a villain.")
            natives_distance += random.randint(7, 14)
        elif choice == 'e':
            print(f"Miles traveled: {miles_traveled}")
            print(f"Drinks in canteen: {drinks}")
            print(f"The guards are {miles_traveled - natives_distance} miles behind you.")

        # Game ending conditions
        if thirst > 6:
            print("You died of thirst! bruh drink more water dummy")
            break
        if camel_tiredness > 8:
            print("Your camel is dead. Like cmon")
            break
        if natives_distance >= miles_traveled:
            print("The guards caught you! NOOOO")
            break
        if miles_traveled >= 200:
            print("You made it across goo lagoon! You win!, Perfect!")
            break

camel_game()
