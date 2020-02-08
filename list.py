lists = [] 
while True:
	name = input('購買的物品:')
	if name == 'quit':
		break
	price = input('金額:')
	lists.append([name, price])
	
for l in lists:
	print(l[0],l[1] ,'元')



  