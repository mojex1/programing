def rps():
    while True: # new
        import random
        user_chose = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        bot_chose = random.choice(possible_actions)
        print(f"\nYou chose {user_chose}, computer chose {bot_chose}.\n")

        if user_chose == bot_chose:
            print(f"Both players selected {user_chose}. It's a tie!")
        elif user_chose == "rock":
            if bot_chose == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_chose == "paper":
            if bot_chose == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_chose == "scissors":
            if bot_chose == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
print(rps())