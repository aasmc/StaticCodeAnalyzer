from CodeAnalyzer import CodeAnalyzer


def analyze():
    path = "test_code.py"
    analyzer = CodeAnalyzer(path)
    analyzer.analyze()


if __name__ == '__main__':
    analyze()

