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
    * [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
    * [Binary Tree Postorder Traversal](#binary-tree-postorder-traversal)
    * [Average of Levels in Binary Tree](#average-of-levels-in-binary-tree)
  * [Medium](#binary-tree-medium)
    * [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
    * [Binary Tree Zigzag Level Order Traversal](#binary-tree-zigzag-level-order-traversal)
    * [Populating Next Right Pointers in Each Node](#populating-next-right-pointers-in-each-node)

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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/two_pointers/move_zeros.py" target="_blank">
          <code>move <br />zeros <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/two_pointers/two_sum.py" target="_blank">
          <code>two <br />sum <br />py </code>
        </a>
      </td>
      <td align="left">O(n logn). because of <a href="https://en.wikipedia.org/wiki/Timsort" target="_blank">Timsort</a>
      </td>
      <td align="left">O(n). n is the length of the tmp List.</td>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/two_pointers/two_sum_two.py" target="_blank">
          <code>two <br />sum <br />two <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/hash_table/two_sum.py" target="_blank">
          <code>two <br />sum <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/hash_table/integer_to_roman.py" target="_blank">
          <code>integer <br />to <br />roman <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/recursive_preorder_traversal.py" target="_blank">
          <code>recursive <br />preorder <br />traversal <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/iterative_preorder_traversal.py" target="_blank">
          <code>iterative <br />preorder <br />traversal <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/morris_traversal.py" target="_blank">
          <code>morris <br />traversal <br />py </code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/iterative_inorder_traversal.py" target="_blank">
          <code>iterative<br />inorder<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/recursive_inorder_traversal.py" target="_blank">
          <code>recursive<br />inorder<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/iterative_postorder_traversal.py" target="_blank">
          <code>iterative<br />postorder<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/recursive_postorder_traversal.py" target="_blank">
          <code>recursive<br />postorder<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/average_of_levels_order_traversal.py" target="_blank">
          <code>average<br />of<br />levels<br />order<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/level_order_traversal.py" target="_blank">
          <code>level<br />order<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/recursive_level_order_traversal.py" target="_blank">
          <code>recursive<br />level<br />order<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/iterative_zigzag_level_order_traversal.py" target="_blank">
          <code>iterative<br />zigzag<br />level<br />order<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/recursive_zigzag_level_order_traversal.py" target="_blank">
          <code>iterative<br />zigzag<br />level<br />order<br />traversal</code>
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
        <a href="https://github.com/Harmouch101/awesome-code/blob/main/solutions/binary_tree/populating_next_right_pointers_in_each_node.py" target="_blank">
          <code>populating<br />next<br />right<br />pointers</code>
        </a>
      </td>
      <td align="left">O(n).</td>
      <td align="left">O(1) by using pointers</td>
    </tr>
  </tbody>
</table>

## Contributing

You can open a pull request if you want!

## License

This project is licensed under the [MIT License](https://github.com/Harmouch101/awesome-code/blob/main/LICENSE).
