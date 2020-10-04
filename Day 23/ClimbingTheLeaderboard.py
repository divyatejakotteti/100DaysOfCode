'''
An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Example
ranked=[100,90,90,80]
player=[70,80,105]

The ranked players will have ranks 1, 2, 2, and 3, respectively. If the player's scores are 70,80 and 105, their rankings after each game are 4th,3rd and 1st. Return [4,3,1].
Function Description

Complete the climbingLeaderboard function in the editor below.

climbingLeaderboard has the following parameter(s):

    int ranked[n]: the leaderboard scores
    int player[m]: the player's scores

Returns

    int[m]: the player's rank after each new score

Input Format

The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
The next line contains an integer, m, the number games the player plays.
The last line contains m space-separated integers player[j], the game scores.

Sample Input 1
CopyDownload




Array: ranked




100


100


50


40


40


20


10



 






Array: player




5


25


50


120



 

7
100 100 50 40 40 20 10
4
5 25 50 120

Sample Output 1

6
4
2
1
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked=sorted(set(ranked)),reverse=True)
    player.sort(reverse=True)
    j=0
    s=[]
    for i in range(len(player)):
        while j<len(ranked) and player[i]<ranked[j]:
            j+=1
        s.append(j+1)
    return(s[::-1])


    return ranking
if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
