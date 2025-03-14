import argparse
import utils

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Trie')

    parser.add_argument('--reference',
                        help='Reference sequence file',
                        type=str)

    parser.add_argument('--string',
                        help='Reference sequence',
                        type=str)

    parser.add_argument('--query',
                        help='Query sequences',
                        nargs='+',
                        type=str)

    return parser.parse_args()

def build_suffix_trie(s):
    trie = {}
    for i in range(len(s)):
        current = trie
        for char in s[i:]:
            if char not in current:
                current[char] = {}
            current = current[char]
        # Optionally, you can mark the end of a suffix with a terminal marker
        current['#'] = True
    return trie

def search_trie(trie, pattern):
    current = trie
    match_length = 0
    for char in pattern:
        if char in current:
            match_length += 1
            current = current[char]
        else:
            break
    return match_length

def main():
    args = get_args()

    T = None

    if args.string:
        T = args.string
    elif args.reference:
        reference = utils.read_fasta(args.reference)
        T = reference[0][1]

    trie = build_suffix_trie(T)

    if args.query:
        for query in args.query:
            match_len = search_trie(trie, query)
            print(f'{query} : {match_len}')

if __name__ == '__main__':
    main()
