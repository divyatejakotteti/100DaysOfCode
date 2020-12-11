'''
There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananasand Peanuts, the Monkeys jump down the Tree.

If every Monkey can eat k Bananas and Peanuts. IfTotal m number of Bananas and p number ofPeanuts offered by Travelers,
calculate how many Monkeys remain on the Tree after some of themjumped down to eat.

At a time, one Monkey gets down and finishes eatingand go to the other side of the road. The Monkey whoclimbed down does not climb up again after eating
until the other Monkeys finish eating.Monkey can either eat k Bananas orj Peanuts. 

If for last Monkey there are less than k Bananas left on theground or less than ; Peanuts left on the ground, only
that Monkey can eat Bananas(<k) along with the Peanuts(<j).
Write the code to take inputs as n, m, p, k, j and
return the number of Monkeys left on the Tree.

Where, n = Total number of Monkeys
k= Number of eatable Bananas by a single Monkey
(Monkey that jumped down last may get less thank
Bananas)
j = Number of eatable Peanuts by a single Monkey
(Monkey that jumped down last may get less thank
Bananas)
m= Total number of Bananas? 
p= Total number of Peanuts
'''
n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())
if(k>0):
	atebanana=(float)m/k
if(j>0)
	atepeanut=(float)p/j
n=n-atebanana-atepeanut
print("Number of Monkeys left on the Tree:",n)
