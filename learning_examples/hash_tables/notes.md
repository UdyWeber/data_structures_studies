# Introduction to Hash Tables

- Hash tables knows in python as Dictionaries are made up a key value pair
- For hash tables you'll need a hash function that hashes the values of each key and that gives us the address of our 
  key value pair.

# Hashing Function
- It goes one way, so you only can hash key values and not the hash them back to the actual value they represent.
- Hashes are deterministic that meaning: So each time you pass a key to the hash function it will always return the same 
  value they return previously.

# How does it work?
- We are going to have a list with empty values with a bunch of indexes, and the values inserted into the hashtable are
  going to be hashed and the hash will return the index (address) value in the primary list, so we can access it.
- Each time we need to access a value of a key, we can just pass in the key, and being the hash function deterministic
  it will always return us the same value for the same key.
- You'll need to start a Hashtable with a list using a defined size, usually you use a prime number to represent the size
  because of the randomness.
- For creating a hash to each value we iterate over the chars of the key passed to the hash function and for each char
  we will get the decimal representation of the char, multiply it by a prime number, sum it to the old hash value and 
  then make the modules of the value against the size of the list of addresses

## Collisions
- Collisions happen when you put a key value pair into the same address of another one that retrieved the same value 
  in the hashing function.
    ## Separated Chaining
    - The key-value pairs that collide, will exist together into a list object in the address retrieved from the 
        hashing function. This operation of handling colliding hashes into a list is called separated chaining.
    - Another way of doing separated chaining is instead of using lists to use linked lists.

    ## Linear Probing
    -  Is another way of handling collisions, but in this example, if 2 hashes point to the same address we will just
       put the colliding address further in the list where it is an empty space.
