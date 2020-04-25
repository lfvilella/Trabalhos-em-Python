import sys

def read_file(file):
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            sys.stdout.write(line)


if __name__ == "__main__":
    read_file(sys.argv[1])
