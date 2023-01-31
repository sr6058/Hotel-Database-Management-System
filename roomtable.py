#roomtable

import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",password="1234",database="project")
if mycon.is_connected():
   print()
mycursor=mycon.cursor()

def createroom():
    try:
        q="create table room(sno int(10),roomno int(3) primary key,type varchar(30),Cost int(15),Status varchar(20))"
        mycursor.execute(q)
        print("Successfully created Room Table")
    except Exception as e:
        print(e)
        mycursor.execute("describe room")
        data=mycursor.fetchall()
        for i in data:
            print(i)

def add():
    s=int(input("Enter Sno:"))
    r_no=int(input("Enter room no.:"))
    ty=input("Enter room type:")
    co=int(input("Enter cost per night:"))
    stat=input("Enter status(BOOKED/AVAILABLE):")
    q="insert into room values({},{},'{}',{},'{}')".format(s,r_no,ty,co,stat)
    mycursor.execute(q)
    mycon.commit()

def display():
    q="select*from room"
    mycursor.execute(q)
    data=mycursor.fetchall()
    print(tabulate(data,headers=["S.No","Room No.","Type","Cost","Status"]))

def seldis():
    q="select sno,type,cost from room where sno in (1,2,3,4)"
    mycursor.execute(q)
    data=mycursor.fetchall()
    print(tabulate(data,headers=["S.No","Type","Cost"]))

def updateroom():
    print("a. Update Room Cost")
    print("b. Update Room Status")
    ch=input("Enter choice:")
    rn=int(input("Enter room number:"))
    if ch=="a":
       c=int(input("Enter new cost:"))
       q1="update room set cost={} where rn={}".format(c,rn)
       mycursor.execute(q1)
       mycon.commit()
    elif ch=="b":
        s="OCCUPIED"
        q2="update room set status='{}' where rno={}".format(s)
        mycursor.execute(q2)
        mycon.commit()
