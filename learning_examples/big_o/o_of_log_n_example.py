# Imagine we have a list of 8 items
items = [1, 2, 3, 4, 5, 6, 7, 8]

# And we are trying to find the number 7 on this list
# In the O(n) way, we were going to iterate over this list and as the number of the length of the list is growing
# The number of operations we need to perform will grow with it, we would have to do 7 iterations to achieve our goal
# But if we cut it in half and were going to see if it's in the half's we cut, so
# we would have [1, 2, 3, 4,] & [5, 6, 7, 8] and we could remove the first one because 7 is not there,
# and then we would have [5, 6] & [7, 8] and finally we would have only [7] & [8] and we found our 7
# We performed 3 operations of cutting it in half, and we achieved the same goal
# This operation is called O(log n) cause it comes from 2^3 = 8, so we would have log sub 2 of 8 = 3
# That basically means 2 to what power is 8

