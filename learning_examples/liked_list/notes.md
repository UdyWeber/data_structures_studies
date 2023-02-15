# LIKED LIST INTRO
  - Liked Lists are a data structure that is mixed up in memory but with nodes pointing to each other that makes it easy
    to map and index all nodes for the liked list

# IMPORTANT CONCEPTS
  - Liked lists are composed of Nodes the first node being the head that is pointing to the next and the next points to
    the last that's called tail and as it is the end of the list tail is pointing to None

# BIG O FOR LIKED LIST METHODS
  - Append: We will have the tail pointing to a new node, and tail now will be our new node, that's O(1), because it
    doesn't matter the number of nodes we have the node being added at the end of the list will be always one operation
  - Pop: We will have the tail removed from the liked list, so we will have no pointer pointing to 
    the item that's before the last tail, so we have to iterate through the list to find it, making it O(n)
  - Add to the front: We will have one new node pointing to our actual head, so we have to point new node to head and
    define it as head that's O(1)
  - Remove the head: We will say that head is equal head.next() pointing head to our second node that now will be the first
    by that we can simply remove the node that's pointing to our head, and that's O(1)
  - Insert: In order to insert a new node to an index we have to find by iterating the list the pointer that points to that index, 
    point our new node to the same point on memory and after that point the pointer that was pointing to the indexed node
    to our new node, and that's how we insert a new node, but as we had to iterate the list that's O(n)
  - Removing from Index: Is almost the same as inserting a value, but we will point our pointer that is pointing 
    to the item that we are removing, to the pointer of this item, so we can just remove it from the list
  - Finding Value: To Find a value into a linked list we have to iterate through the list and check if the value of the
    node is the value that we want, if it's not, the iteration continues, that's O(n)

# COMPARING LIST AND LINKED LIST
    METHOD        ---List--- ---LinkedList---
    Append           O(1)        O(1)
    Pop              O(n)        O(1)
    Prepend          O(1)        O(n)
    Pop First        O(1)        O(n)
    Insert           O(n)        O(n)
    Remove           O(n)        O(n)
    LookUp by index  O(n)        O(1)
    LookUp by value  O(n)        O(n)