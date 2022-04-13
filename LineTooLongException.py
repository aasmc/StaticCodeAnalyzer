class LineTooLongException(Exception):
    def __init__(self, line_num):
        self.message = f"Line {line_num}: S001 Too long"
        super().__init__(self.message)
