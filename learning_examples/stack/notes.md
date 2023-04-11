# Introduction to Stack in Python
  - Stacks use the LIFO mechanism (last in first out) where, as you keep adding to the stack the items will pile up,
    in order to remove the item that is in the bottom of the stack you have to remove all the previous items added
  - When we are going to add or remove items from the stack we are performing a O(n) operation cause we have to add/remove
    then we have to reindex all the other items that were in the stack
  - When building a stack you have to think of it as a linked list but vertically instead of horizontally, so you're adding
    items in the top where it is accessible and removing only from the top
