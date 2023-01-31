
#facilities: Continental hotel,Al Gazebo Hotel,Concierge
import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",password="1234",database="project")
if mycon.is_connected():
  
    print()
mycursor=mycon.cursor()

#CREATION 
def crcon():
    try:
        q="create table continental(item_no int(2) primary key,Description varchar(50),cost decimal(6))"
        mycursor.execute(q)
        print("Successfully created Continental")
    except Exception as e:
        print(e)
        mycursor.execute("describe continental")
        data=mycursor.fetchall()
        for i in data:
            print(i)
            
def crgaz():
    try:
        q="create table algazebo(item_no int(2) primary key,Description varchar(50),cost decimal(6))"
        mycursor.execute(q)
        print("Successfully created Al Gazebo")
    except Exception as e:
        print(e)
        mycursor.execute("describe algazebo")
        data=mycursor.fetchall()
        for i in data:
            print(i)
def crconci():
    try:
        q="create table concierge(carno int(4) primary key,type varchar(30),seats int(5),rateperkm decimal(6))"
        mycursor.execute(q)
        print("Successfully created Concierge Table")
    except Exception as e:
        print(e)
        mycursor.execute("describe concierge")
        data=mycursor.fetchall()
        for i in data:
            print(i)
#INSERT    
def inscon():
        itno=int(input("Enter item no.:"))
        des=input("Enter description:")
        co=int(input("Enter cost:"))
        mycursor.execute("insert into continental values({},'{}',{})".format(itno,des,co))
        mycon.commit()
def insalg():   
        itno=int(input("Enter item no.:"))
        des=input("Enter description:")
        co=int(input("Enter cost:"))
        mycursor.execute("insert into algazebo values({},'{}',{})".format(itno,des,co))
        mycon.commit()
def insconc():   
        can=int(input("Enter car number :"))
        typ=input("Enter company/type of car:")
        se=int(input("Enter no. of seats:"))
        rate=int(input("Enter rate per km :"))
        mycursor.execute("insert into concierge values({},'{}',{},{})".format(can,typ,se,rate))
        mycon.commit()
def discont():
    mycursor.execute("select * from continental")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Item_No.","Description(V-Veg/N-Non veg)","Cost(AED)"]))
def disalg():
     mycursor.execute("select * from algazebo")
     data=mycursor.fetchall()
     print(tabulate(data,headers=["Item_No.","Description","Cost(AED)"]))
def discon():
     mycursor.execute("select * from concierge")
     data=mycursor.fetchall()
     print(tabulate(data,headers=["Car No.","Company/Type","No. of seats","Rate(per km)"]))
   
def conpr():
     r=int(input("Enter room no. :"))
     ts=0
     ans="y"
     while ans=="y":
         p=0
         discont()
        
         ch=int(input("Enter item no.:"))
         n=int(input("Enter qty:"))
         if ch==1:
             p=n*7
         elif ch==2:
             p=n*5
         elif ch==3:
             p=n*12
         elif ch==4:
             p=n*8
         elif ch==5:
             p=n*8
         elif ch==6:
             p=n*10
         elif ch==7:
             p=n*8
         elif ch==8:
             p=n*8
         elif ch==9:
             p=n*6
         elif ch==10:
             p=n*20
         ts=ts+p
         ans=input("Want to order more items?(y/n):")
         if(ans.upper()=='N'):
             break
     print("Your total bill:",ts,"aed")
     q="update customer set total_bill=total_bill+{} where roomno={}".format(ts,r)
     mycursor.execute(q)
     mycon.commit()
   

def algpr():
     r=int(input("Enter room no. :"))
     ts=0
     ans="y"
     while ans=="y":
         p=0
         disalg()
        
         ch=int(input("Enter item no.:"))
         n=int(input("Enter qty:"))
         if ch==1:
             p=n*20
         elif ch==2:
             p=n*15
         elif ch==3:
             p=n*20
         elif ch==4:
             p=n*13
         elif ch==5:
             p=n*10
         elif ch==6:
             p=n*15
         elif ch==7:
             p=n*16
         elif ch==8:
             p=n*12
         elif ch==9:
             p=n*10
         elif ch==10:
             p=n*20
         ts=ts+p
         ans=input("Want to order more items?(y/n):")
         if(ans.upper()=='N'):
             break
     print("Your total bill:",ts,"aed")
     q="update customer set total_bill=total_bill+{} where roomno={}".format(ts,r)
     mycursor.execute(q)
     mycon.commit()
     

def concpr():
     discon()
     r=int(input("Enter room no. :"))
     d=int(input("Enter distance(km):"))
     ch=int(input("Enter car no.:"))
     p=0
     if ch==1:
         p=d*2
     elif ch==2:
         p=d*7
     elif ch==3:
         p=d*15
     elif ch==4:
         p=d*7
     print("Total rate:",p,"aed")
     q="update customer set total_bill=total_bill+{} where roomno={}".format(p,r)
     mycursor.execute(q)
     mycon.commit()
     
         
