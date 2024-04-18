# 0x04. Python - More Data Structures: Set, Dictionary

### Resources :

#### Read or watch:

<p><a href="https://docs.python.org/3/tutorial/datastructures.html" >Data structures</a></p>

<p><a href="https://python-course.eu/advanced-python/lambda-filter-reduce-map.php" >Lambda, filter, reduce and map</a></p>

<p><a href="https://www.youtube.com/watch?v=1GAC6KQUPeg" >Learn to Program 12 Lambda Map Filter Reduce</a></p>

### Learning Objectives :

<ul>
  <li>Why Python programming is awesome</li>
  <li>What are sets and how to use them</li>
  <li>What are the most common methods of set and how to use them</li>
  <li>When to use sets versus lists</li>
  <li>How to iterate into a set</li>
  <li>What are dictionaries and how to use them</li>
  <li>When to use dictionaries versus lists or sets</li>
  <li>What is a key in a dictionary</li>
  <li>How to iterate over a dictionary</li>
  <li>What is a lambda function</li>
  <li>What are the map, reduce and filter functions</li>
</ul>

### My Documentation : 

### Why Python programming is awesome :

<p> Python programming is awesome for many reasons, including its simplicity, readability, versatility, and vast community support </p>

### What are sets and how to use them :

Sets in Python are unordered collections of unique elements. You can create a set using curly braces {} or the set() function.

``` 
my_set = {1, 2, 3, 4}
my_set = (1, 2, 3, 4)

```

### What are the most common methods of sets and how to use them: 

<p> Some common methods of sets include add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), and symmetric_difference() , example : </p>

```
my_set.add(5)
my_set.remove(3)
my_set.discard(10)  # Discard an element safely
my_set.union({4, 5, 6})  # Returns a new set with elements from both sets

```

### When to use sets versus lists :

<p> Use sets when you need to store unique elements and don't care about the order. Use lists when you need to maintain the order of elements or when elements can be duplicated </p>

### How to iterate into a set : 

```
for element in my_set:
    print(element)

```

### What are dictionaries and how to use them : 

<p> Dictionaries in Python are unordered collections of key-value pairs. You can create a dictionary using curly braces {} or the dict() constructor. </p>

```
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

```

### When to use dictionaries versus lists or sets : 

<ul>
    <li>
        Use dictionaries when you need to associate keys with values or when you need to perform fast lookups based on keys.
    </li>
    <li>
        Use lists when you need ordered collections of elements .
    </li>
    <li>
        Use sets when you need to store unique elements and don't care about the order.
    </li>

</ul>

### How to iterate over a dictionary : 

```
for key, value in my_dict.items():
    print(key, value)

```

### What is a lambda function :

<p> A lambda function is a small anonymous function defined using the lambda keyword. It can take any number of arguments but can only have one expression. </p>

### What are the map, reduce, and filter functions :

<ul>
  <li>map(): Applies a function to all the items in an input list and returns a new list with the results.</li>
  <li>reduce(): Applies a rolling computation to sequential pairs of values in a list until only one value remains.</li>
  <li>filter(): Filters out elements from a list based on a condition defined by a function.</li>
</ul>

```
numbers = [1, 2, 3, 4, 5]

# Using map()
squared = list(map(lambda x: x**2, numbers))

# Using reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

# Using filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

```

