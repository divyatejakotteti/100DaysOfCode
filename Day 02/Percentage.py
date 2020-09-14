if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
query_scores=studentmarks[queryname]
sum=0
for num in query_scores:
	sum+=int(num)
avg=sum/3
print(round(avg,2))
