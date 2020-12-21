'''
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Consider that vowels in the alphabet are a, e, i, o, u and y.

Function score_words takes a list of lowercase words as an argument and returns a score as follows:

The score of a single word is
if the word contains an even number of vowels. Otherwise, the score of this word is

. The score for the whole list of words is the sum of scores of all words in the list.

Debug the given function score_words such that it returns a correct score.

Your function will be tested on several cases by the locked template code.

Input Format

The input is read by the provided locked code template. In the first line, there is a single integer
denoting the number of words. In the second line, there are

space-separated lowercase words.

Constraints

Each word has at most

    letters and all letters are English lowercase letters

Output Format

The output is produced by the provided and locked code template. It calls function score_words with the list of words read from the input as the argument and prints the returned score to the output.

Sample Input 0

2
hacker book

Sample Output 0

4

Explanation 0

There are two words in the input: hacker and book. The score of the word hacker is
because it contains an even number of vowels, i.e. vowels, and the score of book is for the same reason. Thus the total score is

.

Sample Input 1

3
programming is awesome

Sample Output 1

4


'''
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for i in words:
        vowels = 0
        for j in i:
            if is_vowel(j):
                vowels += 1
        if vowels % 2 == 0:
            score += 2
        else:
            score+=1
    return score


n = int(raw_input())
words = raw_input().split()
print score_words(words)
