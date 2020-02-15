
import os

#讀取檔案
def read_file(filename):
	accounts = [] 
	with open(filename,'r') as f:
		for line in f:  #line 為 excel 內的每一行
			if '商品,價格'in line:
				continue
			name, price = line.strip().split(',')
			accounts.append([name, price])
	print(accounts)
	return accounts

#增加帳目
def input_file(accounts): 
	while True:
		name = input('購買的物品:')
		if name == 'X':
			break
		price = input('金額:')
		price = int(price)
		accounts.append([name, price])
	return accounts

#印出帳目
def print_products(accounts):	
	for l in accounts:
		print(l[0],l[1] ,'元')

#寫入檔案
def write_file(filename, accounts):	
	with open(filename,'w') as f:
		f.write('商品,價格\n')
		for l in accounts:
			f.write(l[0] + ',' + str(l[1]) + '\n')

#main function
def main(): 
	filename = 'lists.csv'
	if os.path.isfile(filename):
		print('找到檔案了')
		accounts = read_file(filename)
	else:
		print('找不到檔案')

	accounts = input_file(accounts)
	print_products(accounts)
	write_file(filename, accounts)

main()