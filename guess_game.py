from random import randint


def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input("What number did you guess(0 - 100)"))
        if user_guess == random_int:
            print(f"you found the number ({random_int}). Congrats")
            break

        elif user_guess < random_int:
            print(f"Your number is less than the number you guessed.")
        else:
            print(f"Your number is more than the number you guessed.")


if __name__ == "__main__":
    play()
