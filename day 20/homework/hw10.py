# 10) დაითვალე დადებითი და უარყოფითი რიცხვების რაოდენობა სიიდან



numbers=[-1,2,3,4,-5,-6,-7,-8,10,11]


positive=0
negative=0

for i in numbers:
    if i>0:
        positive+=i
    else:
        negative+=i

print(positive)
print(negative)