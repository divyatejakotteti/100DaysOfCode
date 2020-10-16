'''
You wish to buy video games from the famous online video game store Mist.

Usually, all games are sold at the same price,
dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game you buy during the sale will be sold at dollars, but every subsequent game you buy will be sold at exactly dollars less than the cost of the previous one you bought. This will continue until the cost becomes less than or equal to dollars, after which every game you buy will cost dollars each.
Input Format

The first and only line of input contains four space-separated integers
, , and . 
Output Format

Print a single line containing a single integer denoting the maximum number of games you can buy.

Sample Input 0

20 3 6 80

Sample Output 0

6


'''
def howManyGames(p, d, m, s):
    count=0
    while(s>=p):
        count+=1
        s-=p
        p=max(p-d,m)
    return count
       
if __name__ == '__main__':
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])
    answer = howManyGames(p, d, m, s)