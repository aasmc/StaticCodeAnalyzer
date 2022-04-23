# Static Code Analyzer
Educational project based on the course from JetBrains HyperSkill Academy. Level Challenging. 

## Description

To make sure your Python code is beautiful and consistently formatted, you should follow the PEP8 specification and best practices recommended by the Python community. This is not always easy, especially for beginners. Luckily, there are special tools called static code analyzers (pylint, flake8, and others) that automatically check that your code meets all the standards and recommendations. These tools don't execute your code but just analyze it and output all the issues they find.

In this project, you will create a small static analyzer tool that finds some common stylistic mistakes in Python code. This way, you will familiarize yourself with the concept of static code analysis and improve your Python skills along the way.

PEP8 requires that we should "limit all lines to a maximum of 79 characters", which is designed to make your code more readable. So let's first make a program that checks that code lines are not too long.
## Objectives

In this stage, your program should read Python code from a specified file and perform a single check: the length of code lines should not exceed 79 characters.

Note that:

- The path to the file is obtained from standard input.
- The general output format is: 
```text
Line X: Code Message
```
In the format:

- X is the number of the line where the issue was found. The count starts from one.

- Code is the code of the discovered stylistic issue (like S001).

- Message is a human-readable description of the issue (optional).

For example:
```text
Line 3: S001 Too long
```
This format will be used throughout the project with some minor changes.
- The order of the lines should always be first to last.
- Your program can output another message instead of Too long. The rest of the output must exactly match the provided example. In the code S001, S means a stylistic issue, and 001 is the internal number of the issue.

### Examples

Here is an example of the file's contents:
```python
print('What\'s your name?')
name = input()
print(f'Hello, {name}')  # here is an obvious comment: this prints a greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)
```
This code contains two long lines (>79 characters): lines 3 and 5.

Here is the expected output for the given example:
```text
Line 3: S001 Too long
Line 5: S001 Too long
```

## Stage 2
### Description

Let's add a few more checks to the program. All of them are consistent with the PEP8 style guide.
### Objectives

In this stage, you need to add checks for the following five errors to your program:

- [S002] Indentation is not a multiple of four;
- [S003] Unnecessary semicolon after a statement (note that semicolons are acceptable in comments);
- [S004] Less than two spaces before inline comments;
- [S005] TODO found (in comments only and case-insensitive);
- [S006] More than two blank lines preceding a code line (applies to the first non-empty line).

Please note that:

- if a line contains the same stylistic issue several times, your program should print the information only once. However, if a single line has several issues with different types of error codes, they should be printed as a sorted list.
- To simplify the task, we consider it acceptable if your program finds some false-positive stylistic issues in strings, especially in multi-lines ('''...''' and """...""").
- We recommend that you break your code into a set of functions to avoid confusion.

Once again:

- The path to the file with Python code is obtained from standard input.
- The general output format is:
```text
    Line X: Code Message
```
- The lines with found issues must be output in ascending order.

### Examples
Here is an example of badly styled Python code (please never write code like this!):
```python
print('What\'s your name?') # reading an input
name = input();
print(f'Hello, {name}');  # here is an obvious comment: this prints a greeting with a name


very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)



def some_fun():
    print('NO TODO HERE;;')
    pass; # Todo something
```

It contains nine code style issues:
```text
Line 1: S004 At least two spaces required before inline comments
Line 2: S003 Unnecessary semicolon
Line 3: S001 Too long
Line 3: S003 Unnecessary semicolon
Line 6: S001 Too long
Line 11: S006 More than two blank lines used before this line
Line 13: S003 Unnecessary semicolon
Line 13: S004 At least two spaces required before inline comments
Line 13: S005 TODO found
```

## Stage 3
### Objectives

In this stage, you need to improve your program so that it can analyze all Python files inside a specified directory.

Please note that:
- You also need to change the input format. Instead of reading the path from the standard input, the program must obtain it as a command-line argument:
```text
> python code_analyzer.py directory-or-file
```

- The output format also needs to be changed slightly. It should include the path to the analyzed file:
```text
Path: Line X: Code Message 
```
- All output lines must be sorted in ascending order according to the file name, line number, and issue code.
- Non-Python files must be skipped.

Once again:

- It is important that all the checks implemented in the previous stages continue to work properly.

- If a line contains the same stylistic issue several times, your program must print the information only once. If a line has several issues with different types of error codes, they should be printed in ascending order.

- To simplify the solution, we consider it acceptable if your program finds some false-positive stylistic issues in strings, especially in multi-lines ('''...''' and """...""").

- We recommend that you break your program code into a set of functions and classes to avoid confusion.

### Examples
Only a single file is specified as the input:
```text
> python code_analyzer.py /path/to/file/script.py
/path/to/file/script.py: Line 1: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 2: S003 Unnecessary semicolon
/path/to/file/script.py: Line 3: S001 Too long line
/path/to/file/script.py: Line 3: S003 Unnecessary semicolon
/path/to/file/script.py: Line 6: S001 Too long line
/path/to/file/script.py: Line 11: S006 More than two blank lines used before this line
/path/to/file/script.py: Line 13: S003 Unnecessary semicolon
/path/to/file/script.py: Line 13: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 13: S005 TODO found
```

The input path is a directory; the output should contain all Python files from it:
```text
> python code_analyzer.py /path/to/project
/path/to/project/__init__.py: Line 1: S001 Too long line
/path/to/project/script1.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script1.py: Line 2: S003 Unnecessary semicolon
/path/to/project/script2.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script2.py: Line 3: S001 Too long line
/path/to/project/somedir/script.py: Line 3: S001 Too long line
/path/to/project/test.py: Line 3: Line 13: S003 Unnecessary semicolon
```

Useful links
- https://realpython.com/working-with-files-in-python/
- https://dbader.org/blog/python-generator-expressions
- https://realpython.com/python-pathlib/

## Stage 4
### Description

As many coders say, naming is one of the hardest things in programming. Good naming makes your code more readable and uniform. Names should also follow style guides. In Python, the basic requirement is using snake_case for function names and CamelCase for class names. Also, there should be only one space between the construction name and the object name. Checking these rules is the next feature that we need to implement.

Check out the Python tutorial about regular expressions: they will help you implement the checks.
### Objectives

In this stage, we need to add three new checks to the program:

- [S007] Too many spaces after construction_name (def or class);

- [S008] Class name class_name should be written in CamelCase;

- [S009] Function name function_name should be written in snake_case.

Note that:
- Functions names may start or end with underscores (__fun, __init__).
- To simplify the task, we will assume that classes are always written as in the following examples:
```python
# a simple class
class MyClass:
    pass

# a class based on inheritance
class MyClass(AnotherClass):
    pass
```
In reality, it's possible to declare a class this way:
```python
class \
        S:
    pass
```

However, since it is not a common way to declare classes, you can ignore it.

- Another assumption is that functions are always declared like this:
```python
def do_magic():
    pass
```

As before:
- The program obtains the path to the file or directory via command-line arguments:
```text
> python code_analyzer.py directory-or-file
```
- All the previously implemented checks should continue to work properly.

### Examples:

```python
class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')
```

```text
/path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
/path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
```

## Stage 5
Theory

In this stage, it is preferable to make use of the ast module (Abstract Syntactic Tree). If you feel that you need to know more about it, here are two tutorials that can help you work with it:

- A short tutorial: How to use AST to understand code https://www.mattlayman.com/blog/2018/decipher-python-ast/
- A long tutorial that complements the standard documentation https://greentreesnakes.readthedocs.io/en/latest/

ast module also contains many classes that represent different elements of Python's syntax. For example, the class FunctionDef is a node of the tree representing a definition of some function in the code, the class arguments represents function's arguments, the class Assign represents an expression where a value gets assigned to some variable. You can use all these (and other) classes to find places of the code (names of the variables and so on) that you want to check for correctness:
```python
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        function_name = node.name
        # check whether the function's name is written in camel_case
        pass
```
Don't be shy to check some other classes and functions of this module to feel confident while using it. 
### Description

In this final stage, you need to improve your program to check that all the names of function arguments as well as local variables meet the requirements of PEP8. The program must not force the names of variables outside of functions (for example, in modules or classes). The most convenient way to do this is to use the Abstract Syntactic Tree (AST) from the ast module.

Also, your program must check that the given code does not use mutable values (lists, dictionaries, and sets) as default arguments to avoid errors in the program.
### Objectives

You need to add three new checks to your analyzer:

- [S010] Argument name arg_name should be written in snake_case;
- [S011] Variable var_name should be written in snake_case;
- [S012] The default argument value is mutable.

Please note that:

- Names of functions, as well as names of variables in the body of a function should be written in snake_case. However, the error message for an invalid function name should be output only when the function is defined. The error message for an invalid variable name should be output only when this variable is assigned a value, not when this variable is used further in the code.
- To simplify the task, you only need to check whether the mutable value is directly assigned to an argument:
```python
def fun1(test=[]):  # default argument value is mutable
    pass


def fun2(test=get_value()):  # you can skip this case to simplify the problem
    pass
```

- If a function contains several mutable arguments, the message should be output only once for this function.
- Variable and argument names are assumed to be valid if they are written in snake_case. Initial underscores (_) are also acceptable.

As before:

- You can use other messages, but the check codes must be exactly as given above.
- All the previously implemented checks should continue to work correctly, and the program should be able to read from one or more files.

### Examples
```python
CONSTANT = 10
names = ['John', 'Lora', 'Paul']


def fun1(S=5, test=[]):  # default argument value is mutable
    VARIABLE = 10
    string = 'string'
    print(VARIABLE)
```
The expected output for this code is:
```text
/path/to/file/script.py: Line 5: S010 Argument name 'S' should be snake_case
/path/to/file/script.py: Line 5: S012 Default argument value is mutable
/path/to/file/script.py: Line 6: S011 Variable 'VARIABLE' in function should be snake_case
```

Note that the message for the line print(VARIABLE) is not printed since it was already output for line 6, where the variable VARIABLE is assigned a value.
### Extra
You can also use AST to rewrite some of the checks implemented before. It would be especially convenient for checking the names of functions and classes.

If you would like to continue improving this project, you can also:

- implement all of the standard PEP8 checks;
- display column numbers;
- disable some of the checks via command-line arguments.



