from unidecode import unidecode

def chercher(txt, premier, deuxieme, replace=False):
    if deuxieme == "'":
        deuxieme = "' "

    result = (txt[txt.find(premier): txt.find(deuxieme)])

    if result == "":
        result = "#La chaîne de caractères n'a pas été trouvée#"

    result = str(result)

    if not result.startswith(deuxieme, 18) and result != "#La chaîne de caractères n'a pas été trouvée#":
        result = result + deuxieme

    if replace:
        result = result.replace(premier, '').replace(deuxieme, '')
    return result

def no_accent_char(char):
    return unidecode(char)

def print_color(*args, color='white', effect='classic', highlight='False') -> None:
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
    print(highlights[highlight] + colors[color] + effects[effect] + ' '.join(str(arg) for arg in args) + nocolor)