#Customer and booking info
#roomtable

import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",password="1234",database="project")
if mycon.is_connected():
    print()

mycursor=mycon.cursor()
import roomtable
def crcust():
    try:
        q="create table customer(custid int(5) primary key ,fname varchar(20),lname varchar(30),num int(10),city varchar(50),Roomno int(3) null,total_bill int null)"
        mycursor.execute(q)
        print("Successfully created Customer")
    except Exception as e:
        print(e)
        mycursor.execute("describe customer")
        data=mycursor.fetchall()
        for i in data:
            print(i)

def inscust():
    try:
       cid=int(input("Enter your customer id:"))
    except Exception as e:
        print(e)
        custid()
    
    Fname=input("Enter first name:")
    Lname=input("Enter Surname:")
    no=int(input("Enter phone number:"))
    city=input("Enter your city:")
    rno="null"
    bill=0
    q="insert into customer (custid,fname,lname,num,city,roomno,total_bill)values({},'{}','{}',{},'{}',{},{})".format(cid,Fname,Lname,no,city,rno,bill)
    mycursor.execute(q)
    mycon.commit()
#display customer
def discus():
    mycursor.execute("select * from customer")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Customer_ID","Firstname","Surname","Phone no.","city","Roomno","Total_bill"]))

def deletecus():
    cid=int(input("Enter customer id to be deleted:"))
    q="delete from customer where custid={}".format(cid)
    print("Customer removed")
    mycursor.execute(q)
    mycon.commit()
def search():
    cid=int(input("Enter Customer ID whose details are to be shown:"))
    q="select*from customer where custid={}".format(cid)
    mycursor.execute(q)
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Customer_ID","Firstname","Surname","Phone no.","city","Roomno","Total_bill"]))

def updatee():
   cid=int(input("Enter the customer id whose details is to be updated:"))
   print("1.Update First name")
   print("2.Update Last name")
   print("3.Update number")
   
   ch=int(input("Enter choice:" ))
   if ch==1:
       fn=input("Enter modified first name:")
       q1="update customer set fname='{}' where custid={}".format(fn,cid)
       mycursor.execute(q1)
       mycon.commit()
   elif ch==2:
       ln=input("Enter modified last name:")
       q2="update customer set lname='{}' where custid={}".format(ln,cid)
       mycursor.execute(q2)
       mycon.commit()
   elif ch==3:
       n=int(input("Enter modified phone no.:" ))
       q3="update customer set num={} where custid={}".format(n,cid)
       mycursor.execute(q3)
       mycon.commit()
   
#creation of booking table
def crbkng():
    try:
        q="create table booking(custid int(5) primary key,Roomno int(3) null,arrival date,departure date,totalstay int(5),totalpay int null)"
        mycursor.execute(q)
        print("Successfully created Booking")
    except Exception as e:
        print(e)
        mycursor.execute("describe booking")
        data=mycursor.fetchall()
        for i in data:
            print(i)
def disbkng():
    mycursor.execute("select * from booking")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Customer_ID","Roomno","Date of Arrival","Date of Departure","Total_Stay","Totalpay"]))
def book():
    custid()
    inscust()
    print("We have the following rooms available for you:")
    
    roomtable.seldis()
    x=int(input("Enter preferred type of room (S.No):"))
    n=int(input("Enter no. of days you wish to spend:"))
    s=0
    if x==1:
        s=n*200
        print("You have chosen Delux room")
        p="Delux"
    elif x==2:
        s=n*250
        print("You have chosen Super Delux room")
        p="Super Delux"
    elif x==3:
        s=n*400
        print("You have chosen Presidential Suite")
        p="Presidential Suite"
    elif x==4:
        s=n*350
        print("*You have chosen Junior Suite")
        p="Junior Suite"
    print("*Your room charge is:",s,"aed")
   
    print("Available rooms of your type are :")
    q1="select roomno from room where status='AVAILABLE' and type='{}'".format(p)
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for i in data:
        rn=i
        print(rn)
    upd()
    
    print("**To pay the room price**")
    r=int(input("Enter room no.:"))
    q="update customer set total_bill=total_bill+{} where Roomno={}".format(s,r)
    mycursor.execute(q)
    mycon.commit()
    print("Room price paid !")
def upd():
    print("**Kindly enter the following booking details**")
    ron=int(input("Choose a room no. :"))
    cidd=int(input("Enter your customer id:"))
    qq="update customer set roomno={} where custid={}".format(ron,cidd)
    mycursor.execute(qq)
    mycon.commit()
    print("Updated roomno")
    q="update room set status='OCCUPIED' where roomno={}".format(ron)
    mycursor.execute(q)
    mycon.commit()
    arr=input("Enter check-in date(yyyy-mm-dd):" )
    dep=input("Enter check-out date(yyyy-mm-dd):" )
    from datetime import datetime
    date_format = "%Y-%m-%d"
    a = datetime.strptime(arr, date_format)
    b = datetime.strptime(dep, date_format)
    delta = b - a
    days=delta.days
    q="insert into booking values({},{},'{}','{}',{})".format(cidd,ron,arr,dep,days)
    mycursor.execute(q)
    mycon.commit()
    print("Enjoy your stay at Hotel Secret Mirage!")
   
def checkout():
    r=int(input("Enter your room number:"))
    c=int(input("Enter customer id:"))
    q="select total_bill from customer where roomno={}".format(r)
    mycursor.execute(q)
    data=mycursor.fetchall()
    for i in data:
      print("------------------------------")
      print("Your Final bill is",data,"aed")
      print("------------------------------")
    print("Thanks for visiting!")
    q2="update customer set total_bill=0 and roomno='NULL' where roomno={}".format(r)
    q3="update room set status='AVAILABLE' where roomno={}".format(r)
    q4="update customer set roomno=NULL where custid={}".format(c)
    mycursor.execute(q2)
    mycursor.execute(q3)
    mycursor.execute(q4)
    mycon.commit()
    
def custid():
    mycursor.execute("select * from customer")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    cid=count+1
    print("Your customer id :",cid)
