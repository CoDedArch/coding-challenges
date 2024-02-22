import sys
from getopt import getopt, GetoptError

def count_bytes(file_name):
    with open(file_name, 'rb') as f:
        return len(f.read())

def count_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

def count_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return sum(len(line.split()) for line in f)

def count_chars(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return sum(len(line) for line in f)
    
def default_options(file_name):
    byte_count = count_bytes(file_name)
    word_count = count_words(file_name)
    line_count = count_lines(file_name)
    char_count = count_chars(file_name)

    print(f'{line_count} {word_count} {byte_count} {file_name}')
    sys.exit()

def main(argv):
    file_name = None
    option = None
    print(argv)

    if len(argv) == 1:
            file_name = argv[0]
    if not len(argv) == 1:
        try:
            opts, args = getopt(argv, 'c:i:w:m: ', ['byte=', 'line=', 'word=', 'char='])
        except GetoptError:
            print(f'{__name__} -c <command> failed')
            sys.exit(2)

        if not opts:
            print(f"Usage: {__name__} -c <command>")
            sys.exit(2)

        option, file_name = opts[0]
        print(file_name)

        if option in ('-c', '--byte'):
            result = count_bytes(file_name)
        elif option in ('-i', '--line'):
            result = count_lines(file_name)
        elif option in ('-w', '--word'):
            result = count_words(file_name)
        elif option in ('-m', '--char'):
            result = count_chars(file_name)
        print(f'{result} {file_name}')
        sys.exit()

    
    default_options(file_name)

if __name__ == '__main__':
    main(sys.argv[1:])
