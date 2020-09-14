gradelist=[]
scorelist=[]
if __name__ == '__main__':
	for _ in range(int(input())):
		name=int(input())
		score=float(input())
		gradelist+=[[name,score]]
		print(gradelist)
		scorelist+=[score]
		print(scorelist)
	maximum_score=sorted(list(set(scorelist)))[1]
	for name,score in sorted(gradelist):
		if score == maximum_score:
			print(name)