# coding:utf-8
import sys
import time
import string as s


def print_color(string: str, color='white', effect='classic', highlight='False') -> None:
    nocolor = "\033[0;0m"
    colors = {
        'black': '0;',
        'red': '1;',
        'green': '2;',
        'yellow': '3;',
        'blue': '4;',
        'violet': '5;',
        'cyan': '6;',
        'grey': '7;',
        'white': '9;'}
    effects = {
        'bold': '1m',
        'classic': '2m',
        'italic': '3m',
        'underline': '4m',
        'strike': '9m'}
    highlights = {
        'False': '\033[3',
        'True': '\033[4'}
    print(highlights[highlight] + colors[color] + effects[effect] + string + nocolor)


# -- Coding with lists

def encode(password: str, string: str) -> str:
    password = password.lower()
    lowercase = s.ascii_lowercase
    uppercase = s.ascii_uppercase
    result = str()
    password_len = len(password)
    for i in range(len(string)):
        char = string[i]
        if char in lowercase:
            result += lowercase[(lowercase.index(char) + lowercase.index(password[i % password_len])) % 26]
        elif char in uppercase:
            result += uppercase[(uppercase.index(char) + lowercase.index(password[i % password_len])) % 26]
        else:
            result += char
    return result


def decode(password: str, string: str) -> str:
    password = password.lower()
    lowercase = s.ascii_lowercase
    uppercase = s.ascii_uppercase
    result = str()
    password_len = len(password)
    for i in range(len(string)):
        char = string[i]
        if char in lowercase:
            result += lowercase[lowercase.index(char) - lowercase.index(password[i % password_len])]
        elif char in uppercase:
            result += uppercase[uppercase.index(char) - lowercase.index(password[i % password_len])]
        else:
            result += char
    return result


# -- Coding with ASCII table

# -- Menu

def choice_selector(function) -> str:
    password = input('Password : ')
    return function(password.lower(), input('Texte : '))


def main(function: int) -> None:
    while True:
        choice = input('[1- Encode | 2- Decode ] : ')
        if choice == '1':
            print('== ENCODE ==')
            if function == 1:
                print_color(choice_selector(encode), color='blue')
            else:
                print_color(choice_selector(encode), color='blue')
        elif choice == '2':
            print('== DECODE ==')
            if function == 1:
                print_color(choice_selector(decode), color='blue')
            else:
                print_color(choice_selector(decode), color='blue')
        else:
            print_color('Invalid choice', color='red', effect='bold')


def benchmark(function, loops, *args):
    global results
    t = time.perf_counter()
    for i in range(loops):
        function(*args)
    results.append(f'{function.__name__} : {round((time.perf_counter() - t) * 1000, round_value)}')
    return


if __name__ == '__main__':
    main(0)

