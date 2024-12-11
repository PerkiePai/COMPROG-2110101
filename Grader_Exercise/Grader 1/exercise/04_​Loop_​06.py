line = int(input())

def pyramid(line):
    for i in range(1, line + 1):
        if i == line:
            print('*' * (2 * line - 1))
        else:
            for j in range(1, line + i):
                if j == line - i + 1:
                    print('*', end='')
                elif j == line + i - 1:
                    print('*', end='')
                else:
                    print('.', end='')
            print()

pyramid(line)
