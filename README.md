# CS261_assignment5_min_heap

General Instructions
1. Programs in this assignment must be written in Python v3 and submitted to
Gradescope before the due date specified in the syllabus. You may resubmit your
code as many times as necessary. Gradescope allows you to choose which
submission will be graded.
2. In Gradescope, your code will run through several tests. Any failed tests will provide
a brief explanation of testing conditions to help you with troubleshooting. Your goal
is to pass all tests.
3. We encourage you to create your own test programs and cases even though this
work won’t have to be submitted and won’t be graded. Gradescope tests are limited
in scope and may not cover all edge cases. Your submission must work on all valid
inputs. We reserve the right to test your submission with more tests than
Gradescope.
4. Your code must have an appropriate level of comments. At a minimum, each method
should have a descriptive docstring. Additionally, put comments throughout the code
to make it easy to follow and understand.
5. You will be provided with a starter “skeleton” code, on which you will build your
implementation. Methods defined in skeleton code must retain their names and input
/ output parameters. Variables defined in skeleton code must also retain their
names. We will only test your solution by making calls to methods defined in the
skeleton code and by checking values of variables defined in the skeleton code.
You can add more helper methods and variables, as needed. You also are allowed to
add optional default parameters to method definitions.
However, certains classes and methods can not be changed in any way. Please see
comments in the skeleton code for guidance. In particular, content of any methods
pre-written for you as part of the skeleton code must not be changed.
6. Both the skeleton code and code examples provided in this document are part of
assignment requirements. They have been carefully selected to demonstrate
requirements for each method. Refer to them for the detailed description of expected
method behavior, input / output parameters, and handling of edge cases. Code
examples may include assignment requirements not explicitly stated elsewhere.
7. For each method, you can choose to implement a recursive or iterative solution.
When using a recursive solution, be aware of maximum recursion depths on large
inputs. We will specify the maximum input size that your solution must handle.
8. We will test your implementation with different types of objects, not just integers.
We guarantee that all such objects will have correct implementation of methods
__eq__, __lt__, __gt__, __ge__, __le__ and __str__.

Part 2 - Summary and Specific Instructions
1. Implement the MinHeap class by completing provided skeleton code in the file
min_heap.py. Once completed, your implementation will include the following
methods:
add()
get_min()
remove_min()
build_heap()
2. Prewritten DynamicArray class is provided for you in the skeleton code (file
a5_include.py). You should use objects of this class in your MinHeap class
implementation for storing heap content.
3. Prewritten DynamicArray class may provide different functionality than that
described in the lectures or implemented in prior homework assignments. Review
docstrings in the skeleton code to understand available methods, their use, and input
/ output parameters.
4. The number of objects stored in the MinHeap will be between 0 and 1,000,000
inclusive.
5. RESTRICTIONS: You are NOT allowed to use ANY built-in Python data structures
and/or their methods.
You are NOT allowed to directly access any variables of the DynamicArray class. All
work must be done only by using class methods.
6. Variables in the MinHeap class are not private. You ARE allowed to access and
change their values directly. You do not need to write any getter or setter methods
for the MinHeap class.
