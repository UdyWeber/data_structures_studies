# Bubble Sort
- In bubble sort we run through the list values and compare each of them individually using 2 loops, so it's O(n^2)

# Selection Sort
- In selection sort we chose each time the minimum value index per iteration to be swapped with the first index of the 
  iteration
- As we use two nested loops it is also O(n^2)

# Insertion Sort
- In the worst case scenario it is O(n^2) because we have nested loops just like the other ones.
- In insertion sort we run through the list values and move the value if the j is lower than i and continue to do so if
  j still smaller than j - 1
- But if we have an almost sorted list the number of operations decreases a lot so in the base case scenario the time is O(n)

# Sleep Sort
- Using asynchronous tasks we are able to perform sleeps in separated threads, when the sleep is over we can add the values
  to a given list and print it out.

# Merge Sort
- We are going to divide and conquer a given unsorted list into smaller ones, then we are going to merge them together 
  until the values are sorted.
- Merge sort uses a helper function called merge, which takes to sorted lists and merges them into a single list, it 
  achieves that by comparing lists values and adding the smaller into a new list until one list is empty, and with the 
  remaining items, we just append it to the new list.
- All the sorting function relies on recursion, so each list division is divided again until it reaches one node and 
  starts to pop the callstack going back and reuniting the values using merge which combines them in a sorted list
- Unlike the other sorting algorithms, merge sort doesn't sort the list in place, in fact it returns a new sorted list
  and the original list stays untouched. 
  
  ## Big O
  - Space complexity: O(n) because we break a big list into smaller ones so increasing the memory usage
  - Time complexity:
    - Breaking lists apart: O(log n) because we are decreasing exponentially the number of elements on the list
    - Merging them together: O(n) because we have to iterate over all the elements and sort them into a new list
  - So the final big O for merge sort would be O(n log n) which is way more efficient than the previous ones, that were
    O(n^2)
