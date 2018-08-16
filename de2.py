import sys
import stdio
n=int(sys.argv[1])
i=2
j=2
if n<1: 
	stdio.writeln('error')
else:
	while j<n:
	flag=True 
		while i<j:
			if j%i==0:
				flag=False
				i=i+1
		j=j+1
	if flag==True:
		stdio.writeln(str(j))
