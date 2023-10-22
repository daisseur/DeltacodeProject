import os
from time import sleep
from DeltacodeProject.encodings._encodings3 import DayEncoding
from threading import Thread


def simple(obj):
    for i in obj:
        pass


def encode_and_start(_bytes):
    d = DayEncoding("H4RD-pass_word#R€4LL£")
    thread = Thread(target=simple, args=[d.encode_byte(_bytes)])
    thread.start()
    sleep(0.5)
    return d.get_estim()


def test(_bytes=None):
    if _bytes is None:
        print(os.getcwd())
        _bytes = open("../Deltacode.ico", 'rb').read()

    print(len(_bytes))
    _test = encode_and_start(_bytes)
    print(_test)
    if _test > 0.0:
        print("TEST COMPLETED")
    else:
        print("TEST FAILED", _test)


if __name__ == "__main__":
    test()