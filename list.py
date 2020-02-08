lists = [] 
while True:
	name = input('購買的物品:')
	if name == 'quit':
		break
	price = input('金額:')
	price = int(price)
	lists.append([name, price])
	
for l in lists:
	print(l[0],l[1] ,'元')

with open('lists.csv','w') as f:
	f.write('商品,價格\n')
	for l in lists:
		f.write(l[0] + ',' + str(l[1]) + '\n')

  