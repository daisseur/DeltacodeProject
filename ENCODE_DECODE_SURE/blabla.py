class Encoding:
    def __init__(self, password: str, shift=0):
        self.valid_chars = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        self.__valid_chars_len = len(self.valid_chars)
        self.__valid_chars_ascii = [ord(char) for char in self.valid_chars]
        self.__valid_chars_ascii_sorted = sorted(self.__valid_chars_ascii)
        self.__shift = self.__check_shift(shift)
        self.password = self.__check_string(password)
        self.__password_len = len(password)
        self.results = {'encode': [], 'decode': []}

    def __check_shift(self, shift):
        shift_exception = Exception(
            f'Shift must be an integer in range({- self.__valid_chars_ascii_sorted[0]} ,{0x10ffff - self.__valid_chars_ascii_sorted[-1] - self.__valid_chars_len})')
        if shift < - self.__valid_chars_ascii_sorted[0]:
            raise shift_exception
        elif shift + self.__valid_chars_ascii_sorted[-1] + self.__valid_chars_len > 0x10ffff:
            raise shift_exception
        return shift

    def __check_string(self, string: str) -> str:
        for char in string:
            if not char in self.valid_chars:
                raise Exception('Invalid char ' + char + ' in the string')
            else:
                return string.lower()

    def encode(self, string):
        string = self.__check_string(string)
        result = ''
        for i in range(len(string)):
            result += chr(
                ord(string[i]) + self.valid_chars.index(self.password[i % self.__password_len]) + self.__shift)
        self.results['encode'].append([string, result])
        return result

    def decode(self, string):
        string = string.lower()
        result = ''
        try:
            for i in range(len(string)):
                result += chr(
                    ord(string[i]) - self.valid_chars.index(self.password[i % self.__password_len]) - self.__shift)
            self.results['decode'].append([string, result])
        except Exception:
            raise Exception(f'Shift or password are invalid')
        return result

    def results_reset(self):
        self.results = {'encode': [], 'decode': []}

    def set_password(self, password):
        self.password = password


printable = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

if __name__ == '__main__':
    # 33 126
    shift = 1113891
    daisseur_weird_encoding = Encoding(printable, shift)
    txt_encoded = daisseur_weird_encoding.encode(printable)
    print('encoded', txt_encoded)
    print('decoded', daisseur_weird_encoding.decode(txt_encoded))
    print(daisseur_weird_encoding.results)
