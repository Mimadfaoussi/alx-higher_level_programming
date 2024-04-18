# 0x04. Python - More Data Structures: Set, Dictionary

## Resources :

### Read or watch:

<h1>Data structures</h1>
<p>Lambda, filter, reduce and map</p>
<p>Learn to Program 12 Lambda Map Filter Reduce</p>

## Learning Objectives :

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

## My Documentation : 

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
