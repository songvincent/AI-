import os
with open('test.txt',encoding='utf-8') as trainf:
	trainlines=trainf.readlines()
trainf.close()
print(len(trainlines))
#for line in trainlines:
#	print(line)
#with open('result.txt','w+',encoding='utf-8') as resf:
#	for line in trainlines[0:10]:
#		li=line.split('.')
#		for l in li:
#			resf.write(l+'\n')
#resf.close()
res=[]
for trainline in trainlines:
	with open('result.txt','w+',encoding='utf-8') as resf:
		trainli=trainline.split('.')
		for trainl in trainli:
			resf.write(trainl+'\n')
	resf.close()
	os.system('readability result.txt >num.txt')
	tmpres=[]
	with open('num.txt') as numf:
	#	tmpres=[]
		numlines=numf.readlines()
		for numline in numlines:
			tmp=numline.split()
			if not tmp[1].endswith(':'):
				tmpres.append(tmp[1]) 
			#print(numline.split())
	
	numf.close()
	res.append(tmpres)
with open('result.csv','w+',encoding='utf-8') as rescsvf:
	for r in res:
		rescsvf.write(','.join(r)+'\n')
rescsvf.close()


		
