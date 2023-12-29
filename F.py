'''Printing a string'''
import time
i=''
CONST=0
ALPH='ABCDEFGHIKLMNOPQRS\
TUVWXYZabcdefghijklmnopqrstuvwxyz\
0123456789'
word=input('Enter A String: ')
while i!=word:
    for j in ALPH:
                if j==word[CONST]:
                    i+=j
                    print("  '"+i+"'",end='\r')
                    break
                print(' '+i+j,end='\r')
                time.sleep(0.075)
    else:
        i+=word[CONST]
        print("  '"+i+"'",end='\r')
    CONST+=1
    