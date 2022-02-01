#  CLI RPN Calculator
Command-line reverse polish notation (RPN) calculator in Python. In RPN, the operators follow their operands; for instance, to add 3 and 4 together, one would write 3 4 + rather than 3 + 4. If there are multiple operations, operators are given immediately after their final operands

# Prerequisites:
Python installed locally.

# How to run the RPN CLI program:
> python rpn.py

# Usage/Examples:
![image](https://user-images.githubusercontent.com/8810883/151933362-5b9890f2-2c4e-4cfe-bede-3144d0ea4bae.png)

----

![image](https://user-images.githubusercontent.com/8810883/151928604-f89566be-f480-4141-beff-ed1886763f3a.png)

----

![image](https://user-images.githubusercontent.com/8810883/151928757-89002d62-fe8d-4f63-9f85-ccfe9d5c9411.png)

Note: The calculator exits when it receives a q command or an end of input indicator (EOF / Ctrl+D / Ctrl+Z on Windows)

# Some Implementation details:
It's a simple stack based implementaion. I used lambda functions which are inline functions that tend to execute comparatively faster. You can also see that the code can be easily enhanced to include more than the basic 4 operators. How the code can be improved: Instead of using Python module, which behaves like a singleton class (which means we only have one instance), a better approach may be using a class which could be used to create multiple instances that don't interfere with each other.

# Automated Testing
Used unittest - Automated testing framework. The unit testcases include solving a few expressions and error cases. To run the automated testcases, run the following command:

> python test.py

![image](https://user-images.githubusercontent.com/8810883/151930776-579eefa3-fdb3-42c2-99ca-042e0217c465.png)

