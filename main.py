from CodeAnalyzer import CodeAnalyzer


def analyze():
    path = input()
    analyzer = CodeAnalyzer(path)
    analyzer.analyze()


if __name__ == '__main__':
    analyze()

