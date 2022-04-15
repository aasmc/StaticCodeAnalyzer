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

