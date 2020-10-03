'''
Consider the following:

A string, s, of length n where s=c0,c1,c2,...Cn-1.
An integer,k, where k is a factor of n.

We can split s into n/k subsegments where each subsegment, t, consists of a contiguous block of k characters in s. Then, use each t to create string u such that:
The characters in u are a subsequence of the characters in t.
Any repeat occurrence of a character is removed from the string such that each character in u occurs exactly once. In other words, if the character at some index in occurs at a previous index<j in t, then do not include the character in string u.

Given sand k, print n/k lines where each line denotes string u.

Input Format

The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.
Output Format

Print n/k lines where each line i contains string u.

Sample Input

AABCAAADA
3   

Sample Output

AB
CA
AD

'''

def merge_the_tools(string,k):
    l=[]
    count=0
    for i in string:
        count+=1
        if i not in l:
            l.append(i)
        if count==k:
            print(''.join(l))
            l=[]
            count=0


string,k=input(),int(input())
merge_the_tools(string,k)

   
    