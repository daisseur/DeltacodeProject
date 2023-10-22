from time import sleep


def loading(string: str, time=0.01):
    for char in string:
        print(char, flush=True, end='')
        sleep(time)
    print()
