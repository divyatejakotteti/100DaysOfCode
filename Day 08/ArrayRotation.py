'''A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become[3,4,5,1,2].

Given an array 'a' of n integers and a number, d, perform 'd'left rota

Function Description:

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

   1. An array of integers a.
   2. An integerd, the number of rotations.

Input Format:

The first line contains two space-separated integers n and d, the size of a and the number of left rotations you must perform.
The second line n contains space-separated integers a[i].

Output Format:

Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.

#Sample Input

5 4
1 2 3 4 5

#Sample Output

5 1 2 3 4
'''
#Code:Array_left rotation
n,r=input().split()
n=int(n)
r=int(r)
arr=list(map(int,input().strip().split()))
for i in range(len(arr)):
	 left_rotate=arr[r:] + arr[:r]
print(' '.join(map(str,left_rotate)))

'''Array_Right Rotation
for i in range(len(arr)):
	Right_rotate=arr[:r] + arr[r:]
'''
	
