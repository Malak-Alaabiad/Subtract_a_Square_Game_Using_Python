import random   # Import a library to generate a random number of coins
import math     # Import a library to use square root built-in function
# Display welcome message and the game instructions to the user
welcome_message = '''
** Subtract a Square Game **
Hello! To play this game you must read the instructions'''
Instructions = ''' 
** Game Instructions **
1) This Game is played by two players with a pile of coins between them
2) The players take turns removing coins from the pile
3) you should always remove a non-zero square number of coins such as (1, 4, 9, 16,…)
4) The player who removes the last coin wins'''
print(welcome_message)

# Function to know what the user wants
def play_game():
    print("Please, Choose what do you want to do. \n1) Play \n2)Exit the game")
    global choice
    choice = input("Enter your choice from (1/2): ")
    return choice

# Function that explains how to play and get the users' inputs
def play(coins):
    num_list = []
    num = 1
    while num < math.sqrt(coins):
        num_list.append(num**2)
        num += 1
    for i in range(coins):
        print("Current number of coins: ", coins)
        while coins > 0:
            while True:
                try:
                    num1 = int(input("Player(1): Enter the a square number of coins you want to remove: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

            while num1 > coins or num1 <= 0 or coins - num1 < 0 or num1 not in num_list:
                try:
                    num1 = int(input("Invalid number of coins, Please enter a valid number you want to remove: "))
                except ValueError:
                    print("Invalid input. Please try again.")
            coins -= num1
            print("Number of remaining coins: ", coins)
           # check if player(1) is winner
            if coins == 0:
                print("Congratulations!!, Player(1) is the winner!!")
                play_game()
                main()

            else:
                while True:
                    try:
                        num2 = int(input("Player(2): Enter the number of coins you want to remove: "))
                        break
                    except ValueError:
                        print("Invalid input. Please try again.")
                        continue

                while num2 > coins or num2 <= 0 or coins - num2 < 0 or num2 not in num_list:
                    try:
                        num2 = int(input("Invalid number of coins, Please enter a valid number you want to remove: "))
                    except ValueError:
                        print("Invalid input. Please try again.")
                coins -= num2
                print("Number of remaining coins: ", coins)
                # check if player(2) is winner
                if coins == 0:
                    print("Congratulations!!, Player (2) is the winner!!")
                    play_game()
                    main()

# The main function
def main():
    coins = 0
    if choice == '1':
        print("1) Random number of coins \n2) Select a number of coins you want to play with ")
        option = input("Enter your choice from (1/2): ")
        if option == '1':
            # check if the number of coins is square
            while True:
                coins = random.randint(10, 1000)
                while math.sqrt(coins).is_integer():
                    coins = random.randint(10, 1000)
                play(coins)
        elif option == '2':
            while True:
                try:
                    coins = int(input("Enter the number of coins you want to play with: "))
                    break
                except ValueError:
                    print("Invalid input")
                    continue

            while coins <= 0 or coins == 1:
                try:
                    coins = int(input("Invalid number of coins, please enter a valid number: "))
                except ValueError:
                    print("Invalid input")
            # check if the number of coins is square
            while math.sqrt(coins).is_integer():
                try:
                    coins = int(input("Invalid number of coins, please enter a valid number: "))
                except ValueError:
                    print("Invalid input")

            play(coins)
        else:
            print("Invalid choice")
            main()
    # Exit the game
    elif choice == "2":
        print("Exiting Game...")
        exit()
    else:
        print("Invalid choice")
        play_game()
        main()

# Start the game
game_start = input("Press one to read the instructions or zero to exit the game (1/0): ")
if game_start == '1':
    print(Instructions)
    play_game()
    main()
elif game_start == '0':
    print("Exiting Game...")
    exit()
else:
    while True:
        game_start = input("Invalid choice, please try again: ")
        if game_start == '0':
            print("Exiting Game...")
            exit()
        elif game_start == '1':
            print(Instructions)
            play_game()
            main()
