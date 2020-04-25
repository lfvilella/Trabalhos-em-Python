DICT = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def convert(string):
    """ Convert str to int """
    x = -1
    try:
        number = ''
        for token in string:
            number += DICT[token]
        x = int(number)
    except (KeyError, TypeError) as error:
        print(f'Failed - {error!r}')
        pass

    return x
