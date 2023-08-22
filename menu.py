import keyboard
import agetesteg
import testedeidadept


def menu():
    print("1 for eg/2 para pt")
    key = keyboard.read_key()

    if key == "1":
        agetesteg.age_test()

    elif key == "2":
        testedeidadept.teste_idade()


if(__name__ == "__main__"):
    menu()