from Service import Service
from os import system, name

print('Modes:\n1 - ID to tag\n2 - Tag to ID')
mode = int(input('Enter Mode >> '))

system('cls' if name == 'nt' else 'clear')

if mode == 1:
	AccountHighID = int(input('Enter AccountHighID >> '))
	AccountLowID = int(input('Enter AccountLowID >> '))
	AccountID = (AccountLowID << 8) + AccountHighID
	print(Service.TagFromID(AccountID))
elif mode == 2:
	Tag = input('Enter Tag >> ')	
	print(Service.TagToID(Tag))
