'''Endecryption'''
from ast import literal_eval
import random
with open('/storage/emulated/\
0/cs1/encrypted.dat') as d:
    data=literal_eval(d.read())
def ecr(al_):
    '''Encryption'''
    str1=''
    for i in al_:
        if i in list(data.keys()):
            for j in list(data.items()):
                if j[0]==i:
                    num=j[1]
                    str1+=str(num)+'%'
        else:
             num=random.randint(100000,999999)
             data[i]=num
             str1+=str(num)+'%'
    with open('/storage/emula\
ted/0/cs1/encrypted.dat','w') as file_:
        file_.write(str(data))
    return str1
def dcr(al_):
    '''Decryption'''
    dat_=al_.split('%')
    dat_.pop(len(dat_)-1)
    hel_=''
    for i in dat_:
        for j in list(data.items()):
            if int(i)==j[1]:
                hel_+=j[0]
    return hel_

    