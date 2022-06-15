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
       <img src="https://img.shields.io/badge/open_source-%F0%9F%A4%8D-3DA639.svg?style=for-the-badge&logoColor=blue&color=black" alt="Open Source Love"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-code/blob/master/LICENSE">
       <img src="https://img.shields.io/github/license/Harmouch101/awesome-code?style=for-the-badge&logoColor=blue&color=black" alt="License"/>
    </a>
    <a href="https://github.com/Harmouch101/awesome-code/">
       <img src="https://img.shields.io/github/repo-size/Harmouch101/awesome-code?style=for-the-badge&logoColor=blue&color=black" alt="Repo Size"/>
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
python -c "import this" | grep simple
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
* [Hash Map](#hash-table)
  * [Easy](#hash-table-easy)
    * [Two Sum](#two-sum)

## [Two Pointers](https://leetcode.com/tag/two-pointers/) <a name="two-pointers"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="two-pointers-easy"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 0 <a name="move-zeros"></a> | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) |  <ul><li>Use two consecutive pointers, the left one at the start of the list, the right one at start + 1.<br/>| [`move_zeros.py`](./solutions/two_pointers/move_zeros.py) | O(n). The right pointer does not visit the same element twice. | O(1). All operations are made in-place. |
| 1 <a name="two-sum"></a> | [1. Two Sum](https://leetcode.com/problems/two_sum/) | <ul><li>Sort the array and store it into a tmp variable.</li><li>Use two pointers, the left one at the start of the list, the right one at the end of the list.</li><li>Use two pointers, the left one at the start of the list, the right one at the end of it.</li></ul>| [`two_sum.py`](./solutions/two_pointers/move_zeros.py) | O(n logn). because of [Timsort](https://en.wikipedia.org/wiki/Timsort) | O(1). All operations are made in-place. |

#### 🔝 [Go To TOC](#TOC).

### Medium <a name="two-pointers-medium"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 0 <a name="two-sum-ii"></a> | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | <ul><li>The array is already sorted.</li><li>Use two pointers, the left one at the start of the list, the right one at the end of it.</li></ul>  | [`move_zeros.py`](./solutions/two_pointers/two_sum_two.py) | O(n). The right and left pointers do not visit the same element twice. | O(1). All operations are made in-place. |

## [Hash Table](https://leetcode.com/tag/hash-table/) <a name="hash-table"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="hash-table-easy"></a>

| # | Problem Statement | Notes | Solutions | Time Complexity  | Space Complexity |
| :---:| :---: | :---:  | :---:     |  :---:  | :---: |
| 0 <a name="two-sum"></a> | [1. Two Sum](https://leetcode.com/problems/two-sum/) | <ul><li>Create a hashmap which accepts integer datatype as key and value.</li><li>Check if difference (element visited - target) is present in the hashmap.</li><li>If present, return indexes as result.</li><li>Otherwise, add the current element as key and its value as the current iteration</li></ul> | [`two_sum.py`](./solutions/hash_table/two_sum.py) | O(n). One for loop, hashmap lookup ~ O(1) | O(n). Hash Table. |

## Contributing

You can open a pull request if you want!

## License

This project is licensed under the [MIT License](https://github.com/Harmouch101/awesome-code/blob/main/LICENSE).
