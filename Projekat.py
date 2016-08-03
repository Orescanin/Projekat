niz=[
		[1, 2, 3],

		[4, 5, 6],

		[7, 8, 9]

	]

x_kordinata = 0
y_kordinata = 0
x = 'x'
o = 'o'


def proveri_koordinate():
	if x_kordinata in [0,1,2] and y_kordinata in [0,1,2]:
		print ("Sledeci igrac")
	else:
		print ("Greska. Pokusaj ponovo")


	 	
	 	
	 	
def proveri_pobedu():
	global xo
	

	if niz[0][0] == niz[0][1] == niz[0][2]:
		if niz[0][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 
			
		finished = True


	elif niz[1][0] == niz[1][1] == niz[1][2]:
		if niz[1][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!")

		

		finished = True



	elif niz[2][0] == niz[2][1] == niz[2][2]:
		if niz[2][0]=='x':

			print ("prvi igrac pobedio!")

		else: 
			print ("drugi igrac pobedio!")



		finished = True


	elif niz[0][0] == niz[1][0] == niz[2][0]:
		if niz[0][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

	

		finished = True

	elif niz[0][1] == niz[1][1] == niz[2][1]:
		if niz[0][1]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!")

			


		finished = True
		


	elif niz[0][2] == niz[1][2] == niz[2][2]:
		if niz[0][2]=='x':

			print ("prvi igrac pobedio!")

		else:

			print ("drugi igrac pobedio!") 

		finished = True

	elif niz[0][0] == niz[1][1] == niz[2][2]:
		if niz[0][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

			

		finished = True


	elif niz[0][2] == niz[1][1] == niz[2][0]:
		if niz[0][2]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

			

		finished = True

	elif xo == 'x': 

		print ("Prvi igrac je na potezu. Upisi koordinate za X(_,_)")

		x_kordinata, y_kordinata = map(int, input().split(' '))
		niz[x_kordinata][y_kordinata].append(x)
		for i in range(0,3):
			print (niz[i])
		xo = 'o'

	elif xo == 'o':
		print ("Sada je red na drugog igraca. Upisi koordinate za О(_,_).")	
		x_kordinata, y_kordinata = map(int, input().split(' '))
		niz[x_kordinata][y_kordinata].append(o)
		for i in range(0,3):
			print (niz[i])
		
		xo = 'x'

	
xo = 'x'	
finished=False
while finished == False:
	proveri_koordinate()
	proveri_pobedu()






