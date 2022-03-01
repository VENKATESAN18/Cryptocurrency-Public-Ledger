#source code for crypto management
print("\t--------------------------------------------------------------")
print("\t---------------Welcome to Cryptocurrency ledger---------------")
print("\t--------------------------------------------------------------")
#modules
import mysql.connector
import random
import datetime
from tabulate import tabulate
#connector
CC=mysql.connector.connect(host="localhost",user="root",passwd="root")
C=CC.cursor()
#C is mycursor CC is connect = my database
#creating table
C.execute("create database if not exists Cryptocurrency")
C.execute("use Cryptocurrency")
C.execute("create table if not exists Login(USID int not null, password varchar(25) not null)")
C.execute("create table if not exists User(USID int not null, Name varchar(25) not null, Address varchar(25) not null, Numberoftokens int, balance int)")
C.execute("create table if not exists Ledger(Date date, TransactionNumber int not null, SendersAddress varchar(25) not null, ReciversAddress varchar(25) not null, Numberoftokens int, SendersBalance int not null, ReciversBalance int not null)")
C.execute("create table if not exists assign(USID int not null, Address varchar(25))")
#Addind new things to table
C=CC.cursor(buffered=True)
CC.commit()
j=0
C.execute("select * from login")
for i in C:
    j=1
if j==0:
    C.execute("insert into login values('0001','password')")
    CC.commit()
k=0
C.execute("select * from assign")
for i in C:
    k=1
if k==0:
    C.execute("insert into assign values('0001','amk182makik')")
    CC.commit()
l=0
C.execute("select * from user")
for i in C:
    l=1
if l==0:
    C.execute("insert into user values('0001','test','amk182makik','0','0')")
    CC.commit()
m=0
C.execute("select * from ledger")
for i in C:
    m=1
if m==0:
    tday= datetime.date.today()
    C.execute("insert into ledger values('"+str(tday)+"',00001,'amk182makik','amk182makik','0','0','0')")
    CC.commit()
#Interface
while True :
    print("\t------------------------1-Create Account-1--------------------")
    print("\t---------------------------2-Login-2--------------------------")
    print("\t---------------------------3-Exit-3---------------------------")
    print("\t---------------------------4-Ledger-4-------------------------")
    print("\t-----------------------------Choice---------------------------")
    ch=int(input())
    if ch ==1:
        print("\t--------------------------------------------------------------")
        print("\t-----------------------------Create---------------------------")
        print("\t--------------------------------------------------------------")
        name=input("\t----------------------------Enter your name--------------")
        print("\t--------------------------------------------------------------")
        pasd=input("\t----------------------------Create your password--------------")
        print("\t--------------------------------------------------------------")
        C.execute("select * from assign")
        for i in C:
            (nid,adr)=i
            l=[]
            l.append(adr)
        nid+=1
        rl=[random.randint(65,122) for _ in range(10)]
        rsl=list(map(chr,rl))
        rs=''.join(rsl)
        if rs in l:
            rl=[random.randint(65,122) for _ in range(10)]
            rsl=list(map(chr,rl))
            rs=''.join(rsl)
        else:
            pass

        nt=0
        bal=0
        print("\t-------------------------User id------------------------------",nid)
        print("\t--------------------------------------------------------------")
        print("\t-------------------------Address------------------------------",rs)
        C=CC.cursor(buffered=True)
        C.execute("insert into login values('"+str(nid)+"','"+str(pasd)+"')")
        CC.commit()
        C.execute("insert into assign values('"+str(nid)+"','"+str(rs)+"')")
        CC.commit()
        C.execute("insert into user values('"+str(nid)+"','"+name+"','"+str(rs)+"','"+str(nt)+"','"+str(bal)+"')")
        CC.commit()
        print("\t--------------------------------------------------------------")
        print("\t-----------------------------Created--------------------------")
        print("\t--------------------------------------------------------------")
    if (ch == 2):
        print("\t--------------------------------------------------------------")
        print("\t-----------------------------Login----------------------------")
        print("\t--------------------------------------------------------------")
        us=int(input("Enter USID"))
        print("\t--------------------------------------------------------------")
        print("\t-----------------------Enter the password---------------------")
        print("\t--------------------------------------------------------------")
        pasd=input("Enter Password")
        C.execute("select * from login")
        for i in C:
            ad,pas=i
            if us==ad and pasd==pas :
                while True:
                    print("\t--------------------------------------------------------------")
                    print("\t-----------------------Successfully Login---------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t---------------------5-Deposit-5------------------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t---------------------6-Transact-6-----------------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t---------------------7-Display Account-7----------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t---------------------8-Log-Out-8------------------------------")
                    print("\t--------------------------------------------------------------")
                    print("\t------------------------------Choice----------------------------")
                    ch=int(input())
                    if ch == 5:
                        C=CC.cursor(buffered=True)
                        C.execute("select balance from user WHERE USID = '"+str(us)+"'")
                        for i in C:
                            (bale,)=i
                        nt=int(input("------------------------------Enter the N.O of tokens----------------------------"))
                        bale=nt+bale
                        C.execute("update user set Numberoftokens = '"+str(bale)+"', balance = '"+str(bale)+"' WHERE USID = '"+str(us)+"'  ")
                        CC.commit()
                        print("Balance - ",bale)
                        print("\t--------------------------------------------------------------")
                        print("\t-----------------------------deposited------------------------")
                        print("\t--------------------------------------------------------------")
                    if ch == 6:
                        C=CC.cursor(buffered=True)
                        recadd=input("Enter the Address to send tokens")
                        nots=int(input("Enter the number of tokens to be transacted!"))
                        C.execute("select TransactionNumber from ledger ")
                        for i in C:
                            (txno,)=i
                        txno+=1
                        CC.commit()
                        C.execute("select Name, Address, Numberoftokens, balance from user WHERE USID = '"+str(us)+"'")
                        sedadd='dewsed'
                        for i in C:
                            (name,sedadd,notis,balis)=i
                        CC.commit()
                        C.execute("select USID, Numberoftokens, balance from user WHERE Address = '"+str(recadd)+"'")
                        for i in C:
                            (usr,notir,balir)=i
                        CC.commit()
                        balis=balis-nots
                        notis=notis-nots
                        C.execute("update user set Numberoftokens = '"+str(notis)+"', balance = '"+str(balis)+"' WHERE USID = '"+str(us)+"'  ")
                        CC.commit()
                        notir=notir+nots
                        balir=balir+nots
                        daot=datetime.date.today()
                        C.execute("update user set Numberoftokens = '"+str(notir)+"', balance = '"+str(balir)+"' WHERE USID = '"+str(usr)+"'  ")
                        CC.commit()
                        C.execute("insert into ledger values('"+str(daot)+"','"+str(txno)+"','"+sedadd+"','"+recadd+"','"+str(nots)+"','"+str(balis)+"','"+str(balir)+"')")
                        CC.commit()
                        print("\t--------------------------------------------------------------")
                        print("\t-----------------------------Transacted-----------------------")
                        print("\t--------------------------------------------------------------")
                    if ch ==7:
                        C=CC.cursor(buffered=True)
                        print("\t-----------------------------Account--------------------------")
                        C.execute("select * from user WHERE USID = '"+str(us)+"'  ")
                        for i in C:
                            l=[]
                            i1=list(i)
                            i2=["USID","Name","Address","Numberoftokens","balance"]
                            l.append(i2)
                            l.append(i1)
                            print(tabulate(l))  
                    if (ch == 8):
                        C=CC.cursor(buffered=True)
                        print("\t--------------------------------------------------------------")
                        print("\t-----------------------------Log-Out--------------------------")
                        print("\t--------------------------------------------------------------")
                        break
            elif us==ad and pasd!=pas :
                print("\t--------------------------------------------------------------")
                print("\t-----------------------Incorrect Password---------------------")
                print("\t--------------------------------------------------------------")
            elif us!=ad and pasd==pas :
                print("\t--------------------------------------------------------------")
                print("\t-----------------------Incorrect USID ------------------------")
                print("\t--------------------------------------------------------------")
            else:
                pass
    if (ch == 3):
        print("\t--------------------------------------------------------------")
        print("\t-----------------------------Exit-----------------------------")
        print("\t--------------------------------------------------------------")
        break
    if (ch == 4):
        print("\t--------------------------------------------------------------")
        print("\t-----------------------------LEDGER---------------------------")
        print("\t--------------------------------------------------------------")
        C.execute("select * from Ledger")
        for i in C:
            l=[]
            i1=list(i)
            i2=["Date","TransactionNumber","SendersAddress","ReciversAddress","Numberoftokens","SendersBalance","ReciversBalance"]
            l.append(i2)
            l.append(i1)
            print(tabulate(l))
    if ch == 5 or ch==6 or ch==7 :
        break


            
        
   


