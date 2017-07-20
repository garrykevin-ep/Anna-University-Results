dept = ['103','104','105','106','114','105','205']
batch= ['13','14','15','16']
file = open('che_code','r')
url = 'http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl?regno='

clg1 = file.readline()
clg = clg1.split(',')

file.close()

def st(z):
	if z/10 == 0:
		return '00'+str(z)
	elif z/100 == 0:  
		return '0'+str(z)
	return str(z)



for x in clg:
	for y in batch: 
		for z in dept:
			for a in range(1,150):
				print url+x+y+z+st(a)