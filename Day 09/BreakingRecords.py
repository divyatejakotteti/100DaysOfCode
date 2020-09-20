'''Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array scores=[12,24,10,24]. Scores are in the same order as the games played. She would tabulate her results as follows:

                                 Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1
Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.

Function Description:

Complete the breakingRecords function in the editor below. It must return an integer array containing the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1is for breaking least points records.

BreakingRecords has the following parameter(s):

    scores: an array of integers
Sample Input 

9

10 5 20 20 4 5 2 25 1

Sample Output 

2 4

Explanation:

She broke her best record twice (after games 2and 7) and her worst record four times (after games 1, 4, 6, and 8), so we print 2 4 as our answer. Note that she did not break her record for best score during game 3, as her score during that game was not strictly greater than her best record at the time.

'''
#Code:

n=int(input())
arr=list(map(int,input().strip().split()))
min_count=0
max_count=0
mini=arr[0]
maxi=arr[0]
#print(min(arr))
#print(max(arr))
for i in range(n):
     if(mini>arr[i]):
        min_count+=1
        mini=arr[i]
        
for i in range(n):
    if(maxi<arr[i]):
        max_count+=1
        maxi=arr[i]
       
print(max_count,min_count)




