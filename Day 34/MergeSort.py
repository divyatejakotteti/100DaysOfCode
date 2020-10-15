'''
In an array, , the elements at indices and (where ) form an inversion if . In other words, inverted elements and

are considered to be "out of order". To correct an inversion, we can swap adjacent elements.

For example, consider the dataset
. It has two inversions: and

. To sort the array, we must perform the following two swaps to correct the inversions:

Given

datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

Function Description

Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.

countInversions has the following parameter(s):

    arr: an array of integers to sort .

Input Format

The first line contains an integer,

, the number of datasets.

Each of the next

pairs of lines is as follows:

    The first line contains an integer, 

, the number of elements in
.
The second line contains
space-separated integers, . 
Output Format

For each of the

datasets, return the number of inversions that must be swapped to sort the dataset.

Sample Input

2  
5  
1 1 1 2 2  
5  
2 1 3 1 2

Sample Output

0  
4   

'''

def countInversions(arr):
    count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                count += 1
  
    return count 
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
    
    
    