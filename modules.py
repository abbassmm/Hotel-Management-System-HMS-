#pylint:disable=E0602
'''ALL MODULES'''
import time as t
from termcolor import colored as cd
from datetime import date as d
import datetime as dt
from tabulate import tabulate as tab
from detail import *
def check():
        '''CHECK IN'''
        print()
        print(cd('CHECKING FOR A\
VAILABILITY OF ROOMS:-','yellow','on_black',['bold','dark']))
        t.sleep(2)
        a=room_detail()
        for j in range (1,5):
                print()
                if len(a[0][j][3])>0:
                    print(cd(f'''{j}. ROOM TYPE - {a[0][j][1]}
ROOM PRICE - {a[0][j][2]} Rs. / NIGHT
ROOM VACANT - {len(a[0][j][3])} ''','green','on_black',['bold','dark']))
                else:
                    print(cd(f'''{j}. ROOM TYPE - {a[0][j][1]}
ROOM PRICE - {a[0][j][2]} Rs. / NIGHT
ROOM VACANT - {len(a[0][j][3])} ''','red','on_black',['bold','dark']))
                t.sleep(1)
        print()
        print(cd('5. EXIT','yellow','on_black',['bold','dark']))
        print()
        ch=int(input(cd('ENTER: ','blue','on_white',['bold','dark'])))
        if str(ch) in '1234':
            check_in(ch)
        elif ch==5:
            return
        else:
            print(cd('YOU ENTERED A W\
RONG VALUE, TRY AGAIN!','red','on_white',['bold','dark']))
        return
def check_in(a):
    '''FOR CHECK IN'''
    print(cd('FORWARDING TO CHECK IN PAGE:-','yellow','on_black',['bold','dark']))
    t.sleep(2)
    print(cd('FILL THE FOLLOWING DETAILS:-','blue','on_white',['bold','dark','underline']))
    n=int(input(cd('ENTER NUMBER OF GUEST \
(4 GUESTS ARE ALLOWED AT MAX): ','blue','on_white',['bold','dark'])))
    if str(n) in '1234':
        pass
    else:
        print(cd('YOU ENTERED A WRONG NUMBER, TRY AGAIN!','red','on_white',['bold','dark']))
        return
    d=cust_detail_read()
    q=[]
    for i in range(1,n+1):
        print()
        name=input(cd(f'ENTER NAME OF GUEST {i}: ','blue','on_white',['bold','dark']))
        age=int(input(cd(f'ENTER AGE OF GUEST {i}: ','blue','on_white',['bold','dark'])))
        gen=input(cd(f'ENTER GENDER OF GUEST {i} (M/F/O): ','blue','on_white',['bold','dark']))
        if gen in 'MFO':
            q.append([name,age,gen])
        else:
            print(cd('Entered Inappropriate gender:-','red','on_white',['bold','dark']))
            return
        print()
    addr=input(cd('ENTER ADDRESS: ','blue','on_white',['bold','dark']))
    phn=int(input(cd('ENTER A 10 DIGIT PHONE NUMBER: ','blue','on_white',['bold','dark'])))
    dte=input(cd('ENTER CHECK IN DATE (YYYY-MM-DD): ','blue','on_white',['bold','dark']))
    l=str(dt.datetime.now())[0:11]
    if len(str(phn))==10 and dte>=l:
        b=room_detail()
        room=b[0][a][3][0]
        l=[]
        l.append(q)
        l.extend([addr,phn,dte,room,0])
        d.append(l)
        print()
        print(cd(f'YOUR CHECK IN IS SUCCESSFULL\
\nYOUR ROOM NUMBER IS {room}','green','on_black',['bold','dark']))
        print()
        updt_room_detail(room)
        cust_detail(d)
    elif len(str(phn))!=10:
        print(cd('YOU ENTERED A WRONG PHONE NUMBER, TRY AGAIN!','red','on_white',['bold','dark']))
    elif  dte>=l:
        print(cd('YOU ENTERED A WRONG DATE, TRY AGAIN!','red','on_white',['bold','dark']))
    return
def serve():
    '''ROOM SERVICE'''
    room_num=int(input(cd('ENTER YOUR ROOM NUMBER: ','blue','on_white',['bold','dark'])))
    t_r=room_detail()
    if room_num in t_r[1]:
        a=food_read()[int(str(room_num)[0])]
        j=1
        for i in a:
            print(cd(f'''{j}.Food Type: {a[i][0]}
1.Price Per Plate (veg): {a[i][1]}
2.Price Per Plate (non-veg): {a[i][2]}
''','blue','on_white',['bold','dark']))
            t.sleep(0.5)
            j+=1
        print(cd('''Enter as (Food type number,veg/nonveg,n_plates) for example:
 2,1,4 means Lunch,Veg,4 Plates:-''','blue','on_white',['bold','dark']))
        srv=input(cd('WHAT YOU WANT (FT,V_NV,PLT): ','blue','on_white',['bold','dark']))
        data=srv.split(',')
        amt1=food_read()[int(str(room_num)[0])][int(data[0])][int(data[1])]
        if data[0] in '123' and data[1] in '12':
            for i in cust_detail_read():
                if i[-2]==int(room_num):
                    amt=i[-1]
                    break
            amt=amt+(int(amt1)*int(data[2]))
            print()
            print(cd('YOU WILL RECIEVE YOUR ORDER SOON:-','green','on_black',['bold','dark']))
            print()
    else:
          print(cd('ENTER A CORRECT ROOM NUMBER:-','red','on_white',['bold','dark']))
    a=cust_detail_read()
    for i in a:
        if i[-2]==int(room_num):
            i[-1]=amt
    cust_detail(a)
def check_out():
    '''Check out'''
    b=cust_detail_read()
    room_num=input(cd('ENTER YOUR ROOM NUMBER: ','blue','on_white',['bold','dark']))
    t_r=room_detail()
    if int(room_num) in t_r[1] and room_num.isnumeric():
        while True:
            dt=input(cd('ENTER DATE OF CHECK OUT (YYYY-MM-DD): ','blue','on_white',['bold','dark']))
            for i in b:
                if int(i[-2])==int(room_num):
                    break
            if dt>=str(b[b.index(i)][-1]):
                v=str(b[b.index(i)][-1])
                chi_dt=d(int(v[0:4]),int(v[5:7]),int(v[8:10]))
                cho_dt=d(int(dt[0:4]),int(dt[5:7]),int(dt[8:10]))
                diff=int((cho_dt-chi_dt).days)
                if diff==0:
                    diff=1
                am=int(b[b.index(i)][-2])
                y=room_detail()
                o=int(str(room_num)[0])
                amt=y[0][o][2]
                am+=int(amt)*int(diff) 
                b[b.index(i)][-1]=am
                b[b.index(i)].append(dt)
                cust_detail(b)
                updt_room_out(int(room_num))
                bill(b[b.index(i)])
                print()
                print(cd(f'YOU HAVE BEEN SUCCESSFULLY CHECKED OUT\nYOUR BILL IS {am} Rs.','green','on_black',['bold','dark']))
                print()
            else:
                print(cd('YOU HAVE ENTERED A WRONG DATE PLS TRY AGAIN:-','red','on_white',['bold','dark']))
            break
    else:
        if not room_num.isnumeric():
            print(cd('Room  Number is always a Number:-','red','on_white',['bold','dark']))
        else:
             print(cd('Enter a correct Room Number:-','red','on_white',['bold','dark']))
        return
def bill(a):
    table=tab(a[0],headers=['NAME','AGE','GENDER'],tablefmt='simple')
    tym=str(dt.datetime.now())[0:19]
    billo=(
f'''THE HOTEL
=== =====
ROOM NUMBER: {a[-3]}
===== =======
{table}

ADDRESS: {a[1]}
======= 
CONTACT NUMBER: {a[2]}
=======  ======= 
CHECK-IN DATE: {a[3]}
======== =====
CHECK-OUT DATE: {a[-1]} (11:00 AM)
========= =====
PAYABLE AMOUNT: {a[-2]} Rs.
======= ======== 




AUTHORISED SIGNATURE: 
==========  ==========

This bill is made at : {tym}''')
    with open(f'{a[0]}_bill.txt','w') as x:
       x.write(billo)