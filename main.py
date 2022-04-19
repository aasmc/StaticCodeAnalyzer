from CodeAnalyzer import analyze_file
from CodeAnalyzer import analyze_dir
import sys


def analyze():
    path = sys.argv[1]
    if path.endswith(".py"):
        analyze_file(path)
    else:
        analyze_dir(path)


if __name__ == '__main__':
    analyze()

