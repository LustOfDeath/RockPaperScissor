import pickle
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

MENIU_CHOICES = """
[1] - Play
[2] - Statistics
[3] - Exit
"""

STATISTICS_CHOICES = """
[1] - This game results
[2] - All results
[3] - Exit
"""

player_score, computer_score, draw_score = 0, 0, 0
player_result, computer_result, draw_result = 0, 0, 0
pictures = [rock, paper, scissors]

while True:
    choice = input(MENIU_CHOICES)
    if choice == "1":
        try:
            with open("all_scores.pkl", "rb") as pickle_file:
                player_result = pickle.load(pickle_file)
                computer_result = pickle.load(pickle_file)
                draw_result = pickle.load(pickle_file)
        except FileNotFoundError:
            print("File was created\n")
            with open("all_scores.pkl", "wb") as pickle_file:
                score_container = player_result, computer_result, draw_result
                pickle.dumps(player_result)
                pickle.dumps(computer_result)
                pickle.dumps(draw_result)

        print('Welcome to "ROCK PAPER SCISSORS" game!\n')
        player_choice = int(input("Choose your symbol:\n[0] - Rock\n[1] - Paper\n[2] - Scissors\n"))
        computer_choice = random.randint(0, 2)

        if player_choice >= 3 or player_choice < 0:
            print("Check your input symbol and try again!")

        else:
            print("You chose:")
            print(pictures[player_choice])
            print("Computer chose:")
            print(pictures[computer_choice])

        if player_choice == 0 and computer_choice == 2:
            player_score += 1
            player_result += 1
            print("You won!")

        elif computer_choice == 0 and player_choice == 2:
            computer_score += 1
            computer_result += 1
            print("You lost!")

        elif computer_choice > player_choice:
            computer_score += 1
            computer_result += 1
            print("You lost!")

        elif player_choice > computer_choice:
            player_score += 1
            player_result += 1
            print("You won!")

        elif computer_choice == player_choice:
            draw_score += 1
            draw_result += 1
            print("It's a draw!")

        with open("all_scores.pkl", "wb") as pickle_file:
            score_container = player_result, computer_result, draw_result
            pickle.dump(player_result, pickle_file)
            pickle.dump(computer_result, pickle_file)
            pickle.dump(draw_result, pickle_file)

    elif choice == "2":

        while True:
            choice = input(STATISTICS_CHOICES)
            if choice == "1":
                print(f"This game results:\nWon: {player_score}\n"
                      f"Lost: {computer_score}\nDraw: {draw_score}")

            elif choice == "2":

                with open("all_scores.pkl", "rb") as pickle_file:
                    player_result = pickle.load(pickle_file)
                    computer_result = pickle.load(pickle_file)
                    draw_result = pickle.load(pickle_file)
                    print("Total victories:", player_result)
                    print("Total defeats:", computer_result)
                    print("Total draw:", draw_result)
                    games_total = (player_result + computer_result + draw_result)
                    victories_percentage = ((player_result / games_total) * 100)
                    print("Winning percentage: ", round(victories_percentage), "%")

                with open("all_scores.pkl", "wb") as pickle_file:
                    score_container = player_result, computer_result, draw_result
                    pickle.dump(player_result, pickle_file)
                    pickle.dump(computer_result, pickle_file)
                    pickle.dump(draw_result, pickle_file)

            elif choice == "3":
                break

    elif choice == "3":
        print("See you next time!")
        break
    else:
        print("Wrong choice")
