import random

print("Welcome to - Guess The number")
player_1 = input("Player 1, enter your name\n")
player_2 = input("Player 2, enter your name\n")
try:
    a = int(input("First choose from where the number starts\n"))
    b = int(input("Second choose where the number ends\n"))
    number1 = random.randint(a,b)
    print("----------------------Let's being the game----------------------")
    print(f"{player_1}, its your turn")
    print(f"Guess the number between {a} and {b}")
    user1_input = 0
    player1_chances = 0
    while number1!=user1_input:
        user1_input = int(input())
        if user1_input == number1:
            player1_chances += 1
            print(f"You won the game in {player1_chances} chance/s")
            print("-----------------------------------------------------------")
            break
        if user1_input < number1:
            player1_chances += 1
            print("Guess a greater number")
            continue
        if user1_input > number1:
            player1_chances += 1
            print("Guess a smaller number")
            continue
    user2_input = 0
    player2_chances = 0
    number2 = random.randint(a,b)
    
    print(f"{player_2}, its your turn")
    print(f"Guess the number between {a} and {b}")
    while number2!=user2_input:
        user2_input = int(input())
        if user2_input == number2:
            player2_chances += 1
            print(f"You won the game in {player2_chances} chance/s")
            print("-----------------------------------------------------------")
            break
        if user2_input < number2:
            player2_chances += 1
            print("Guess a greater number")
            continue
        if user2_input > number2:
            player2_chances += 1
            print("Guess a smaller number")
            continue
    print("--------------------------WINNERS--------------------------")
    if player2_chances > player1_chances:
        print(f"{player_1} won the game. {player_1} guess the number in {player1_chances} chance/s")
    if player2_chances < player1_chances:
        print(f"{player_2} won the game. {player_2} guess the number in {player2_chances} chance/s")
    if player2_chances == player1_chances:
        print(f"DRAW")
        print(f"{player_1} guess the number in {player1_chances} chance/s and {player_2} guess the number in {player2_chances} chance/s")
except ValueError as e:
    print("Only enter numbers")
