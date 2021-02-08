# --- Loops, conditions and parsing ---

# Learning Objectives
       At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
        How to create SSH keys
        What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
        How to use while, until and for loops
        How to use if, else, elif and case condition statements
        How to use the cut command
        What are files and other comparison operators, and how to use them

# Requirements

**General**
   - Allowed editors: vi, vim, emacs
   - All your files will be interpreted on Ubuntu 14.04 LTS
   - All your files should end with a new line
   - A README.md file, at the root of the folder of the project, is mandatory
   - All your Bash script files must be executable
   - You are not allowed to use awk
   - Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
   - The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
   - The second line of all your Bash scripts should be a comment explaining what is the script doing

# Tasks:
   - 0 - All your files, classes and methods must be unit tested and be PEP 8 validated.
   - 1 - Write the first class Base. Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package. Create a file named models/base.py
   - 2 - Write the class Rectangle that inherits from Base.
   - 3 - Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).
   - 4 - Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
   - 5 - Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
   - 6 - Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
   - 7 - Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.
   - 8 - Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.
   - 9 - Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.
   - 10 -Write the class Square that inherits from Rectangle.

# Advanced.
   - 20 - Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV
