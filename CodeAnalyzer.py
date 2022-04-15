from Exceptions import LineTooLongException
from Exceptions import IndentationException
from Exceptions import SemicolonException
from Exceptions import LessThanTwoSpacesException
from Exceptions import TodoFoundException
from Exceptions import MoreThanTwoBlankLinesException


def check_for_long_line(line, line_number):
    if len(line) > 79:
        return LineTooLongException(line_number)
    else:
        return None


def check_for_indentation(line, line_number):
    indentation = len(line) - len(line.lstrip())
    if 0 < indentation < 4 or indentation % 4 != 0:
        return IndentationException(line_number)
    else:
        return None


def check_for_semicolons(line, line_num):
    semi_colon_last_index = line.rfind(";")
    if semi_colon_last_index != -1:
        quote_first_idx = line.find('"')
        while quote_first_idx != -1:
            quote_last_index = line.find('"', quote_first_idx + 1)
            if quote_first_idx < semi_colon_last_index < quote_last_index:
                return None
            quote_first_idx = line.find('"', quote_last_index + 1)
        quote_first_idx = line.find("'")
        while quote_first_idx != -1:
            quote_last_index = line.find("'", quote_first_idx + 1)
            if quote_first_idx < semi_colon_last_index < quote_last_index:
                return None
            quote_first_idx = line.find("'", quote_last_index + 1)
        comment_idx = line.find("#")
        if comment_idx != -1:
            if semi_colon_last_index < comment_idx:
                return SemicolonException(line_num)
        else:
            return SemicolonException(line_num)
    else:
        return None


def check_for_spaces_before_comments(line, line_num):
    comment_idx = line.find("#")
    if comment_idx != -1 and comment_idx != 0:
        line_before_comment = line[0:comment_idx]
        num_right_spaces = len(line_before_comment) - len(line_before_comment.rstrip())
        if num_right_spaces < 2:
            return LessThanTwoSpacesException(line_num)

    return None


def check_for_todo(line, line_num):
    comment_idx = line.find("#")
    line_after_comment = line[comment_idx:].lower()
    if "todo" in line_after_comment:
        return TodoFoundException(line_num)
    return None


class CodeAnalyzer:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def analyze(self):
        line_counter = 0
        blank_lines_counter = 0
        exceptions = []
        with open(self.path_to_file, 'r') as program_file:
            for line in program_file:
                line_counter += 1
                if line.strip():
                    exceptions.append(check_for_long_line(line, line_counter))
                    exceptions.append(check_for_indentation(line, line_counter))
                    exceptions.append(check_for_semicolons(line, line_counter))
                    exceptions.append(check_for_spaces_before_comments(line, line_counter))
                    exceptions.append(check_for_todo(line, line_counter))
                    if blank_lines_counter > 2:
                        exceptions.append(MoreThanTwoBlankLinesException(line_counter))
                    blank_lines_counter = 0
                else:
                    blank_lines_counter += 1
        filtered = filter(lambda ex: ex, exceptions)
        for e in filtered:
            print(e)



