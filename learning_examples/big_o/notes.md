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