'''You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

  1. The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
  1. The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO. 

Input Format:

A single line of four space-separated integers denoting the respective values ofx1, v1, x2,and v2.

Output Format:

Print YES if they can land on the same location at the same time; otherwise, print NO.

Note: The two kangaroos must land at the same location after making the same number of jumps.
'''
#Code:

x1,v1,x2,v2=input().split()
x1=int(x1)
v1=int(v1)
x2=int(x2)
v2=int(v2)
if x1 > x2 and v1 > v2:
         print("NO")
if x1 < x2 and v1 < v2:
        print("NO")
else:
    print("YES")
