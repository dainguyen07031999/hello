import stdio
import math
stdio.write('Nhap mot so: ')
n = stdio.readInt()
count = 0
i = 2
while count < n:
	flag = True
	c = int(math.sqrt(i))
	for k in range(2, c+1):
		if i % k == 0:
			flag = False
			break 
	if flag:
		count = count + 1
	if (count < n):
		i = i + 1
stdio.writeln('So nguyen to thu ' + str(n) + ' la: ' + str(i))
// Make by me
