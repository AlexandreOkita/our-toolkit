def flip_coin(return_string=False, option_a="heads", option_b="tails"):
    from random import randint
    r = randint(0,1)

    if option_a != "heads" or option_b != "tails":
        return_string = True

    if not return_string:
        if r == 0:
            return True
        return False

    if r == 0:
        return option_a
    return option_b
