'''
You are given a string .
Your task is to verify that

is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
For example:
?+4.50
?-1.0
?.5
?-.7
?+.4
? -+4.5

Number must contain at least

decimal value.
For example:
? 12.
?12.0  

Number must have exactly one . symbol.
Number must not give any exceptions when converted using

.

Input Format

The first line contains an integer
, the number of test cases.
The next line(s) contains a string

.

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0

False
True
True
False


'''
from re import match, compile

pattern = compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))