# INTRO TO BIG O
Big O is a way of comparing code efficiency mathematically
  - Time complexity for Big O is not measured in Time, cause if a program takes 10 seconds to Run if I ran it on a
    computer twice as fast it will complete it twice as fast.
  - What's taken into measuring is the actual number of operations that a code does to complete its task.
  - Another factor to be considered is the Space Complexity, that looks for the amount of memory a code uses to
    run the same task as others.
  - Both of these factors are important to measuring the Big O complexity, but you need to be sure what results you
    mean to achieve.

# IMPORTANT UNDERSTANDINGS
  - While working with Big O there are 3 greek letters that will appear
    - Omega(Ω)
      - Best Case Scenario for Big O
    - Theta(Θ)
      - Average Case Scenario for Big O
    - Omicron(Ο)
      - Worst Case Scenario for Big O
  - When talking about Big O we are always talking about the worst case that is happening or will happen   

  - Examples:
    Will have to iterate over a list of [1, 2, 3, 4, 5, 6, 7] and get the value we want
    So the best case scenario would be 1 our Omega cause it takes the less amount of operations to achieve its purpose
    The average case scenario would be 4 our Theta cause it takes a little more operations to achieve the value
    The worst would be 7 cause our Omicron it takes the whole amount of operations tho achieve 7 that is in the end of the list

# SIMPLIFYING RULES
  - When we have an operation that does the exact same thing with a parameter we pass in, like `drop_constant_example`
    Instead of saying that the operation is a O(2n) we can just say that is a O(n) operation 
  - When we have nesting operations like on our `o_of_n_squared_example` it doesn't matter how much nesting we have
    It will always be simplified as O(2^n)
  - When we have a dominant number of operations on a program like `drop_non_dominants_example` we simplify the equation
    By cutting out the smaller part and only considering the bigger amount of operations that will happen
  - as we could see on `o_of_one_example` despite the value of our n if the number of operations isn't growing based on 
    n, so we call it O(1) 
  - As we could see on `different_terms_for_inputs_example` we cannot simplify equations if their n are not equal
    in this case we had a = 10 and b = 20 se we are not able to assume that O(n) + O(n) = O(2n) and drop the constant 
    and just remain with O(n), is right to tink of it as O(a + b) to simplify at the maximum, 
    and if it were nested for loops the same rule is applied is not O(n^2) is O(a*b)

# PERFORMANCE
  - As we saw on `o_of_log_n_example` we can simplify an operation by taking shortcuts like cutting operations in half
    to achieve the same problem, and it is very efficient not as O(1) efficient but is almost the same flat as it.
  - Some sorting algorithms like quick sort uses the O(n*log n) 
    that is not that efficient but is the most efficient for sorting algorithms
  - 