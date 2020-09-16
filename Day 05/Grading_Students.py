'''HackerLand University has the following grading policy:

  -->  Every student receives a grade in the inclusive range from 0 to 100.

  -->  Any grade less than 40is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

   1. If the difference between the grade and the next multiple of 5is less than 3, round grade up to the next multiple of 5.
   2. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Examples:
	1. grade=84 round to 85(85-84 is less than 3)
	2. grade=29 do not round(result is less than 40)
	3. grade=57 do not round(60-57 is 3 or higher)
'''

#Code:

n=int(input())
for _ in range(n):
	grade=int(input().strip())
	if(grade>=38):
		remainder=grade%5
		if(remainder>=3):
			grade=grade+(5-remainder)
	print(grade)