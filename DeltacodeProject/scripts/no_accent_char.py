from unidecode import unidecode


def no_accent_char(char):
    return unidecode(char)
