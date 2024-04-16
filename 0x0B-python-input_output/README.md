# 0x0B. Python - Input/Output

## Resources :

#### Read or watch :

<ul>
    <li> <a href = "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files">7.2. Reading and Writing Files</a></li>
    <li> <a href = "https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions">8.7. Predefined Clean-up Actions</a></li>
    <li> <a href = "https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf">Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))</a></li>
    <li> <a href = "https://docs.python.org/3/library/json.html">JSON encoder and decoder</a></li>
    <li> <a href = "https://www.youtube.com/watch?v=EukxMIsNeqU">Learn to Program 8 : Reading / Writing Files </a></li>
    <li> <a href = "https://automatetheboringstuff.com/">Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333) </a></li>
    <li> <a href = "https://techvidvan.com/tutorials/python-file-read-write/">All about py-file I/O </a></li>

</ul>

## Learning Objectives :

#### General :

<ul>
  <li>Why Python programming is awesome</li>
  <li>How to open a file</li>
  <li>How to write text in a file</li>
  <li>How to read the full content of a file</li>
  <li>How to read a file line by line</li>
  <li>How to move the cursor in a file</li>
  <li>How to make sure a file is closed after using it</li>
  <li>What is and how to use the with statement</li>
  <li>What is JSON</li>
  <li>What is serialization</li>
  <li>What is deserialization</li>
  <li>How to convert a Python data structure to a JSON string</li>
  <li>How to convert a JSON string to a Python data structure</li>
</ul>

## My Documentation : 

#### How to open a file : 
```
file = open('filename.txt', 'r')  # Opens the file in read mode

```

#### How to write text in a file : 

```
file = open('filename.txt', 'w')  # Opens the file in write mode
file.write('Hello, world!\n')  # Writes text to the file
file.close()  # Remember to close the file after writing

```

#### How to read the full content of a file :

```
file = open('filename.txt', 'r')  # Opens the file in read mode
content = file.read()  # Reads the full content of the file
print(content)
file.close()

```

#### How to read a file line by line :

<p> You can read a file line by line using a loop or the readline() method. </p>


```
file = open('filename.txt', 'r')  # Opens the file in read mode
for line in file:
    print(line)
file.close()

```