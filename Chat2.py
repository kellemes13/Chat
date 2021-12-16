
import os
chatlist=[]
def read_file(filename):
	cnt1=0
	cnt2=0
	if os.path.isfile(filename):
		with open(filename,'r',encoding='utf-8') as f:
			for line in f:
				line = line.strip().split()
				print(line)
				for index in range(2,len(line)):
					print('index',index)
					if line[1]=='Joanne':
						cnt1=cnt1+len(line[index])
					else:			
						cnt2=cnt2+len(line[index])	
				row = str(line[1])+': '+str(line[2:])
				chatlist.append(row)						
				#print(row)
			print("J words",cnt1)
			print("me words",cnt2)

	else:	
		print('no file')	

def write_file(filename):
	with open(filename,'w',encoding='utf-8') as f:
		for entry in chatlist:
			f.write(entry+'\n')

read_file('input2.txt')
write_file('output2.txt')
