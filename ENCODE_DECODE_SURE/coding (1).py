# import unittest

"""
class TestEncodingMethods(unittest.TestCase):
    def test(self):
        encoding = Encoding()
        encoding.set_password(encoding.valid_chars)

        for char in encoding.valid_chars:
            string = char * len(encoding.valid_chars)

            # shift min
            encoding.set_shift(encoding.shift_min)
            encrypted = encoding.encode(string)
            self.assertEqual(string, encoding.decode(encrypted))

            # shift max
            encoding.set_shift(encoding.shift_max)
            encrypted = encoding.encode(string)
            self.assertEqual(string, encoding.decode(encrypted))
"""


class Encoding:
    def __init__(self, password='', shift=0):
        self.valid_chars = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n¤§°™±²¬¡\t\f\b\r"""
        # """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n "'"""
        self.__valid_chars_len = len(self.valid_chars)
        self.__valid_chars_ascii = [ord(char) for char in self.valid_chars]
        self.valid_chars_ascii_sorted = sorted(self.__valid_chars_ascii)
        self.shift_min = -self.valid_chars_ascii_sorted[0]
        self.shift_max = 0x110000 - self.valid_chars_ascii_sorted[-1] - self.__valid_chars_len
        self.__shift = self.__check_shift(shift)
        self.__password = password
        self.__password_len = len(password)
        self.results = {'encoded': [], 'decoded': []}

    def __check_shift(self, shift):
        shift_exception = Exception(f'Shift must be an integer in range({self.shift_min} ,{self.shift_max})')
        if shift < self.shift_min:
            raise shift_exception
        elif shift > self.shift_max:
            raise shift_exception
        return shift

    def __check_string(self, string: str) -> str:
        for char in string:
            if char not in self.valid_chars:
                raise Exception('Invalid char ' + char + ' in the string')
            else:
                return string

    def encode(self, string) -> str:
        string = self.__check_string(string)
        result = ''
        for i in range(len(string)):

            result += chr(ord(string[i]) + self.valid_chars.index(self.__password[i % self.__password_len]) + self.__shift)
        self.results['encoded'].append(result)
        return result

    def decode(self, string) -> str:
        string = string
        result = ''
        try:
            for i in range(len(string)):
                result += chr(
                    ord(string[i]) - self.valid_chars.index(self.__password[i % self.__password_len]) - self.__shift)
            self.results['decoded'].append(result)
        except Exception:
            raise Exception(f'Shift or password are invalid')
        return result

    def reset_results(self):
        self.results = {'encoded': [], 'decoded': []}

    def set_password(self, password):
        self.__password = self.__check_string(password)
        self.__password_len = len(self.__password)

    def set_shift(self, shift):
        self.__shift = self.__check_shift(shift)


def t_e_s_t_all():
    encoding = Encoding()
    encoding.set_password(encoding.valid_chars)
    print('test start')

    # Exception: Shift must be an integer in range(-10 ,1113889)
    for char in encoding.valid_chars:
        string = char * len(encoding.valid_chars)
        for shift in range(encoding.shift_min, encoding.shift_max, 10000):
            encoding.set_shift(shift)
            res = encoding.decode(encoding.encode(string))
            if string != res:
                print(shift, string, res)
    print('if there\'s nothing displayed between start and end, test is ok')
    print('test end')


if __name__ == '__main__':
    encoding = Encoding()

    encoding.set_shift(encoding.shift_max)
    encoding.set_password(encoding.valid_chars)

    txt_to_encode = ["encode me", "me too", encoding.valid_chars]

    for txt in txt_to_encode:
        encoding.encode(txt)

    for results in encoding.results['encoded']:
        encoding.decode(results)

    for i in range(len(encoding.results['decoded'])):
        print('#=======================================================#')
        print('encoded =>', repr(encoding.results['encoded'][i])[1:][:-1])  # this prints all chars
        print('decoded =>', encoding.results['decoded'][i])
