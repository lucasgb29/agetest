import keyboard
import os
import time


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def enter_age():
    your_age = input("Your age: ")
    their_age = input("Their age: ")
    return your_age, their_age


def convert_age(your_age, their_age):
    int_your_age = int(your_age)
    int_their_age = int(their_age)
    return int_your_age, int_their_age


def check_minimum_age(your_age, their_age):
    int_your_age = int(your_age)
    int_their_age = int(their_age)
    if int_your_age < 14:
        print("You are too young to date, go be a child!!!")
        return False
    elif int_their_age < 14:
        print("They are too young to date, find someone your age.")
        return False
    else:
        return True


def check_age_range(int_your_age, int_their_age):
    min_age = (int_your_age / 2) + 7
    max_age = (int_your_age - 7) * 2
    too_young = int_their_age < min_age
    too_old = int_their_age > max_age
    return too_young, too_old


def calculate_adjustment(too_young, too_old, int_your_age, int_their_age):
    adjustment = 0
    while too_young or too_old:
        int_your_age += 1
        int_their_age += 1
        adjustment += 1
        too_young, too_old = check_age_range(int_your_age, int_their_age)
    return adjustment


def display_result(too_young, too_old, adjustment):
    if too_young:
        print("They are considered too young for you.")
        print("You will be in the right age in {} years".format(adjustment))
    elif too_old:
        print("They are considered too old for you.")
        print("You will be in the right age in {} years".format(adjustment))
    else:
        print("They are considered in the right age for you.")


def options():
    print("\nPress R to restart")
    print("Press Q to quit")

    while True:
        key = keyboard.read_key().upper()
        if key == "Q":
            print("\nGoodbye!!")
            return "Q"
        elif key == "R":
            return "R"


def invalid_age():
    clear_screen()
    print("############")
    print("Invalid age.")
    print("############")
    time.sleep(1)  
    return enter_age()


def age_test():
    while True:
        clear_screen()

        your_age, their_age = enter_age()

        if your_age.isdigit() and their_age.isdigit():
            if check_minimum_age(your_age, their_age):
                int_your_age, int_their_age = convert_age(your_age, their_age)

                too_young, too_old = check_age_range(int_your_age, int_their_age)

                adjustment = calculate_adjustment(too_young, too_old, int_your_age, int_their_age)

                display_result(too_young, too_old, adjustment)

        else:
            your_age, their_age = invalid_age()

        key = options()
        if key == "Q":
            break


if __name__ == "__main__":
    age_test()
