from Exceptions import LineTooLongException
from Exceptions import IndentationException
from Exceptions import SemicolonException
from Exceptions import LessThanTwoSpacesException
from Exceptions import TodoFoundException
from Exceptions import MoreThanTwoBlankLinesException
from Exceptions import ConstructionFormatException
from Exceptions import FunctionNameFormatException
from Exceptions import ClassNameFormatException
from Exceptions import ArgumentNameFormatException
from Exceptions import VariableFormatException
from Exceptions import MutableArgumentException
from pathlib import Path
import os
import re


camel_case_regex = re.compile(r'^_{,2}[a-z][a-z0-9_]*_{,2}?$')


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


def check_for_spaces_after_construction(line, line_num):
    class_regex = re.compile(r'class [^\s]+')
    func_regex = re.compile(r'def [^\s]+')
    if "class" in line and class_regex.search(line) is None:
        return ConstructionFormatException(line_num, "class")
    elif "def" in line and func_regex.search(line) is None:
        return ConstructionFormatException(line_num, "def")
    else:
        return None


def check_for_class_name_format(line, line_num):
    if "class" in line:
        class_name_regex = re.compile(r'class\s+([A-Z][a-z0-9]+)+')
        if class_name_regex.search(line) is None:
            class_idx = line.find("class")
            class_name = line[class_idx + len("class"):].lstrip()
            space_idx = class_name.find(":")
            if space_idx != -1:
                class_name = class_name[:space_idx]
            return ClassNameFormatException(line_num, class_name)
        else:
            return None
    else:
        return None


def check_for_func_name_format(line, line_num):
    if "def" in line:
        func_idx = line.find("def")
        func_name = line[func_idx + len("def"):].lstrip()
        bracket_idx = func_name.find("(")
        if bracket_idx != -1:
            func_name = func_name[:bracket_idx]
        if camel_case_regex.match(func_name) is None:
            return FunctionNameFormatException(line_num, func_name), True
        else:
            return None, True
    else:
        return None, False


def get_args_list_from_line(line):
    left_bracket_idx = line.find("(")
    right_bracket_idx = line.find(")")
    arguments = line[left_bracket_idx + 1:right_bracket_idx]
    list_args = arguments.split(",")
    return list_args


def check_for_arg_name_format(line, line_num):
    if "def" in line:
        list_args = get_args_list_from_line(line)
        for arg in list_args:
            if arg:
                equals_idx = arg.find("=")
                if equals_idx != -1:
                    arg = arg[:equals_idx]
                self_idx = arg.find("self.")
                if self_idx != -1:
                    arg = arg[6:]
                arg = arg.strip()
                if camel_case_regex.match(arg) is None:
                    return ArgumentNameFormatException(line_num, arg)
    return None


def check_for_variable_name_format(line, line_num):
    if "def" not in line:
        equals_idx = line.find("=")
        if equals_idx != -1:
            var_name = line[:equals_idx].strip()
            if "self." in var_name:
                var_name = var_name[6:]
            if camel_case_regex.match(var_name) is None:
                return VariableFormatException(line_num, var_name)
    return None


def check_for_default_argument_mutability(line, line_num):
    if "def" in line:
        list_args = get_args_list_from_line(line)
        for arg in list_args:
            equals_idx = arg.find("=")
            if equals_idx != -1:
                if "[" in arg or "{" in arg:
                    return MutableArgumentException(line_num)
    return None


def analyze_file(path):
    line_counter = 0
    blank_lines_counter = 0
    exceptions = []
    function_body_entered = False
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
                    function_body_entered = False
                elif blank_lines_counter == 2:
                    function_body_entered = False
                blank_lines_counter = 0
                exceptions.append(check_for_spaces_after_construction(line, line_counter))
                exceptions.append(check_for_class_name_format(line, line_counter))
                function_name_format_result = check_for_func_name_format(line, line_counter)
                function_name_format_exception = function_name_format_result[0]
                exceptions.append(function_name_format_exception)
                exceptions.append(check_for_arg_name_format(line, line_counter))
                was_entered_result = function_name_format_result[1]
                if not function_body_entered and was_entered_result:
                    function_body_entered = True
                if function_body_entered:
                    exceptions.append(check_for_variable_name_format(line, line_counter))
                exceptions.append(check_for_default_argument_mutability(line, line_counter))
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
