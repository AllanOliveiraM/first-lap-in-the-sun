# coding: utf-8


'''Starts aplication with API features.

Process input text to output text.
'''


from core.engine import Processors
from handlers.file_handlers import write_file, read_file_data


if __name__ == '__main__':

    Processor = Processors()

    input_file_name = input('Nome do arquivo de entrada > ')
    
    write_file(
        'output.txt',
        Processor.parse(
            read_file_data(
                input_file_name
            )
        )
    )
