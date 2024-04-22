from random import choice, seed


def flip_coin():
    # Change this line
    session_id = "c7e5368ce58677491cc63b520fa18ea7"
    # Change this line
    for round in range(1,13):
        seed(str(round) + "_" + session_id)

        print(choice(["tails", "heads"]))

flip_coin()
