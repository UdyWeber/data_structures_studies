# Introduction to recursion
- It's main concept is a function that calls itself till a condition is reached.
- If we don't have a stop condition it can cause a Stack Overflow by the function calling itself forever
- And you have to have a return statement in the recursive function, or it is going to cause a stack overflow either

# Call Stack
- The call stack is a Stack structure, that has on it the functions to be called. The function that's on the top of the
  stack is the first to be called, so the next function under can run till the stack is completely empty
