'''Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.
Consider the chocolate bar as an array of squares,s=[2,2,1,3,2] . She wants to find segments summing to Ron's birth day, d=4 with a length equalling his birth month, m=2. In this case, there are two segments meeting her criteria:[2,2] and [1,3].

Function Description:

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s):

    s: an array of integers, the numbers on each of the squares of chocolate
    d: an integer, Ron's birth day
    m: an integer, Ron's birth month

Input Format:

The first line contains an integer n, the number of squares in the chocolate bar.
The second line contains n space-separated integers s[i], the numbers on the chocolate squares where 0<=i<n.
The third line contains two space-separated integers,d and m, Ron's birth day and his birth month.

Output Format:

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

Sample Input 

5
1 2 1 3 2
3 2

Sample Output 

2
'''
#Code:
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
count = 0
q = s[:m-1]
for i in s[m-1:]:
    q.append(i)
    if (sum(q) == d):
        count += 1
    q.pop(0)
print(count)