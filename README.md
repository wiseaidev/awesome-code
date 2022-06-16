<!-- MIT License

Copyright (c) 2022, Harmouch101
All rights reserved.
 -->

<div align="center">
    <a href="https://circleci.com/gh/Harmouch101/awesome-code/tree/main">
       <img src="https://circleci.com/gh/Harmouch101/awesome-code/tree/main.svg?style=svg"
       alt="CircleCI"/>
    </a>
    <a href="https://results.pre-commit.ci/latest/github/Harmouch101/awesome-code/main">
       <img src="https://results.pre-commit.ci/badge/github/Harmouch101/awesome-code/main.svg"
       alt="pre-commit.ci status"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-code">
       <img src="https://img.shields.io/badge/open_source-%F0%9F%A4%8D-3DA639.svg" alt="Open Source Love"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-code/blob/master/LICENSE">
       <img src="https://img.shields.io/github/license/Harmouch101/awesome-code" alt="License"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-code/">
       <img src="https://img.shields.io/github/repo-size/Harmouch101/awesome-code" alt="Repo Size"/>
    </a>
</div>

---

# Leetcode Python Solutions.

## 📜 Summary

This repository contains solutions to Leetcode problems. It will be updated regularly(Daily/Weekly). The primary reason for this repository is because I believe the best way to solve these problems is by dividing them into topics, each topic into difficulties, and solving at least one problem within each difficulty(quality > quantity). Such repositories are hard to find on the internet; this is the first one most likely. Therefore, I will gradually build this place to make it easier for beginners to learn algorithms by solving problems on leetcode by topics.

> Don't forget to slap that ⭐ button an odd number of times ;-)

> Currently maintained by [`Mahmoud Harmouch`](https://github.com/Harmouch101).

---

## Prerequisites

Basic understanding of the core language. If you are new to python, I highly recommend checking out the free learning material I compiled in the [`awesome-python`](https://github.com/Harmouch101/awesome-python) repository.

```sh
python -c "import this" | grep Simple
```

```sh
Simple is better than complex.
```

---

## 👉 Table Of Content (TOC). <a name="TOC"></a>

* [Two Pointers](#two-pointers)
  * [Easy](#two-pointers-easy)
    * [Move Zeros](#move-zeros)
    * [Two Sum](#two-sum)
  * [Medium](#two-pointers-medium)
    * [Two Sum II](#two-sum-ii)
* [Hash Table](#hash-table)
  * [Easy](#hash-table-easy)
    * [Two Sum](#hash-table-two-sum)
  * [Medium](#hash-table-medium)
    * [Integer to Roman](#integer-to-roman)
* [Binary Tree](#binary-tree)
  * [Easy](#binary-tree-easy)
    * [Binary Tree Preorder Traversal](#preorder-traversal)

## [Two Pointers](https://leetcode.com/tag/two-pointers/) <a name="two-pointers"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="two-pointers-easy"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 283. <a name="move-zeros"></a> | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) |  <ul><li>Use two consecutive pointers, the left one at the start of the list, the right one at start + 1.</li></ul>| [`move_zeros.py`](./solutions/two_pointers/move_zeros.py) | O(n). The right pointer does not visit the same element twice. | O(1). All operations are made in-place. |
| 1. <a name="two-sum"></a> | [Two Sum](https://leetcode.com/problems/two_sum/) | <ul><li>Sort the array and store it into a tmp variable.</li><li>Use two pointers, the left one at the start of the list, the right one at the end of the list.</li></ul>| [`two_sum.py`](./solutions/two_pointers/two_sum.py) | O(n logn). because of [Timsort](https://en.wikipedia.org/wiki/Timsort) | O(n). Because of the tmp List |

### Medium <a name="two-pointers-medium"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 167. <a name="two-sum-ii"></a> | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | <ul><li>The array is already sorted.</li><li>Use two pointers, the left one at the start of the list, the right one at the end of it.</li></ul>  | [`two_sum_two.py`](./solutions/two_pointers/two_sum_two.py) | O(n). The right and left pointers do not visit the same element twice. | O(1). All operations are made in-place. |

## [Hash Table](https://leetcode.com/tag/hash-table/) <a name="hash-table"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="hash-table-easy"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 1. <a name="hash-table-two-sum"></a> | [Two Sum](https://leetcode.com/problems/two-sum/) | <ul><li>Create a hashmap which accepts integer datatype as key and value.</li><li>Check if difference (element visited - target) is present in the hashmap.</li><li>If present, return indexes as result.</li><li>Otherwise, add the current element as key and its value as the current iteration</li></ul> | [`two_sum.py`](./solutions/hash_table/two_sum.py) | O(n). One for loop, hashmap lookup ~ O(1) | O(n). Hash Table. |

### Medium <a name="hash-table-medium"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 12. <a name="integer-to-roman"></a> | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | <ul><li>Store the numbers from largest to smallest into a hashmap, aka dict.</li><li>Keep dividing the given number by the numbers stored in the hashmap</li>><li>The quotient of division denotes how many times the current roman number appears in the end result</li><li> Update the number by the reminder of the previous division.</li></ul> | [`integer_to_roman.py`](./solutions/hash_table/integer_to_roman.py) | O(k). k: length of the hash table. | O(n). n: length of the hash table + list. |

## [Binary Tree](https://leetcode.com/tag/binary-tree) <a name="binary-tree"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="binary-tree-easy"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 144. <a name="preorder-traversal"></a> | [Recursive Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |  <ul><li>Add the current node onto the list.</li><li>Traverse the left sub-tree, and keep adding the visited node.</li><li>If root is None, stop traverse, and move to the right sub-tree.</li></ul>| [`recursive_preorder_traversal.py`](./solutions/binary_tree/recursive_preorder_traversal.py) | O(n), n number of nodes | O(log n) ~ height of the tree. |
| 144. <a name="preorder-traversal"></a> | [Iterative Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |  <ul><li>Use a stack(LIFO).</li><li>Add the root node into a list.</li><li>Visit right, then left nodes, and push onto the stack.</li><li>Pop an element from the stack, add it into the list.</li><li>Repeat the previous two steps until the stack is empty.</li></ul>| [`iterative_preorder_traversal.py`](./solutions/binary_tree/iterative_preorder_traversal.py) | O(n), n number of nodes | O(log n) ~ height of the tree. |
| 144. <a name="preorder-traversal"></a> | [Morris Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |  <ul><li>Preorder traversal without recursion and or stack.</li><li>Push current.right rather than the current node. The None cases will handle themselves by the inner while loop.</li></ul>| [`morris_traversal.py`](./solutions/binary_tree/morris_traversal.py) | O(n), n number of nodes | O(1) |

## Contributing

You can open a pull request if you want!

## License

This project is licensed under the [MIT License](https://github.com/Harmouch101/awesome-code/blob/main/LICENSE).
