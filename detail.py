import enc_dcr
def room_detail():
        with open('/storage/emulated/0/\
cs1/detail.txt') as d:
            b=d.read()
            a=enc_dcr.dcr(b)
            c=eval(a)
        return c
def cust_detail(a):
    with open('cust_details.txt','w') as f:
        data=enc_dcr.ecr(str(a))
        f.write(data)
def cust_detail_read():
    try:
        with open('cust_details.txt','r') as f:
            a=f.read()
        return eval(enc_dcr.dcr(a))
    except SyntaxError:
        a=[]
        return a
def updt_room_detail(a):
    b=int(str(a)[0])
    s=room_detail()
    x=s[0][b][3].pop(0)
    s[1].append(x)
    with open('detail.txt','w') as d:
        d.write(enc_dcr.ecr(str(s)))
def updt_room_out(a):
    b=int(str(a)[0])
    s=room_detail()
    x=s[0][b][3].append(a)
    s[1].remove(a)
    with open('detail.txt','w') as d:
        d.write(enc_dcr.ecr(str(s)))
def food_read():
    with open(r'/storage/emulated/0/cs1/food.txt','r') as a:
        return eval(enc_dcr.dcr(a.read()))