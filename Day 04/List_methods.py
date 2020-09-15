'''Consider a list (list = []). You can perform the following commands: 
 
1. insert i e: Insert integer e at i position .

2. print: Print the list.

3. remove e: Delete the first occurrence of integer e.

4. append e: Insert integer e at the end of the list. 

5. sort: Sort the list.

6. pop: Pop the last element from the list.

7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7types listed above. 
Iterate through each command in order and perform the corresponding operation on your list. 

Input Format::

The first line contains an integer,n,denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints::

    The elements added to the list must be integers.
'''

n=int(input())
lis=[]
for i in range(n):
	s=input().split()
	for i in range(1,len(s)):
		s[i]=int(s[i])
	if s[0] == 'append':
		lis.append(s[1])
	elif s[0] == 'insert':
		lis.insert(s[1],s[2])
	elif s[0] == 'remove':
		lis.remove(s[1])
	elif s[0] == 'reverse':
		lis.reverse()
	elif s[0] == 'pop':
		lis.pop()
	elif s[0] == 'sort':
		lis.sort()
	elif s[0] == 'print':
		print(lis)
