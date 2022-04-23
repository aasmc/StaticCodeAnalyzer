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


class ConstructionFormatException(AnalyzerException):
    def __init__(self, line_num, constr_type):
        super().__init__(
            line_num=line_num,
            err_code="S007",
            err_msg=f"Too many spaces after '{constr_type}'"
        )


class ClassNameFormatException(AnalyzerException):
    def __init__(self, line_num, class_name):
        super().__init__(
            line_num=line_num,
            err_code="S008",
            err_msg=f"Class name '{class_name}' should use CamelCase"
        )


class FunctionNameFormatException(AnalyzerException):
    def __init__(self, line_num, func_name):
        super().__init__(
            line_num=line_num,
            err_code="S009",
            err_msg=f"Function name '{func_name}' should use snake_case"
        )


class ArgumentNameFormatException(AnalyzerException):
    def __init__(self, line_num, arg_name):
        super().__init__(
            line_num=line_num,
            err_code="S010",
            err_msg=f"Argument name '{arg_name}' should be snake_case"
        )


class VariableFormatException(AnalyzerException):
    def __init__(self, line_num, var_name):
        super().__init__(
            line_num=line_num,
            err_code="S011",
            err_msg=f"Variable '{var_name}' in function should be snake_case"
        )


class MutableArgumentException(AnalyzerException):
    def __init__(self, line_num):
        super().__init__(
            line_num=line_num,
            err_code="S012",
            err_msg=f"Default argument value is mutable"
        )