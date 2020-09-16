'''Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
In the diagram below, the red region denotes his house, where s is the start point, and t is the endpoint.
The apple tree is to the left of his house, and the orange tree is to its right. 
You can assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. 
A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range[s,t])?
'''
#Code:

s,t=input().split()
s=int(s)
t=int(t)
a,b=input().split()
a=int(a)
b=int(b)
m,n=input().split()
m=int(m)
n=int(n)
apples=list(map(int,input().strip().split()))
oranges=list(map(int,input().strip().split()))
apples_count=0
oranges_count=0
for i in range(len(apples)):
    if (a+apples[i]>=s and a+apples[i]<=t):
        apples_count+=1
print(apples_count)
for i in range(len(oranges)):
    if (b+oranges[i]>=s and b+oranges[i]<=t):
        oranges_count+=1
print(oranges_count)
