import wikipedia
def trun():
	f = open('syed.txt','w')
	f.truncate()
	f.close()


def writecontent():
	trun()
	z = open('syed.txt','w')
	lis = ['mark zuckerberg','barack obama']
	for i in lis:
		data = wikipedia.page(i)
		z.write(data.content)
	z.close()



