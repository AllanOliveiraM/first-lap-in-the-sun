# coding: utf-8


'''Processor core engine.

Replace and generate crypt code with data mapping.
'''


from random import randint

from parsers.mapping import MAPPING


class Processors():
    '''Processor class with parse methods.'''

    def __init__(self):
        self._input = None

        self.splited_data = []
        self.parsed_data = []

    def _split_data(self):
        '''Split all chars in one list.'''

        for character in self._input:
            self.splited_data.append(character.lower())

    def _parse_data(self):
        '''Parse splitted data.'''

        for character in self.splited_data:
            nuance = randint(1, 2)
            current_parsed_character = None

            try:
                _parse_f_result = MAPPING["f"][character]

                try:
                    if len(_parse_f_result) != 1:
                        _parse_f_result = _parse_f_result[randint(
                            1, len(_parse_f_result) - 1)]
                        _parse_f_result = f'[{_parse_f_result}]'

                except:
                    pass

                current_parsed_character = f'f{_parse_f_result}'
            except Exception:
                current_parsed_character = character

            if nuance == 2:
                try:
                    _parse_d_result = MAPPING["d"][character]

                    try:
                        if len(_parse_d_result) != 1:
                            _parse_d_result = _parse_d_result[randint(
                                1, len(_parse_d_result) - 1)]
                            _parse_d_result = f'[{_parse_d_result}]'
                    except:
                        pass

                    current_parsed_character = f'd{_parse_d_result}'
                except Exception:
                    pass

            if len(self.parsed_data) != 0:
                if (
                    current_parsed_character == ' '
                        and current_parsed_character != self.parsed_data[-1]):
                    self.parsed_data.append(current_parsed_character)
                else:
                    if current_parsed_character != ' ':
                        self.parsed_data.append(current_parsed_character)

            else:
                self.parsed_data.append(current_parsed_character)

    def parse(self, data: str) -> str:
        '''Public parse manager method.'''

        self._input = data

        self._split_data()
        self._parse_data()

        char_code_list = []

        for char_code in self.parsed_data:
            if char_code != '\n':
                char_code_list.append(char_code)

        char_number_counter = 0
        formatted_char_code_list = ''

        for char_code in char_code_list:
            if char_number_counter % 11 == 0:
                formatted_char_code_list = formatted_char_code_list + '\n' + '-'
            formatted_char_code_list = formatted_char_code_list + char_code + '-'
            char_number_counter += 1

        formatted_char_code_list = formatted_char_code_list.replace(' ', '|')
        formatted_char_code_list = formatted_char_code_list.replace('-', ' ')

        return formatted_char_code_list
