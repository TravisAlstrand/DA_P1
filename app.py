import random
import statistics


guess_list = []
guess_attempts = 0
high_score = 200


def welcome():
    print("""
    \n*******************************************
    \n*** Welcome to the Number Guessing Game ***
    \n*******************************************
    """)
    start_game()


def start_game():
    global guess_attempts
    global high_score
    guess_attempts = 0
    random_number = random.randint(1, 100)
    print(f"(( {random_number} ))")
    if high_score < 200:
        print(f"\nThe current high score is {high_score}")
    while True:
        player_guess = input("\nPlease guess a number between 1 & 100: ")
        try:
            guess_int = int(player_guess)
            if guess_int <= 0 or guess_int > 100:
                raise Exception("""
                    \n--- Your guess must be between 1 & 100. Try again! ---
                    \n*******************************************
                    """)
        except ValueError:
            print(f"""
            \n--- Your guess must be a whole number. Try again! ---
            \n*******************************************
            """)
            continue
        except Exception as e:
            print(f"\n{e}")
            continue
        else:
            if guess_int < random_number:
                print("""
                \nYour guess was too low. Attempts +1.
                \nTry again!
                \n*******************************************
                """)
                guess_attempts += 1
                continue
            elif guess_int > random_number:
                print("""
                \nYour guess was too high. Attempts +1.
                \nTry again!
                \n*******************************************
                """)
                guess_attempts += 1
                continue
            elif guess_int == random_number:
                guess_attempts += 1
                handle_endgame()
                break


def handle_endgame():
    global guess_attempts
    global high_score
    guess_list.append(guess_attempts)
    mean = get_mean(guess_list)
    median = get_median(guess_list)
    mode = get_mode(guess_list)
    print("\n*******************************************")
    if guess_attempts < high_score:
        high_score = guess_attempts
        print("\nWay to go! A new high score!!")
    else:
        print("\nWay to go! You guessed it!")
    print(f"It took you {guess_attempts} tries!")
    print(f"""
    \n*******************************************
    \n************ PLAYER STATS *****************
    \n*******************************************
    \nMean: {mean}
    \nMedian: {median}
    \nMode: {mode}
    """)
    while True:
        play_again = input("\nWould you like to play again? y / n: ")
        if play_again.lower() == "y":
            start_game()
            break
        elif play_again.lower() == "n":
            print("\nThanks for playing! See ya!")
            quit()
        else:
            print("\n--- Please enter a 'y' or an 'n' ---")
            continue


def get_mean(guesses):
    return statistics.mean(guesses)


def get_median(guesses):
    return statistics.median(guesses)


def get_mode(guesses):
    return statistics.mode(guesses)


if __name__ == "__main__":
    welcome()
