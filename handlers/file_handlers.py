# coding: utf-8


'''Fila managers.

Manipulate existing files in the main directory.
'''


def write_file(filename: str, data='') -> None:
    '''Generate a new file.

    Create a file in root directory. Required the name parameter.
    '''

    _instance = open(filename, 'w')
    _instance.write(str(data))
    _instance.close()


def read_file_data(filename: str) -> str or None:

    try:
        _instance = open(filename or 'input.txt', 'r')
        _data = _instance.read()
        _instance.close()

        return _data

    except Exception:
        print('Input-file not found.')

        return ''
