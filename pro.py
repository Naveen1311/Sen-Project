import os
file=open('dumpy.txt','r')
dumpy=file.read()
os.remove('code.c')
code_file=open('code.c','a')
dumpy=dumpy[:len(dumpy)-1]
print 'Entered natural language commands:',dumpy

lines=dumpy.split(" ")
#print lines

declarations=['add','sum','plus','combine','total','addition']
typeof=['int','integer','double','float']
X=['array','list','set']
code_file=open('code.c','a')
a=[x for x in lines if x in typeof]
b=[x for x in lines if x in declarations]
c=[x for x in lines if x in X]

d=[int(x) for x in lines if x.isdigit()==True ]

#print a,len(d)
if len(a)==0:
	a=raw_input('Give the data type of the numbers to be added:')
if len(b)==0:	
	b=raw_input('Give the actions to be done:')

if a=='int' or a=='integer':
	d=[int(x) for x in lines if x.isdigit()==True]
	if len(d)==0:
		d=map(int,raw_input('Give the numbers to be added:').split())		
if a=='double':
	d=[float(x) for x in lines if x.isdigit()==True]
	if len(d)==0:
		d=map(float,raw_input('Give the numbers to be added:').split())
if a=='float':
	d=[float(x) for x in lines if x.isdigit()==True]
	if len(d)==0:
		d=map(float,raw_input('Give the numbers to be added:').split())

#print a,b,d

code_file.write("#include<stdio.h>\n")
code_file.write("void main(){\n")
if len(c)==0 and len(d)==2:
	
	code_file.write(a+' '+'a='+str(d[0])+';\n')
	code_file.write(a+' '+'b='+str(d[1])+';\n')
	code_file.write(a+' '+'s'+';\n')
	code_file.write('s '+'='+'a+'+'b'+';\n')
	if a=='int' or a=='integer':	
		code_file.write('printf('+'"the sum is equal to : %d"'+',s'+');\n')
	if a=='int' or a=='double':	
		code_file.write('printf('+'"the sum is equal to : %f"'+',s'+');\n')
	if a=='int' or a=='float':	
		code_file.write('printf('+'"the sum is equal to : %lf"'+',s'+');\n')
	
	code_file.write('printf'+'("'+'\\'+'n"'+');\n')
	code_file.write('}\n')


else:
	#declaring an array in c
	code_file.write(a+' '+'ar[]='+str(d)+';\n')
	code_file.write(a+' '+'s'+';\n')
	s=sum(d)
	code_file.write('s='+str(s)+';\n')	
	#code_file.write('printf('+'"the sum is equal to : %d"'+',s'+');\n')
	#code_file.write('printf'+'("'+'\\'+'n"'+');\n')
	code_file.write('}\n')

print 'The name of code :-> "code.c"','\n','to compile the code :->"gcc code.c"','\n','to run the code for output:->"./a.out"','\n','to see the code file created :->"gedit code.c "'





