def main():

	niz=[[1,1,1],[1,1,1],[1,1,1]]


	x_kordinata=0
	y_kordinata=0
main()


	 	
	 	
	 	
def proveri_pobedu():

	 niz=[
	 ['x','o','x'],

		['o','o','x'],

		['o','x','x']

		]

	if niz[0][0] == niz[0][1] == niz[0][2]:
		if niz[0][0]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break


	elif niz[1][0] == niz[1][1] == niz[1][2]:
		if niz[1][0]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break



	elif niz[2][0] == niz[2][1] == niz[2][2]:
		if niz[2][0]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break


	elif niz[0][0] == niz[1][0] == niz[2][0]:
		if niz[0][0]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break

	elif niz[0][1] == niz[1][1] == niz[2][1]:
		if niz[0][1]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break
		


	elif niz[0][2] == niz[1][2] == niz[2][2]:
		if niz[0][2]=='x'
			print "prvi igrac pobedio!"

		else 

			print "drugi igrac pobedio!" 

		break

	elif niz[0][0] == niz[1][1] == niz[2][2]:
		if niz[0][0]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break


	elif niz[0][2] == niz[1][1] == niz[2][0]:
		if niz[0][2]=='x'
			print "prvi igrac pobedio!"

		else 
			print "drugi igrac pobedio!" 

		break

	else: 
		print ("Prvi igrac je na potezu. Upisi koordinate za X(_,_)")
		a = input().split(' ')
		print (a)
		for i in range(0,3):
			print (niz[i])

		print ("Sada je red na drugog igraca. Upisi koordinate za О(_,_).")	
		b = input().split(' ')
		print (b)
		for i in range(0,3):
			print (niz[i])

while True:
	proveri_pobedu()






