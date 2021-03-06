'''You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

    The elements of the first array are all factors of the integer being considered
    The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

Function Description:

Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):

    a: an array of integers
    b: an array of integers

Input Format:
The first line contains two space-separated integers, n and m, the number of elements in array a and the number of elements in array b.
The second line contains n distinct space-separated integers describing a[i]where 0<=i<n.
The third line contains m distinct space-separated integers describing b[j]where 0<=j<m.

Constraints:
 1. 1<= n,m <=10
 2. 1<= a[i] <=100
 3. 1<= b[j] <=100

Output Format:

Print the number of integers that are considered to be between a and b.
Sample Input

2 3
2 4
16 32 96

Sample Output

3

Explanation

2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b. 
'''
#Code:
n,m = input().rstrip().split()
n = int(n)
m = int(m)
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
a_fact=[]
b_fact=[]
co_fact=[]
max_len=len(a+b)
#print(max_len)
for i in range(1,101):
    for num in a:
        if i%num==0 :
            a_fact.append(i)
#print(a_fact)
for i in range(1,101):
    for num in b:
        if num % i==0:
            b_fact.append(i)
#print(b_fact)
temp=a_fact + b_fact
#print(temp)
for num in temp:
    #print(temp.count(num))
    if temp.count(num)==max_len:
        co_fact.append(num)
print(len(set(co_fact)))

