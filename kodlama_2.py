a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = a-b*c+d

if a>b:
	if a>c:
	    print(c*d)
	elif a<b:
	    print(a+e-c)
	else:
	     print(b)
elif a<c:
	print(a+e)
else:
	print(a+b+c+d+e)
