# CS-210-Programming-Languages
Coursework from CS-210

This project was meant to provide users with the ability to view different parts of a hypothetical grocery store's inventory. The program vets user input, interfaces with Python, interats with files, and displays and manipultes data from those files.

An area where I did well in this project is with the Python/C functions, found in python_functions.cpp. I optimized the starter code for my implementation to keep my instance of a Python class alive so it could be called upon to perform different functions within the program. 

My program could be improved as memory efficiency goes. While I passed by reference instead of value when possible, I did not have time to sufficiently manage the memory used by Python while running. Given time I believe I could make the program faster and use fewer resources. 

THe msot challenging (and rewarding pieces) to write were, once again, the Python/C interfacing. I spent hours and hours reading the documentation for the Python/C API, and figured out how its heap worked in terms of being embedded in C++ (It turns out it is a private heap, and much of Python's inner-workings is "black-boxed" away from the C++ program, which is by design- it prevents accidental interference by programmers). I definitely have the entire Python documentation bookmarked, as it maybe useful in the future.

Integrating C and Python is perhaps the most transferable, as I intend to specialize in machine learning later in my educational career. I believe using C++ with Python will be an excellent mix of data processing an d support from Python, with speed and efficiency being the benefit of C++.

As far as adaptibility, I believe making the python code into a class was perhaps the best move. Much of the data that was relevant to the program would had to have been redundantly created were it not inside a class instance. Also, the Python code became much easier to modify once it was in a class, as it provided a structure where otherwise the file would have been a series of separate functions. For maintainability and readability, I followed C++ and Python style guides as closely as possible. I also extensively commented my code to demonstrate understanding and also to keep track of what the intention was for each line of code.
