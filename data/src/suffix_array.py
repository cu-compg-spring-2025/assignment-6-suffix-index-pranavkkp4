import argparse
import utils
import suffix_tree

SUB = 0
CHILDREN = 1

def get_args():
    parser = argparse.ArgumentParser(description='Suffix Tree')

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

def build_suffix_array(T):
    tree = suffix_tree.build_suffix_tree(T)
    suffix_array = []
    
    def dfs(node_idx, depth):
        node = tree[node_idx]
        if not node[CHILDREN]:  # If it's a leaf node
            suffix_array.append(depth - len(node[SUB]))
        for child_idx in sorted(node[CHILDREN].values()):
            dfs(child_idx, depth + len(tree[child_idx][SUB]))
    
    dfs(0, 0)  # Start DFS traversal from the root
    return sorted(suffix_array)

def search_array(suffix_array, q):
    lo, hi = 0, len(suffix_array)
    while lo < hi:
        mid = (lo + hi) // 2
        if suffix_array[mid] < q:
            lo = mid + 1
        else:
            hi = mid
    return lo

def main():
    args = get_args()

    T = None

    if args.string:
        T = args.string
    elif args.reference:
        reference = utils.read_fasta(args.reference)
        T = reference[0][1]
    
    T += "$"  # Append terminal character to ensure uniqueness
    
    array = build_suffix_array(T)

    if args.query:
        for query in args.query:
            match_index = search_array(array, query)
            print(f'{query} : {match_index}')

if __name__ == '__main__':
    main()
