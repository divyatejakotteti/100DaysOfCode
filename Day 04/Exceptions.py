'''
Handling Exceptions :

	The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.

Task:

You are given two values a and b.
Perform integer division and print a/b.

Input Format::

The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.

Constraints :
	0<T<10

'''
#Code



n= int(input())
for i in range(n):
	try:
		a,b=map(int,input().split())
		print(a/b)
	except BaseException as e:
		print("Error code",e)
