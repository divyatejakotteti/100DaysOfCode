'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format:

The first line contains integer T, the number of test cases.
The next Tlines contains the string S.

Output Format:

Print "True" or "False" for each test case without quotes.

'''
#Code

import re
n=int(input())
for _ in range(n):
	try:
		print(bool(re.compile(input()))
	except re.error:
		print("False")