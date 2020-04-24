import sys
from urllib.request import urlopen


def fetch_words(url):
    json = urlopen(url)
    dicts = []

    for line in json:
        line_words = line.decode('utf-8').split(',')
        for word in line_words:
            dicts.append(word)

    json.close()
    return dicts


def print_items(items):
    for word in items:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
    # Run example: python3 words.py <your-url>
