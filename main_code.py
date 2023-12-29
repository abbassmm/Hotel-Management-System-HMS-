'''Main code'''
import time as t
from termcolor import colored as cd
from modules import  *
def main_code():
    '''CHOICE MODULE'''
    print(cd('WELCOME TO THE HOTEL:-\
', 'cyan','on_black',['bold','dark','underline']))
    t.sleep(0.5)
    while True:
        #try:
            chc=int(input(cd('''WHAT YOU WANT TO DO?
1. CHECK IN
2. ROOM SERVICE
3. CHECK OUT
4. EXIT
ENTER: ''','blue','on_white',['bold'])))
            if chc==1:
                check()
            elif chc==2:
                serve()
            elif chc==3:
                check_out()
            elif chc==4:
                print()
                print(cd('THANKS FOR VISITING, \
HAVE A NICE DAY!','green','on_black',['bold']))
                break
            else:
                 print(cd('YOU ENTERED \
A WRONG VALUE, TRY AGAIN!','red','on_white',['bold']))
'''except ValueError as a:
            print(a)
            print(cd('YOU ENTERED \
A WRONG CHARACTOR, TRY AGAIN!','red','on_white',['bold']))'''
main_code()