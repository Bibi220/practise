#Password Generator Project
import random



def pwgen(nr_letters: int, nr_numbers: int, nr_symbols: int):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    for a in range(nr_letters):
        letters_index = random.randint(0, len(letters) - 1)
        password += letters[letters_index]

    for b in range(nr_symbols):
        symbols_index = random.randint(0, len(symbols) - 1)
        password += symbols[symbols_index]

    for c in range(nr_numbers):
        numbers_index = random.randint(0, len(numbers) - 1)
        password += numbers[numbers_index]
    pw_random = list(password)
    random.shuffle(pw_random)
    new_pw = ''.join(pw_random)
    return new_pw



if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = pwgen(nr_letters, nr_symbols,nr_numbers)
    print(password)
