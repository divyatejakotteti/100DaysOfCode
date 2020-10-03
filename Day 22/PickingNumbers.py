'''
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

Example
a=[1,1,2,2,4,4,5,5,5]

There are two subarrays meeting the criterion:[1,1,2,2] and [4,4,5,5,5]. The maximum length subarray has 5 elements.

Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):

    int a[n]: an array of integers

Returns

    int: the length of the longest subarray that meets the criterion

Input Format

The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers, each an a[i].
Sample Input 

6
4 6 5 3 3 1

Sample Output 

3

Explanation 

We choose the following multiset of integers from the array: {4,3,3}. Each pair in the multiset has an absolute difference<=1 (i.e.,|4-3|=1 and |3-3|=0), so we print the number of chosen integers, 3, as our answer.

'''

def pickingNumbers(a):
    # Write your code here
    maximum = 0
    diff = 1
    for i in a:
        n = a.count(i)
        m = a.count(i-diff)
        s=n+m
        maximum = max(maximum,s)
    return (maximum) 

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
    
    
    