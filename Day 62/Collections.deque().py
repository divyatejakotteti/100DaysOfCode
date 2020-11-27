'''
Task

Perform append, pop, popleft and appendleft methods on an empty deque

.

Input Format

The first line contains an integer
, the number of operations.
The next

lines contains the space separated names of methods and their values.

Constraints

Output Format

Print the space separated elements of deque

.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output

1 2

'''
from collections import deque
d = deque()
for i in range(int(input())):
    s = input().split()
    if s[0] == 'append':
        d.append(s[1])
    elif s[0] == 'appendleft':
        d.appendleft(s[1])
    elif s[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print (" ".join(d)) 