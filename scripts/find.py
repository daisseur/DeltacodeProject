def find(txt, first, second, replace=False):
    second = "' " if second == "'" else second

    result = (txt[txt.find(first):txt.find(second)])
    result = None if result == '' else str(result)

    if result[1] != second and result:
        result += second

    if replace:
        result = result.replace(first, '').replace(second, '')
    return result
