# Intro to Trees in Python
- A tree is built of nodes as the other data structures, the only difference between them is that the three nodes can 
 point either to the left or right (Or as many we want).
- A node can be either a child or a parent so if the Node(n) is pointing to Node(z) and Node(x) n is parent of its 
  children x and z being called siblings.
- Every node can only have one parent!
- Child nodes can also be parent nodes.
- A node that has no children is called a leaf

# Types of Trees
* Full - A tree that's pointing to either Zero nodes or two of them on each level
* Perfect - A tree that's full and all levels are completely fulfilled so each node its point to two nodes
* Complete - A tree that's full left to right

# Binary Search Tree
  - To build a binary search tree we have to follow a straight rule that consist of if the node that we are going to add
    it's greater than the parent we place it at left of the tree else we place it at right, and so it goes recursively.
    ## Big O 
    - Each level of the tree is going to be approximately 2^level or O(log n) so being very efficient because we 
      are dividing and conquering the half of the tree that our item of search is placed based on it's value
    - The best case scenario would be a complete tree because we are breaking it in small half's
    - The worst case would be if we had a tree that only goes in one way so that's no dividing we are essentially going 
      through a linked list so the search is O(n) instead of O(log n)
    - All operations of a binary search tree we consider O(log n)

# Recursive methods
- We basically want to give to each recursion the pointer to the next node on the tree and update or insert values in it
- For deleting is simple but complicated, we have to be able to transverse the tree to find our node, then we drop the
  node from the tree, but just if it's a leaf node, if it's a parent node we have to put up the leaf that node was holding,
  and it gets more complicated when the leaf are holding two subtrees, then we have to go the right one and find the lower
  value that we can copy tho the node we are trying to drop and complete the tree again by dropping the lower value at the end.
