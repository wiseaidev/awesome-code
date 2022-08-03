<!-- MIT License

Copyright (c) 2022, wiseaidev
All rights reserved.
 -->

<div align="center">
    <a href="https://circleci.com/gh/wiseaidev/awesome-code/tree/main">
       <img src="https://circleci.com/gh/wiseaidev/awesome-code/tree/main.svg?style=svg"
       alt="CircleCI"/>
    </a>
    <a href="https://results.pre-commit.ci/latest/github/wiseaidev/awesome-code/main">
       <img src="https://results.pre-commit.ci/badge/github/wiseaidev/awesome-code/main.svg"
       alt="pre-commit.ci status"/>
    </a>
    <a href="https://github.com/wiseaidev/awesome-code">
       <img src="https://img.shields.io/badge/open_source-%F0%9F%A4%8D-3DA639.svg" alt="Open Source Love"/>
    </a>
    <a href="https://github.com/wiseaidev/awesome-code/blob/master/LICENSE">
       <img src="https://img.shields.io/github/license/wiseaidev/awesome-code" alt="License"/>
    </a>
    <a href="https://github.com/wiseaidev/awesome-code/">
       <img src="https://img.shields.io/github/repo-size/wiseaidev/awesome-code" alt="Repo Size"/>
    </a>
</div>

---

# Leetcode Python Solutions.

## 📜 Summary

This repository contains solutions to Leetcode problems. It will be updated regularly(Daily/Weekly). The primary reason for this repository is because I believe the best way to solve these problems is by dividing them into topics, each topic into difficulties, and solving at least one problem within each difficulty(quality > quantity). Such repositories are hard to find on the internet; this is the first one most likely. Therefore, I will gradually build this place to make it easier for beginners to learn algorithms by solving problems on leetcode by topics.

> Don't forget to slap that ⭐ button an odd number of times ;-)

> Currently maintained by [`Mahmoud Harmouch`](https://github.com/wiseaidev).

---

## Prerequisites

Basic understanding of the core language. If you are new to python, I highly recommend checking out the free learning material I compiled in the [`awesome-python`](https://github.com/wiseaidev/awesome-python) repository.

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
    * [Squares of a Sorted Array](#squares-of-a-sorted-array)
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
    * [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
    * [Binary Tree Postorder Traversal](#binary-tree-postorder-traversal)
    * [Average of Levels in Binary Tree](#average-of-levels-in-binary-tree)
  * [Medium](#binary-tree-medium)
    * [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
    * [Binary Tree Zigzag Level Order Traversal](#binary-tree-zigzag-level-order-traversal)
    * [Populating Next Right Pointers in Each Node](#populating-next-right-pointers-in-each-node)
* [Binary Search](#binary-search)
  * [Easy](#binary-search-easy)
    * [Find Smallest Letter Greater Than Target](#find-smallest-letter-greater-than-target)
    * [Binary Search](#binary-search-problem)
    * [First Bad Version](#first-bad-version)
    * [Search Insert Position](#search-insert-position)
    * [Sqrt(x)](#sqrtx)
  * [Medium](#binary-search-medium)
    * [Find Minimum in Rotated Sorted Array](#find-minimum-in-rotated-sorted-array)
    * [Find Peak Element](#find-peak-element)
    * [My Calendar I](#my-calendar-i)
  * [Hard](#binary-search-hard)
    * [Find Minimum in Rotated Sorted Array II](#find-minimum-in-rotated-sorted-array-ii)
* [String](#string)
  * [Easy](#string-easy)
    * [Longest Common Prefix](#longest-common-prefix)
    * [Reorder Data in Log Files](#reorder-data-in-log-files)
    * [Isomorphic Strings](#isomorphic-strings)
    * [Is Subsequence](#is-subsequence)
  * [Medium](#string-medium)
    * [Group Anagrams](#group-anagrams)
* [Linked List](#linked-list)
  * [Easy](#linked-list-easy)
    * [Reverse Linked List](#reverse-linked-list)
    * [Merge Two Sorted Lists](#merge-two-sorted-list)
  * [Medium](#linked-list-medium)
    * [Add Two Numbers](#add-two-numbers)
    * [Reorder List](#reorder-list)
* [Array](#array)
  * [Easy](#array-easy)
    * [Running Sum of 1d Array](#running-sum-of-1d-array)
    * [Find Pivot Index](#find-pivot-index)
  * [Medium](#array-medium)
    * [Search a 2D Matrix II](#search-a-2d-matrix-ii)
    * [Kth Smallest Element in a Sorted Matrix](#kth-smallest-element-in-a-sorted-matrix)

## [Two Pointers](https://leetcode.com/tag/two-pointers/) <a name="two-pointers"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="two-pointers-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">283. <a name="move-zeros"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/move-zeroes/" target="_blank">Move Zeroes</a>
      </td>
      <td align="left">
        <ul>
          <li>Use two consecutive pointers, the left one at the start of the list, the right one at start + 1.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/two_pointers/move_zeros.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n). The right pointer does not visit the same element twice.</td>
      <td align="left">O(1). All operations are made in-place.</td>
    </tr>
    <tr>
      <td align="left">1. <a name="two-sum"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/two_sum/" target="_blank">Two Sum</a>
      </td>
      <td align="left">
        <ul>
          <li>Sort the array and store it into a tmp variable.</li>
          <li>Use two pointers, the left one at the start of the list, the right one at the end of the list.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/two_pointers/two_sum.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n logn). because of <a href="https://en.wikipedia.org/wiki/Timsort" target="_blank">Timsort</a>
      </td>
      <td align="left">O(n). n is the length of the tmp List.</td>
    </tr>
    <tr>
      <td align="left">977. <a name="squares-of-a-sorted-array"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/squares-of-a-sorted-array/" target="_blank">Squares of a Sorted Array</a>
      </td>
      <td align="left">
        <ul>
          <li>The array is already sorted.</li>
          <li>Use two pointers, the left one at the start of the list, the right one at the end of the list.</li>
          <li>Compare the abs of the left and right elements.</li>
          <li>If abs_left is larger than abs_right, then:
            results[right - left] = abs_left * abs_left
            left += 1
          </li>
          <li>else:
            results[right - left] = abs_right * abs_right
            right -= 1
          </li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/two_pointers/squares_of_a_sorted_array.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n). A linear scan, n is the length of the results List
      </td>
      <td align="left">O(n). n is the length of the results List.</td>
    </tr>
  </tbody>
</table>

### Medium <a name="two-pointers-medium"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">167. <a name="two-sum-ii"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/" target="_blank">Two Sum II - Input Array Is Sorted</a>
      </td>
      <td align="left">
        <ul>
          <li>The array is already sorted.</li>
          <li>Use two pointers, the left one at the start of the list, the right one at the end of it.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/two_pointers/two_sum_two.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n). The right and left pointers do not visit the same element twice.</td>
      <td align="left">O(1). All operations are made in-place.</td>
    </tr>
  </tbody>
</table>

## [Hash Table](https://leetcode.com/tag/hash-table/) <a name="hash-table"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="hash-table-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">1. <a name="hash-table-two-sum"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/two-sum/" target="_blank">Two Sum</a>
      </td>
      <td align="left">
        <ul>
          <li>Create a hashmap which accepts integer datatype as key and value.</li>
          <li>Check if difference (element visited - target) is present in the hashmap.</li>
          <li>If present, return indexes as result.</li>
          <li>Otherwise, add the current element as key and its value as the current iteration</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/hash_table/two_sum.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n). One for loop, hashmap lookup ~ O(1)</td>
      <td align="left">O(n). Hash Table.</td>
    </tr>
  </tbody>
</table>

### Medium <a name="hash-table-medium"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">12. <a name="integer-to-roman"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/integer-to-roman/" target="_blank">Integer to Roman</a>
      </td>
      <td align="left">
        <ul>
          <li>Store the numbers from largest to smallest into a hashmap, aka dict.</li>
          <li>Keep dividing the given number by the numbers stored in the hashmap</li>
          <li>The quotient of division denotes how many times the current roman number appears in the end result</li>
          <li> Update the number by the reminder of the previous division.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/hash_table/integer_to_roman.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(k). k: length of the hash table.</td>
      <td align="left">O(n). n: length of the hash table + list.</td>
    </tr>
  </tbody>
</table>

## [Binary Tree](https://leetcode.com/tag/binary-tree) <a name="binary-tree"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="binary-tree-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">144. <a name="preorder-traversal"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/" target="_blank">Recursive Preorder Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>Add the current node onto the list.</li>
          <li>Traverse the left sub-tree, and keep adding the visited node.</li>
          <li>If root is None, stop traverse, and move to the right sub-tree.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/recursive_preorder_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(log n) ~ height/depth of the tree.</td>
    </tr>
    <tr>
      <td align="left">144.</td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/" target="_blank">Iterative Preorder Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>Use a stack(LIFO).</li>
          <li>Add the root node into a list.</li>
          <li>Visit right, then left nodes, and push onto the stack.</li>
          <li>Pop an element from the stack, add it into the list.</li>
          <li>Repeat the previous two steps until the stack is empty.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/iterative_preorder_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(log n) ~ height/depth of the tree.</td>
    </tr>
    <tr>
      <td align="left">144.</td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/" target="_blank">Morris Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>Preorder traversal without recursion and or stack.</li>
          <li>Push current.right rather than the current node. The None cases will handle themselves by the inner while loop.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/morris_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(1).</td>
    </tr>
    <tr>
      <td align="left">94. <a name="binary-tree-inorder-traversal"></a></td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-inorder-traversal/" target="_blank">Iterative Inorder Traversal</a>
      </td>
      <td align="left">
        <ul>
        <li>
        Push all the left children of root into the stack until there's no more nodes.
        </li>
        <li>
        Then pop from the stack which is called current.
        </li>
        <li>
        Add current to result list.
        </li>
        <li>
        Kepp calling push_all_left() on current's right child until stack is empty.
        </li></ul>
        </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/iterative_inorder_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(n), n number of nodes.</td>
    </tr>
    <tr>
      <td align="left">94.</td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-inorder-traversal/" target="_blank">Recursive Inorder Traversal</a>
      </td>
      <td align="left">
        <ul>
        <li>
        Keep visiting all the left nodes. Once finished, add the current node while visiting the right node.
        </li></ul>
        </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/recursive_inorder_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(log n) ~ height/depth of the tree.</td>
    </tr>
    <tr>
      <td align="left">145 <a name="binary-tree-postorder-traversal"></a></td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-postorder-traversal/" target="_blank">Iterative Postorder Traversal</a>
      </td>
      <td align="left">
        <ul>
        <li>
        Push all the left children of root into the stack until there's no more nodes.
        </li>
        <li>
        Then pop from the stack which is called current.
        </li>
        <li>
        Keep calling push_all_left() on current's right child until stack is empty.
        </li>
        <li>
        Add current to result list.
        </li></ul>
        </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/iterative_postorder_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(n), n number of nodes.</td>
    </tr>
    <tr>
      <td align="left">145.</td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-postorder-traversal/" target="_blank">Recursive Postorder Traversal</a>
      </td>
      <td align="left">
        <ul>
        <li>
        Keep visiting all the left nodes, then all the left of current.
        </li>
        <li>
        Once finished, add the current node while visiting the right node.
        </li>
        </ul>
        </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/recursive_postorder_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(log n) ~ height/depth of the tree.</td>
    </tr>
    <tr>
      <td align="left">637. <a name="average-of-levels-in-binary-tree"></a></td>
      <td align="left">
        <a href="https://leetcode.com/problems/average-of-levels-in-binary-tree/" target="_blank">Iterative Average of Levels in Binary Tree</a>
      </td>
      <td align="left">
        <ul>
        <li>Same as level order traversal, append the average value of each level nodes onto the list.
        </li>
        </ul>
        </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/average_of_levels_order_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n number of nodes.</td>
      <td align="left">O(n), n number of nodes.</td>
    </tr>
  </tbody>
</table>

### Medium <a name="binary-tree-medium"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">102. <a name="binary-tree-level-order-traversal"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">Level Order Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>Traverse tree level by level.</li>
          <li>Use a Queue/Deque to keep track of all the nodes of the next level before moving to the next level.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/level_order_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(n)</td>
    </tr>
    <tr>
      <td align="left">102.
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-level-order-traversal/" target="_blank">Recursive Level Order Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>Traverse tree level by level.</li>
          <li>Use a Deque to keep track of all the nodes of the next level before moving to the next level.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/recursive_level_order_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(logn)</td>
    </tr>
    <tr>
      <td align="left">103. <a name="binary-tree-zigzag-level-order-traversal"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" target="_blank">Iterative Zigzag Level Order Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>After doing level order traversal using recursion, we simply reverse the direction at alternate levels</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/iterative_zigzag_level_order_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(n)</td>
    </tr>
    <tr>
      <td align="left">103.
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" target="_blank">Recursive Zigzag Level Order Traversal</a>
      </td>
      <td align="left">
        <ul>
          <li>After doing level order traversal using recursion, we simply reverse the direction at alternate levels</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/recursive_zigzag_level_order_traversal.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(logn)</td>
    </tr>
    <tr>
      <td align="left">116. <a name="populating-next-right-pointers-in-each-node"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/populating-next-right-pointers-in-each-node/" target="_blank">Populating Next Right Pointers in Each Node</a>
      </td>
      <td align="left">
        <ul>
          <li>Using BFS to populate next pointers of each node with nodes that occur to its immediate right on the same level.</li><li>Since for each node, we require the right node on the same level, we will perform a right-to-left BFS instead of the standard left-to-right BFS.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_tree/populating_next_right_pointers_in_each_node.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(1) by using pointers</td>
    </tr>
  </tbody>
</table>


## [Binary Search](https://leetcode.com/tag/binary-search/) <a name="binary-search"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="binary-search-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">744. <a name="find-smallest-letter-greater-than-target"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/find-smallest-letter-greater-than-target" target="_blank">Find Smallest Letter Greater Than Target</a>
      </td>
      <td align="left">
        <ul>
          <li>Return letters[0] if letter at index 0 is larger than target.</li>
          <li>Return letters[0] if letter at index -1 is lower or equal to target.</li>
          <li>Perform a binary seach on the list for target.</li>
          <li>The condition of the while loop is left <= right.</li>
          <li>Check if mid element > target element, update right = mid_point - 1.</li>
          <li>else: left = mid_point + 1.</li>
          <li>Return letters[left]</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/smallest_letter_greater_than_target.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
    <tr>
      <td align="left">704. <a name="binary-search-problem"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-search/" target="_blank">Iterative Binary Search</a>
      </td>
      <td align="left">
        <ul>
          <li>Initialise two pointers: left = 0, right = length of the array - 1.</li>
          <li>While left <= right:</li>
          <li>Compare nums[mid] to target.</li>
          <li>If the target = nums[mid]: return mid.</li>
          <li>If target < nums[mid], continue the search on the left, right = mid - 1.</li>
          <li>Else continue the search on the right, left = mid + 1.</li>
          <li>If not found, return -1.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/iterative_binary_search.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
    <tr>
      <td align="left">704.</a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/binary-search/" target="_blank">Recursive Binary Search</a>
      </td>
      <td align="left">
        <ul>
          <li>Pass the array, two pointers, and the target to a function for reursive calls: binary_search(nums, left, right, target)</li>
          <li>Base case: if left > right: return - 1</li>
          <li>If the target = nums[mid]: return mid.</li>
          <li>If target < nums[mid], continue the search on the left, right = mid - 1: binary_search(nums,left , mid-1, target)</li>
          <li>Else continue the search on the right, return binary_search(nums,mid + 1 , right, target)</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/recursive_binary_search.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(log n). log n: The length of the binary tree.</td>
    </tr>
    <tr>
      <td align="left">278. <a name="first-bad-version"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/first-bad-version/" target="_blank">Iterative First Bad Version</a>
      </td>
      <td align="left">
        <ul>
          <li>Initialise two pointers: left = 1, right = n.</li>
          <li>While left <= right:</li>
          <li>check if isBadVersion(mid).</li>
          <li>If not isBadVersion(mid): continue the search on the right, left = mid + 1.</li>
          <li>Else continue the search on the left, right = mid - 1.</li>
          <li>return left</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/iterative_first_bad_version.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
    <tr>
      <td align="left">278.</a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/first-bad-version/" target="_blank">Recursive First Bad Version</a>
      </td>
      <td align="left">
        <ul>
          <li>Pass two pointers to a function for reursive calls: binary_search(left = 1, right = n)</li>
          <li>Base case: if left > right: return - 1</li>
          <li>if left == right: return left</li>
          <li>If the target = nums[mid]: return mid.</li>
          <li>if not isBadVersion(mid), continue the search on the right, return binary_search(mid + 1, right).</li>
          <li>Else continue the search on the left, return binary_search(left, mid).</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/recursive_first_bad_version.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(log n). log n: The length of the binary tree.</td>
    </tr>
    <tr>
      <td align="left">35. <a name="search-insert-position"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/search-insert-position/" target="_blank">Iterative Search Insert Position</a>
      </td>
      <td align="left">
        <ul>
          <li>Initialise two pointers, and a return value variable: left = 0, right = length of the array - 1, ret_val = 0.</li>
          <li>Compare nums[mid] to target.</li>
          <li>If the target = nums[mid]: return mid.</li>
          <li>If target < nums[mid], continue the search on the left, right = mid - 1.</li>
          <li>Else continue the search on the right, left = mid + 1, and set ret_val = left. </li>
          <li>return ret_val.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/iterative_search_insert_position.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
    <tr>
      <td align="left">35.</a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/search-insert-position/" target="_blank">Recursive Search Insert Position</a>
      </td>
      <td align="left">
        <ul>
          <li>pass the array, two pointers, target, and a ret_val to a function for reursive calls: binary_search(nums, left, right, target, ret_val)</li>
          <li>Base case: if left > right: return ret_val</li>
          <li>If the target = nums[mid]: return mid.</li>
          <li>If target < nums[mid], continue the search on the left, right = mid - 1: binary_search(nums,left , mid-1, target)</li>
          <li>Else set ret_val = mid + 1, and continue the search on the right, return binary_search(nums,mid + 1 , right, target)</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/recursive_search_insert_position.py.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(log n). log n: The length of the binary tree.</td>
    </tr>
    <tr>
      <td align="left">69. <a name="sqrtx"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/sqrtx/" target="_blank">Sqrt(x)</a>
      </td>
      <td align="left">
        <ul>
          <li>Use two pointers <code>left, right= 0, number</code>.</li>
          <li>The condition of the while loop is <code>left <= right</code>.</li>
          <li>Check if <code>mid * mid <= number < (mid + 1) * (mid + 1)</code>, return mid.</li>
          <li>Check if <code>number < mid * mid </code>, set right to mid.</li>
          <li>else, set left to mid.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/sqrt_x.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: given number.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
  </tbody>
</table>

### Medium <a name="binary-search-medium"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">153. <a name="find-minimum-in-rotated-sorted-array"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">Find Minimum in Rotated Sorted Array</a>
      </td>
      <td align="left">
        <ul>
          <li>Check if the array is sorted but not rotated, return the first element.</li>
          <li>Perform a binary seach on the list.</li>
          <li>The condition of the while loop is left < right.</li>
          <li>Check if mid element > right element, update left = mid_point + 1.</li>
          <li>else: right = mid_point.</li>
          <li>Return min(nums[left], nums[right]).</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/find_minimum_in_rotated_sorted_array.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
    <tr>
      <td align="left">162. <a name="find-peak-element"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/find-peak-element/" target="_blank">Find Peak Element</a>
      </td>
      <td align="left">
        <ul>
          <li>Perform a binary seach on the list.</li>
          <li>The condition of the while loop is left < right.</li>
          <li>Check if mid element < mid element + 1, update left = mid_point + 1.</li>
          <li>else: right = mid_point.</li>
          <li>Return left.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/find_peak_element.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
    <tr>
      <td align="left">729. <a name="my-calendar-i"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/my-calendar-i/" target="_blank">My Calendar I</a>
      </td>
      <td align="left">
        <ul>
          <li>Check if it is possible to insert an interval when possible by performing a binary seach on the calendar.</li>
          <li>The condition of the while loop is left < right.</li>
          <li>Check if target <= nums[mid][0], update right = mid.</li>
          <li>else: left = mid + 1.</li>
          <li>Return left.</li>
          <li>Check if index > 0 and self.calendar[index-1][1] > start, return False</li>
          <li>Check if index < len(self.calendar) and end > self.calendar[index][0], return False</li>
          <li>Insert into calender: self.calendar.insert(index, [start, end])</li>
          <li>return True</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/my_calendar_i.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
  </tbody>
</table>

### Hard <a name="binary-search-hard"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">154. <a name="find-minimum-in-rotated-sorted-array-ii"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/" target="_blank">Find Minimum in Rotated Sorted Array II</a>
      </td>
      <td align="left">
        <ul>
          <li>Same as Find Minimum in Rotated Sorted Array.</li>
          <li>The only difference is that we can have duplicates.</li>
          <li>Therefore we need to update left += 1, and right += 1, instead of mid.</li>
          <li>Example, [5,5,0,5,5,5,5]</li>
          <li>Return nums[left]</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/binary_search/find_minimum_in_rotated_sorted_array_two.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(log n). n: length of the list.</td>
      <td align="left">O(1). pointers.</td>
    </tr>
  </tbody>
</table>

## [String](https://leetcode.com/tag/string/) <a name="string"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="string-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">14. <a name="longest-common-prefix"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/longest-common-prefix/" target="_blank">Longest Common Prefix</a>
      </td>
      <td align="left">
        <ul>
          <li>Horizontal scanning.</li>
          <li>Assign the first element of the list as the common prefix.</li>
          <li>Iterate over the list.</li>
          <li>Test if all characters match the second string.</li>
          <li>If not, remove a letter from the end of the string(first element of the list.).</li>
          <li>If matches, continue untill you find the common prefix amoung all strings.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/string/longest_common_prefix.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n is the length of the array.</td>
      <td align="left">O(1). constant length of the prefix.</td>
    </tr>
    <tr>
      <td align="left">14. <a name="reorder-data-in-log-files"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/reorder-data-in-log-files/" target="_blank">Reorder Data in Log Files</a>
      </td>
      <td align="left">
        <ul>
          <li>We define a tuple of 3 keys, (key_1, key_2, key_3), as follows:</li>
          <li>key_1: this key serves as a indicator for the type of logs. For the letter-logs, we could assign its key_1 with 0, and for the digit-logs, we assign its key_1 with 1.</li>
          <li>key_2: for this key, we use the content of the letter-logs as its value.</li>
          <li>key_3: similarly with the key_2, this key serves to further order the letter-logs.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/string/reorder_data_in_log_files.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(m n logn). because of <a href="https://en.wikipedia.org/wiki/Timsort" target="_blank">Timsort. m the for the comparison between two keys.</a></td>
      <td align="left">O(m n) to keep the keys for the log.</td>
    </tr>
    <tr>
      <td align="left">205. <a name="isomorphic-strings"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/isomorphic-strings/" target="_blank">Isomorphic Strings</a>
      </td>
      <td align="left">
        <ul>
          <li>Simultaneously, loop over the two strings s and t.</li>
          <li>Map each char in s to a char in t only if a new char of t not in values of dict/map. Example: <code>s = "badc", t = "baba", dict = {'b' : 'b', 'a': 'a', ...}</code></li>
          <li>If the current char of s not in dict, and the current char of t in values of dict, return False.</li>
          <li>If the current char of s in dict, and the value of key of s char is not equal to the current char of t, return False.</li>
          <li>return True.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/string/isomorphic_strings.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n: length of the input string.</td>
      <td align="left">O(1), because the number of ASCII chars is constant, <code>man ascii</code></td>
    </tr>
    <tr>
      <td align="left">205. <a name="isomorphic-strings"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/is-subsequence/" target="_blank">Is Subsequence</a>
      </td>
      <td align="left">
        <ul>
          <li>Loop over all chars in t.</li>
          <li>If the current char of t is equal to the char of s at index pointer, increase pointer.</li>
          <li>If pointer is equal to the length of s, break.</li>
          <li>Return True if pointer is equal to the length of s, False otherwise.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/string/is_subsequence.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(1).</td>
    </tr>
  </tbody>
</table>

### Medium <a name="string-medium"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">154. <a name="group-anagrams"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">Group Anagrams</a>
      </td>
      <td align="left">
        <ul>
          <li>Maintain a map result : {str: list[str]} where each key K is a sorted string, and each value is the list of strings from the initial input that when sorted, are equal to K.</li>
          <li>Eample: strs_input = ["are", "bat", "ear", "code", "tab", "era"] <br> result = {'aer'): ['are', 'ear', 'era'], ...}</li>
          <li>Itertate over the list of strings.</li>
          <li>Converts each string into a sorted tuple.</li>
          <li>Store the previous tuple as a key into the dict whos value the string itself.</li>
          <li>Once finished, return the values of the dict.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/string/group_anagrams.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(N K log⁡ K), N is the length of strs, and K is the maximum length of a string in strs.</td>
      <td align="left">O(N K), N strings, K is the maximum length of a string in strs.</td>
    </tr>
  </tbody>
</table>

## [Linked List](https://leetcode.com/tag/linked-list/) <a name="linked-list"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="linked-list-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">206. <a name="reverse-linked-list"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">Iterative Reverse Linked List</a>
      </td>
      <td align="left">
        <ul>
          <li>Maintain three variables, current node, head, previous node.</li>
          <li>Iterate the head through the list is done using the following instruction: head.next = head.</li>
          <li>But, we need to store the head before moving to the next node using the variable current = head.</li>
          <li>Move the current point to the previous node; this way, the list is being reversed.</li>
          <li>Assign the presvious node to current node.</li>
          <li>Keep iterating until head point to None.</li>
          <li>Return previous node as the new head for our reversed LinkedList.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/iterative_reverse_linked_list.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n denotes the size of the linked list.</td>
      <td align="left">O(1), Operations are made in-place.</td>
    </tr>
    <tr>
      <td align="left">206.</a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">Recursive Reverse Linked List</a>
      </td>
      <td align="left">
        <ul>
          <li>Return the pointer of next node to its previous node and then make the previous node as the next node of returned node and then return the current node.</li>
          <li>We first traverse till the last node and making the last node as the head node of reversed linked list and then applying the above procedure in the recursive manner.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/recursive_reverse_linked_list.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n denotes the size of the linked list.</td>
      <td align="left">O(n), n denotes the size of the linked list.</td>
    </tr>
    <tr>
      <td align="left">206.
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">Stack Iterative Reverse Linked List</a>
      </td>
      <td align="left">
        <ul>
          <li>Traverse the list and push all of its nodes onto a stack.</li>
          <li>Traverse the list from the head node again and pop a value from the stack top and connect them in reverse order.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/stack_iterative_reverse_linked_list.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n denotes the size of the linked list.</td>
      <td align="left">O(n), n denotes the size of the linked list.</td>
    </tr>
    <tr>
      <td align="left">21. <a name="merge-two-sorted-list"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">Iterative Merge Two Sorted Lists</a>
      </td>
      <td align="left">
        <ul>
          <li>Create two dummy nodes, <code>current = dummy = ListNode()</code></li>
          <li>Simultaneously, Traverse both lists.</li>
          <li>Compare the values of the current nodes from both lists.</li>
          <li>Assign the next node of current to the node that has the minimum value.</li>
          <li>Assign list to list.next.</li>
          <li>Assign current to list</li>
          <li>return <code>dummy.next</code></li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/iterative_merge_two_sorted_lists.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n denotes the size of a linked list.</td>
      <td align="left">O(n), n denotes the size of a linked list.</td>
    </tr>
    <tr>
      <td align="left">21.
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">Recursive Merge Two Sorted Lists</a>
      </td>
      <td align="left">
        <ul>
          <li>Base case: if one of the lists is empty, return either lists.</li>
          <li>Compare the values of the current nodes from both lists.</li>
          <li>Assign the next node of current to the node that has the minimum value.</li>
          <li>Assign list.next to either <code>mergeTwoLists(list.next, list)</code> or <code>mergeTwoLists(list, list.next)</code>.</li>
          <li>return either lists</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/recursive_merge_two_sorted_lists.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n denotes the size of a linked list.</td>
      <td align="left">O(n), n denotes the size of a linked list.</td>
    </tr>
  </tbody>
</table>

### Medium <a name="linked-list-medium"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">2. <a name="add-two-numbers"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/add-two-numbers/" target="_blank">Add Two Numbers</a>
      </td>
      <td align="left">
        <ul>
          <li>Initialize current node to dummy head of the returning list.</li>
          <li>Initialize carry to 0.</li>
          <li>Initialize dummy_head current_head.</li>
          <li>Loop through lists l1 and l2 until you reach both ends.</li>
          <li>Get the values from the linkedLists.</li>
          <li>Move heads to the next node.</li>
          <li>Check if carry > 0, if so append a new node with value carry to the returning list.</li>
          <li>Return dummy head's next node because we initialized the dummy_head with a value 0.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/add_two_numbers.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(max⁡(m,n)) where m and n represents the length of l1 and l2 respectively.</td>
      <td align="left">O(max⁡(m,n)) The length of the new list is at most max⁡(m,n)+1.</td>
    </tr>
    <tr>
      <td align="left">143. <a name="reorder-list"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/reorder-list" target="_blank">Reorder List</a>
      </td>
      <td align="left">
        <ul>
          <li>Find the middle of or list - be careful, it needs to work properly both for even and for odd number of nodes. we can use slow/fast iterators trick, where slow moves with speed 1 and fast moves with speed 2</li>
          <li>Reverse the second part of linked list. The idea is to keep three pointers: prev, curr, nextt stand for previous, current and next and change connections in place.</li>
          <li>Finally, we need to merge two lists, given its heads. Interchange nodes: we put head2 as next element of head1 and then say that head1 is now head2 and head2 is previous head1.next.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/linked_list/recursive_reverse_linked_list.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n denotes the size of the linked list.</td>
      <td align="left">O(1).</td>
    </tr>
  </tbody>
</table>

## [Array](https://leetcode.com/tag/array/) <a name="array"></a>

#### 🔝 [Go To TOC](#TOC).

### Easy <a name="array-easy"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">1480. <a name="running-sum-of-1d-array"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/running-sum-of-1d-array/" target="_blank">Running Sum of 1d Array</a>
      </td>
      <td align="left">
        <ul>
          <li>Iterate over the list.</li>
          <li>Add nums[i] to nums[i - 1] and assign the result to nums[i].</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/array/running_sum_of_1d_array.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n is the length of the array.</td>
      <td align="left">O(1). Operations are made in place.</td>
    </tr>
    <tr>
      <td align="left">724. <a name="find-pivot-index"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/find-pivot-index/" target="_blank">Find Pivot Index</a>
      </td>
      <td align="left">
        <ul>
          <li>Set the left and the right sums to 0 and sum(nums) respectively.</li>
          <li>Subtract nums[i] from the right sum.</li>
          <li>Test if left_sum == right_sum, then return.</li>
          <li>else, add nums[i] to the left sum.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/array/find_pivot_index.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(n), n is the length of the array.</td>
      <td align="left">O(1). Operations are made in place.</td>
    </tr>
  </tbody>
</table>

### Medium <a name="array-mediun"></a>

<table>
  <tbody>
    <tr>
      <th align="center">#</th>
      <th align="center">Problem Statement</th>
      <th align="center">Notes</th>
      <th align="center">Solution</th>
      <th align="center">Time Complexity</th>
      <th align="center">Space Complexity</th>
    </tr>
    <tr>
      <td align="left">240. <a name="search-a-2d-matrix-ii"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/search-a-2d-matrix-ii/" target="_blank">Search a 2D Matrix II</a>
      </td>
      <td align="left">
        <ul>
          <li>Start iterating from bottom left corner with two pointers: <code>bottom, left = nb_rows-1, 0</code>.</li>
          <li>If target is larger then current element, then go right by incrementing the left pointer by one.</li>
          <li>If target is smaller then current element, then go up by decrementing the bottom pointer by one.</li>
          <li>If target is equal to the current element, then return True.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/array/search_a_2d_matrix_ii.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(m+n), m, n are the number of columns and rows in the array.</td>
      <td align="left">O(1). Operations are made in place.</td>
    </tr>
    <tr>
      <td align="left">378. <a name="kth-smallest-element-in-a-sorted-matrix"></a>
      </td>
      <td align="left">
        <a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/" target="_blank">Kth Smallest Element in a Sorted Matrix</a>
      </td>
      <td align="left">
        <ul>
          <li>Set two pointers: <code>left = matrix[0][0]</code> (top left), and <code>right = matrix[n-1][n-1]</code> bottom right.</li>
          <li>Search for the mid of left and right, The mid is NOT necessarily an element in the matrix.</li>
          <li>If <code>countLessOrEqual(mid) >= k</code>, we keep current <code>ans = mid</code> and try to find smaller value by searching in the left side. Otherwise, we search in the right side.</li>
          <li>Since ans is the smallest value which <code>countLessOrEqual(ans) >= k</code>, so it's the <code>kth</code> smallest element in the matrix.</li>
        </ul>
      </td>
      <td align="left">
        <a href="https://github.com/wiseaidev/awesome-code/blob/main/solutions/array/kth_smallest_element_in_a_sorted_matrix.py" target="_blank">
          <code>file</code>
        </a>
      </td>
      <td align="left">O(m+n), m, n are the number of columns and rows in the array.</td>
      <td align="left">O(1). Operations are made in place.</td>
    </tr>
  </tbody>
</table>

## Contributing

You can open a pull request if you want!

## License

This project is licensed under the [MIT License](https://github.com/wiseaidev/awesome-code/blob/main/LICENSE).
