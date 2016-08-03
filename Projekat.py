niz=[
		['x','o','x'],

		['o','o','x'],

		['o','x','x']

	]


def proveri_koordinate():
	if x_kordinata and y_kordinata in range (0,2):
		print ("Sledeci igrac")
	else:
		print ("Greska. Pokusaj ponovo")


	 	
	 	
	 	
def proveri_pobedu():

	

	if niz[0][0] == niz[0][1] == niz[0][2]:
		if niz[0][0]=='x':
			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

		break


	elif niz[1][0] == niz[1][1] == niz[1][2]:
		if niz[1][0]=='x':
			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!")

		break



	elif niz[2][0] == niz[2][1] == niz[2][2]:
		if niz[2][0]=='x':
			print ("prvi igrac pobedio!")

		else: 
			print ("drugi igrac pobedio!")

		break


	elif niz[0][0] == niz[1][0] == niz[2][0]:
		if niz[0][0]=='x':
			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

		break

	elif niz[0][1] == niz[1][1] == niz[2][1]:
		if niz[0][1]=='x':
			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!")

		break
		


	elif niz[0][2] == niz[1][2] == niz[2][2]:
		if niz[0][2]=='x':
			print ("prvi igrac pobedio!")

		else :

			print ("drugi igrac pobedio!") 

		break

	elif niz[0][0] == niz[1][1] == niz[2][2]:
		if niz[0][0]=='x':
			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

		break


	elif niz[0][2] == niz[1][1] == niz[2][0]:
		if niz[0][2]=='x':
			print ("prvi igrac pobedio!")

		else :
			print ("drugi igrac pobedio!") 

		break

	else: 
		x = 'x'
		o = 'o'

		print ("Prvi igrac je na potezu. Upisi koordinate za X(_,_)")
		a = map(str.split, input())
		niz[a].append(x)
		for i in range(0,3):
			print (niz[i])

		print ("Sada je red na drugog igraca. Upisi koordinate za О(_,_).")	
		b = map(str.split, input())
		niz[b].append(o)
		for i in range(0,3):
			print (niz[i])

while True:
	proveri_koordinate()
	proveri_pobedu()






