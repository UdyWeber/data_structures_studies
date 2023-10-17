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
