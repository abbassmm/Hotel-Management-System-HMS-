'''Encryption...'''
import random
with open('/storage/emulated/0/cs1/code.dat','r') as f:
	s= f.read()
dis=eval(s)
def e(y):
	a=str(y)
	str1=''
	while True:
		for i in range(len(a)):
			if str(a[i]) not in dis:
				b=random.randint(0,50000)
				s=dis.values()
				if b not in s:
					dis[a[i]]=b
					break
					return 
			if i!=len(a)-1:
				i+=1
			else:
				break
				return
		else:
			break
		for i in a:
			if i in dis:
				for j in dis:
					if i==j:
						str1+=str(dis[j])+'%'
			else:
				pass
		return str1
def ecr(a):
    str1=''
    for i in range(len(a)):
        t=e(a[i])
        write()
        str1+=t
    return str1		
def write():
	with open('/storage/emulated/0/cs1/code.dat','w') as f:
		f.write(str(dis))
def dcr(a):
	str1=''
	v=a.split('%')
	for i in v:
		k=i
		for j in dis:
			if str(dis[j])==str(k):
				str1+=j
	return str1

