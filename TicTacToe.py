import os


def pmatrix(mat):

	i = len(mat)
	j = len(mat[0])
	for l in range(i):
		for c in range(j):
			print('{:>3}|'.format(matrix01[l][c]),end=' ')
		print()

def verification(lin,col):
	verified = 0
	if(matrix01[lin][col]=='X' or matrix01[lin][col]=='O'):
		verified+=1
	return(verified)

def victory(mat,jog):
	if turn<5:
		return ('none')
	elif (turn>8):
		return('No winner - Tie')
	else:
		for x in mat:
			if(x.count('X')>2):
				return('X is the winner')
			elif(x.count('O')>2):
				return('O is the winner')
		for col in range(3):
			listaaux = []
			for lin in range(3):
				listaaux.append(mat[lin][col])
			if(listaaux.count('X')>2):
				return('X is the winner')
			elif(listaaux.count('O')>2):
				return('O is the winner')
		if((mat[0][2]==mat[1][1]==mat[2][0]=='O')
		or(mat[0][0]==mat[1][1]==mat[2][2]=='O')):
			return('O is the winner')
		elif((mat[0][0]==mat[1][1]==mat[2][2]=='X')
		or(mat[0][2]==mat[1][1]==mat[2][0]=='X')):
			return('X is the winner')
		return('none')
			
matrix01 = [['00','01','02'],['10','11','12'],['20','21','22']]	
winner='none'
turn = 1
pmatrix(matrix01)

while(winner=='none'):

	if(turn%2 == 0):
		valin = int(input('X turn - which line would you like to play?: '))
		valcol = int(input('X joga - which column would you like to play?: '))
		ver = verification(valin,valcol)
		if(ver==0):
			os.system('cls')
			matrix01[valin][valcol] ='X'
			turn+=1
		else:
			os.system('cls')
			print('space already selected')
	else:
		valin = int(input('O turn - which line would you like to play?: '))
		valcol = int(input('O turn - which column would you like to play?: '))
		ver = verification(valin,valcol)
		if(ver==0):
			os.system('cls')
			matrix01[valin][valcol] ='O'
			turn+=1
		else:
			os.system('cls')
			print('space already selected')
	pmatrix(matrix01)
	winner = victory(matrix01,turn)
	


os.system('cls')
print('\nEnd of the game\n')
pmatrix(matrix01) 
print('\nWinner:',winner)
