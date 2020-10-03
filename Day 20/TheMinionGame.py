'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,S.
Both players have to make substrings using the letters of the stringS.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the stringS.

For Example:
String S= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
'''
def minion_game(string):
    # your code goes here
    stuartpoint=0
    kelvin_point=0
    for i in range(len(string)):
        if s[i] in "AEIOU":
            kelvin_point+=len(string)-i
        else:
            stuartpoint+=len(string)-i
    if kelvin_point>stuartpoint:
        print("Kevin",kelvin_point)
    elif kelvin_point<stuartpoint:
        print("Stuart",stuartpoint)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)