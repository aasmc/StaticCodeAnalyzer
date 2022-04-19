from Exceptions import LineTooLongException
from Exceptions import IndentationException
from Exceptions import SemicolonException
from Exceptions import LessThanTwoSpacesException
from Exceptions import TodoFoundException
from Exceptions import MoreThanTwoBlankLinesException
from pathlib import Path
import os
import re


def check_for_long_line(line, line_number):
    if len(line) > 79:
        return LineTooLongException(line_number)
    else:
        return None


def check_for_indentation(line, line_number):
    indents_reg = re.compile(r'^\s+')
    indents = indents_reg.search(line)
    if indents is not None and len(indents[0]) % 4 != 0:
        return IndentationException(line_number)
    else:
        return None


def check_for_semicolons(line, line_num):
    if (";" in line) and (re.search(r'#.*;|[\'\"].*;.*[\'\"]', line) is None):
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


def analyze_file(path):
    line_counter = 0
    blank_lines_counter = 0
    exceptions = []
    with open(path, 'r') as program_file:
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
        print(f"{path}:", e)


def analyze_dir(path):
    files_to_analyze = []
    analyze_dir_recursive(path, files_to_analyze)
    for f in sorted(files_to_analyze):
        analyze_file(f)


def analyze_dir_recursive(path, files_to_analyze):
    entries = Path(path)
    for entry in entries.iterdir():
        new_path = os.path.join(path, entry.name)
        if entry.is_file():
            files_to_analyze.append(new_path)
        else:
            analyze_dir_recursive(new_path, files_to_analyze)

