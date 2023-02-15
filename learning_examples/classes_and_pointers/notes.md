# INTRO TO CLASSES
  - Classes are like models that we can shape in every way we want, all data structures in Python will be classes
    that will have they particular properties and methods to be used by the instance of the class
  - The methods inside classes are functions and the first method of a class is always it's initialize method that in
    python we call __init__ method, it will be tha constructor for our class.
  - The method __init__ takes in `self`  that references to the class and differs a function of a method, our class can 
    receive int the init method any other  parameters that we need to initialize our class

# CLASS EXAMPLES AND EXPLANATIONS
  - As we can see in the example `class_example` we create a class called Person and each instance of the class has
    its own set of properties, based on the variables we passed in the constructor

# POINTERS EXAMPLES AND EXPLANATIONS
  - As we can see in the example `integer_pointers_example` variables that store integers point to specific registers
    in memory, that if accessed by another variable points to the same register that the first pointer is pointing
    but if we change the value of the second variable that is pointing to the same register it will create a new
    space in memory because integers in memory are immutable, so we cannot change the value of a pointer to an integer
  - But as we see in `dictionary_pointers_example` as dictionaries are not immutable we can point to the same space in
    memory and change its value through any pointer, that's the start of a LikedList Concept.
