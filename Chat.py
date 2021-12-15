
import os
chatlist=[]
def read_file(filename):
	if os.path.isfile(filename):
		with open(filename,'r',encoding='utf-8') as f:
			for line in f:
				line = line.strip()
				if line=='你'or line=='和田順':
					name = line
					continue
				else:
					chat=name+': '+line
					print(chat)
					chatlist.append(chat)	

					#print(line)	

	else:	
		print('no file')	

def write_file(filename):
	with open(filename,'w',encoding='utf-8') as f:
		for entry in chatlist:
			f.write(entry+'\n')

read_file('input.txt')
write_file('output.txt')