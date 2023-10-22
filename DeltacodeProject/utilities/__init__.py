from os.path import dirname, join
from subprocess import run
from sys import executable


def util_encode(*args):
    path = join(dirname(__file__), "encode.py")
    print(path)
    run([executable, path] + list(args), shell=True)


def util_decode(*args):
    path = join(dirname(__file__), "decode.py")
    print(path)
    run([executable, path] + list(args), shell=True)
