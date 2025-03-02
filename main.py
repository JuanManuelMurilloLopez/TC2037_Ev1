from Infix_to_Postfix import shuntingYard


def main():

    # alphabet = input("Alphabet: ")
    alphabet = "abcd"

    # regEx = input("RegEx: ")
    regEx = "a+bc"

    print("Alphabet: ", alphabet)
    print("RegEx: ", regEx)
    print("Posfix: ", shuntingYard(regEx, alphabet))


main()
