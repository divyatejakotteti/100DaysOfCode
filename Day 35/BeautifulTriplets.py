'''
Given a sequence of integers , a triplet

is beautiful if:

Given an increasing sequenc of integers and the value of

, count the number of beautiful triplets in the sequence.

Function Description

Complete the beautifulTriplets function in the editor below. It must return an integer that represents the number of beautiful triplets in the sequence.

beautifulTriplets has the following parameters:

    d: an integer
    arr: an array of integers, sorted ascending

Input Format

The first line contains
space-separated integers and , the length of the sequence and the beautiful difference.
The second line contains space-separated integers.

Output Format

Print a single line denoting the number of beautiful triplets in the sequence.

Sample Input

7 3
1 2 4 5 7 8 10

Sample Output

3

'''   
  
def beautifulTriplets(d, arr):
    count=0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            if ((arr[j] - arr[i] == d)):
                for k in range(j+1,len(arr)):
                    if((arr[k] - arr[j] == d)):
                        count+= 1
                        break
    return(count)

if __name__ == '__main__':


    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)
  
    