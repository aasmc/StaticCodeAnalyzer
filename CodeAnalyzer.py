from LineTooLongException import LineTooLongException


class CodeAnalyzer:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def analyze(self):
        counter = 0
        with open(self.path_to_file, 'r') as program_file:
            for line in program_file:
                try:
                    counter += 1
                    if len(line) > 79:
                        raise LineTooLongException(counter)
                except LineTooLongException as err:
                    print(err)
