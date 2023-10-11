# Intro to Heaps
- It's a binary tree, but the nodes are organized in a way that the higher value stays at the top
- It is a complete tree, meaning that's filled left to right on each level with no gaps
- The height of the tree is O(log n)
- Instead of a binary search tree, a heap can have duplicates
- You can have max heaps that put the maximum value at the top and min heaps that put the minimum value at the top
- The tree has no ordering other than the maximum or minimum values being at the top of each other depending on the rule
- Heaps are not good for searching, you only use them to keep track of the biggest value at the top and quickly be able
  to remove it
- We are going to store the heap as a list, and it only stores integers the greater value being at index 1 leaving a gap
  in the index 0 to facilitate the math to manipulate the values into the heap
- To search for the children of a value the math would be `left_child = 2 * parent index` and 
  `right_child = 2 * child index + 1`.
- To search for the parent of a given child we are only going to divide it by 2
- To insert a value into a heap we first append it to the list, and then we analyze if it is a valid heap if it isn't we
  compare and move the values till the tree follows the rule of the parents being greater or equal than it's children
- Doing an insert or remove on a heap is O(log n)
- A priority Queue can be implemented using BinarySearchTrees or LinkedLists, but we use a heap to implement it more often
  because to search for the highest priority in a linked list and an unbalanced BST are both O(n), making implementing it
  on a heap more efficient, because on Max Heap the max priority item is always at the top.
