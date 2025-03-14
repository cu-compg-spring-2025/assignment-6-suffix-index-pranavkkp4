[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2H4hMYgM)

# suffix_index
Suffix data structures for aligning reads to a reference.

This repository implements several suffix-based data structures and search functions to support efficient matching of query sequences against a reference string.

---

## Suffix Tree

### `add_suffix(nodes, suf)`

#### Purpose
The `add_suffix` function integrates a suffix `suf` into an existing tree structure represented by nodes. This function modifies the nodes structure in-place by either adding a new node for the suffix if it's not already present, or by splitting an existing node in case only a part of the suffix matches.

#### Parameters
- **nodes**: A list of nodes representing the current state of the suffix tree. Each node is a list containing two elements:
  1. A substring (`SUB`) representing the edge label leading from the parent to the current node. The root node will have the empty string (`''`) as its edge label.
  2. A dictionary (`CHILDREN`) mapping the first character in the child's edge label to node indices representing the node's children.
- **suf**: A string representing the suffix to be added to the suffix tree.

#### Operation
- The function iterates over the characters of `suf`.
- For each character, it checks if the character is already represented in the tree at the current node's children.
- If not, a new node is created for the remaining part of `suf`, and the process terminates for this suffix.
- If the character is found, the function compares the suffix with the substring of the found node to check how much of it matches.
- If a mismatch is found before the end of the node's substring, a new intermediate node is created to represent the common prefix, and the original node is split into two parts: the common prefix and the remaining substring.
- This process is repeated until the entire suffix has been processed.

#### Notes
- This function is called iteratively by `build_suffix_tree` for each suffix of the input text.
- The constants `CHILDREN` and `SUB` are assumed predefined indices or keys that correspond to the children dictionary and the substring part of a node, respectively.

---

### `build_suffix_tree(text)`

#### Purpose
The `build_suffix_tree` function constructs a suffix tree for a given input string `text`. It initializes the tree structure and iteratively adds each suffix of the text to the tree using the `add_suffix` function.

#### Parameters
- **text**: The input string for which the suffix tree is to be constructed.

#### Returns
A list of nodes representing the suffix tree of the input text. Each node is structured as described in the `add_suffix` function documentation.

#### Operation
- Appends a terminal symbol `$` to the end of `text` to mark the end of the string. This ensures that all suffixes are considered unique.
- Initializes the tree with a single root node having an empty substring and no children.
- Iterates over each index of `text`, treating each suffix starting from that index as a new suffix to be added to the tree.
- Calls `add_suffix` for each of these suffixes, passing the current state of the tree and the suffix.
- Returns the constructed suffix tree.

#### Notes
- The suffix tree structure allows for efficient search and analysis operations on the input text, such as finding substrings, repetitions, etc.
- The terminal symbol `$` is crucial for ensuring that no suffix is a prefix of another, simplifying the tree construction logic.

---

### `search_tree(suffix_tree, P)`

#### Purpose
The `search_tree` function searches for a pattern `P` within the suffix tree.

#### Operation
- Starting from the root, the function traverses the tree following the characters in `P`.
- At each node, it checks if the next part of the pattern matches the node's edge label.
- If a mismatch occurs at any point, the function returns that the pattern is not found.
- If the traversal successfully matches all characters of `P`, the pattern is considered found.

---

## Suffix Array

The suffix array is built from the suffix tree structure.

### `build_suffix_array(T)`

#### Purpose
Construct a sorted suffix array from the reference string `T` using the suffix tree.

#### Operation
- The function performs a depth-first search (DFS) of the suffix tree to extract the starting indices of all suffixes.
- The collected indices are then sorted to create the suffix array.
- This array can be used for further search operations on the reference text.

---

### `search_array(suffix_array, q)`

#### Purpose
Perform a binary search on the suffix array to locate a query pattern `q`.

#### Operation
- The binary search efficiently finds the location in the suffix array where the query pattern would fit.
- The function returns the index in the array corresponding to the query's match location.

---

## Suffix Trie

The suffix trie provides an alternative approach to index all suffixes of a string.

### `build_suffix_trie(s)`

#### Purpose
Construct a suffix trie for the string `s` by inserting every suffix into a nested dictionary structure.

#### Operation
- For each suffix starting from every index in `s`, traverse (or create) the nodes in the trie.
- Optionally, a terminal marker (e.g., `'#'`) is added to denote the end of each suffix.

---

### `search_trie(trie, pattern)`

#### Purpose
Search for a given `pattern` in the suffix trie.

#### Operation
- The function traverses the nested dictionary (trie) following the characters of `pattern`.
- It returns the number of consecutive characters (match length) that are found in the trie from the beginning of the pattern.

---

This repository now includes implementations for both suffix tree and suffix trie structures, along with their corresponding search functionalities and a suffix array construction from the tree. These data structures provide a strong foundation for aligning and analyzing reads against a reference sequence.

---
