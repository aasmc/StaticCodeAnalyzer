class AnalyzerException(Exception):
    def __init__(self, line_num, err_code, err_msg):
        self.message = f"Line {line_num}: {err_code} {err_msg}"
        super().__init__(self.message)


class LineTooLongException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S001",
            err_msg="Too long"
        )


class IndentationException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S002",
            err_msg="Indentation is not a multiple of four"
        )


class SemicolonException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S003",
            err_msg="Unnecessary semicolon"
        )


class LessThanTwoSpacesException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S004",
            err_msg="At least two spaces required before inline comments"
        )


class TodoFoundException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S005",
            err_msg="TODO found"
        )


class MoreThanTwoBlankLinesException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S006",
            err_msg="More than two blank lines used before this line"
        )
