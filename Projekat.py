niz=[
		[None, None, None],

		[None, None, None],

		[None, None, None]

	]

x_kordinata = 0
y_kordinata = 0
x = 'x'
o = 'o'


def proveri_koordinate():
	global x_kordinata
	global y_kordinata

	if x_kordinata in [0,1,2] and y_kordinata in [0,1,2]:

		if niz[x_kordinata][y_kordinata]==None:
			print ("Sledeci igrac")
			return True
		else:
			print ("Na tom mestu vec ima x ili ox. Pokusaj ponovo.")
			return False
	else:
		print("Greska. Pokusaj ponovo")
		return False

	 	
	 	
	 	
def proveri_pobedu():
	global xo
	global finished
	global x_kordinata
	global y_kordinata
	

	if niz[0][0] == niz[0][1] == niz[0][2] != None:
		if niz[0][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 
			
		finished = True


	elif niz[1][0] == niz[1][1] == niz[1][2] != None:
		if niz[1][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!")

		

		finished = True



	elif niz[2][0] == niz[2][1] == niz[2][2] != None:
		if niz[2][0]=='x':

			print ("prvi igrac pobedio!")

		else: 
			print ("drugi igrac pobedio!")



		finished = True


	elif niz[0][0] == niz[1][0] == niz[2][0] != None:
		if niz[0][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

	

		finished = True

	elif niz[0][1] == niz[1][1] == niz[2][1] != None:
		if niz[0][1]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!")

			


		finished = True
		


	elif niz[0][2] == niz[1][2] == niz[2][2] != None:
		if niz[0][2]=='x':

			print ("prvi igrac pobedio!")

		else:

			print ("drugi igrac pobedio!") 

		finished = True

	elif niz[0][0] == niz[1][1] == niz[2][2] != None:
		if niz[0][0]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

			

		finished = True


	elif niz[0][2] == niz[1][1] == niz[2][0] != None:
		if niz[0][2]=='x':

			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

			

		finished = True

	elif xo == 'x': 

		print ("Prvi igrac je na potezu. Upisi koordinate za x(_,_)")
		a = input()
		x_kordinata = int(a[0])
		y_kordinata = int(a[1])
		if proveri_koordinate() == True:
			niz[x_kordinata][y_kordinata] = x
			xo = 'o'
		for i in range(0,3):
			print (niz[i])
		

	elif xo == 'o':
		print ("Sada je red na drugog igraca. Upisi koordinate za o(_,_).")	
		a = input()
		x_kordinata = int(a[0])
		y_kordinata = int(a[1])
		if proveri_koordinate() == True:
			niz[x_kordinata][y_kordinata] = o
			xo = 'x'
		for i in range(0,3):
			print (niz[i])
		

	
xo = 'x'	
finished=False
while finished == False:
	proveri_pobedu()
	






