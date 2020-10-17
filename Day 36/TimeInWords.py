'''
Given the time in numerals we may convert it into words, as shown below:

At
, use o' clock. For , use past, and for

use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below. It should return a time string as described.

timeInWords has the following parameter(s):

    h: an integer representing hour of the day
    m: an integer representing minutes after the hour

Input Format

The first line contains
, the hours portion The second line contains

, the minutes portion

Constraints

Output Format

Print the time in words as described.

Sample Input 0

5
47

Sample Output 0

thirteen minutes to six

Sample Input 1

3
00

Sample Output 1

three o' clock


'''
def timeInWords(h, m):
    nums = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",  
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]
    if (m == 0): 
        print(nums[h], "o' clock")
    elif (m == 1): 
        print("one minute past", nums[h]); 
  
    elif (m == 59): 
        print("one minute to", nums[(h % 12) + 1]); 
  
    elif (m == 15): 
        print("quarter past", nums[h]); 
  
    elif (m == 30): 
        print("half past", nums[h]); 
  
    elif (m == 45): 
        print("quarter to", (nums[(h % 12) + 1])); 
  
    elif (m <= 30): 
        print(nums[m],"minutes past", nums[h]); 
  
    elif (m > 30): 
        print(nums[60 - m], "minutes to",  
              nums[(h % 12) + 1])

if __name__ == '__main__':

    h = int(input())

    m = int(input())

    timeInWords(h, m)