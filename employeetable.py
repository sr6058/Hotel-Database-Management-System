#Employee table
import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",password="1234",database="project")
if mycon.is_connected():
   print()
mycursor=mycon.cursor()

def createemployee():
     try:
        q="create table employee(employeeid char(2) primary key,name char(50),contact varchar(20),designation varchar(30),salary int(20),grade varchar(2))"
        mycursor.execute(q)
        print("Successfully created employee")
     except Exception as e:
        print(e)
        mycursor.execute("describe employee")
        data=mycursor.fetchall()
        for i in data:
            print(i)

def insertemployee():
    e_id=input("Enter employee id:")
    na=input("Enter name:")
    de=input("Enter designation:")
    c=int(input("Enter contact no.:"))
    sal=int(input("Enter salary:"))
    g=input("Enter employee grade:")
    q="insert into employee values('{}','{}','{}',{},{},'{}')".format(e_id,na,de,c,sal,g)
    mycursor.execute(q)
    mycon.commit()
    
def update():
    print("1. Update name")
    print("2. Update salary")
    print("3. Update Contact No.")
    print("4. Update Grade" )
    choice=int(input("Enter choice:"))
    if choice==1:
        n=input("Enter employee ID:")
        mycursor.execute("select*from employee where employeeid='{}'".format(n))
        data=mycursor.fetchone()
        print(data)
        nname=input("Enter new name:")
        q="update employee set name='{}' where employeeid='{}'".format(nname,n)
        mycursor.execute(q)
        mycon.commit()
        print("Updated Successfully")
    elif choice==2:
        n=input("Enter employee ID:")
        mycursor.execute("select*from employee where employeeid='{}'".format(n))
        data=mycursor.fetchone()
        print(data)
        sa=int(input("Enter new salary:"))
        q="update employee set salary={} where employeeid='{}'".format(sa,n)
        mycursor.execute(q)
        mycon.commit()
        print("Updated Successfully")
    elif choice==3:
        n=input("Enter employee ID:")
        mycursor.execute("select*from employee where employeeid='{}'".format(n))
        data=mycursor.fetchone()
        print(data)
        cn=int(input("Enter new Contact number:"))
        q="update employee set contact={} where employeeid='{}'".format(cn,n)
        mycursor.execute(q)
        mycon.commit()
        print("Updated Successfully")
    elif choice==4:
        n=input("Enter employee ID:")
        mycursor.execute("select*from employee where employeeid='{}'".format(n))
        data=mycursor.fetchone()
        print(data)
        grd=input("Enter new grade:")
        q="update employee set grade='{}' where employeeid='{}'".format(grd,n)
        mycursor.execute(q)
        mycon.commit()
        print("Updated Successfully")
        
def delete():
        n=input("Enter employee id to be deleted:")
        mycursor.execute("select * from employee where employeeid='{}'".format(n))
        data=mycursor.fetchone()
        count=mycursor.rowcount
        if count==0:
            print("Invalid Employee id")
        else:
           print(data)
           print("Are you sure you want to delete this record?")
           ans=input("Enter choice:")
           if ans=="y":
              q="delete from employee where employeeid='{}'".format(n)
              mycursor.execute(q)
              mycon.commit()
              print("Deleted Successfully")
def displayempl():
    mycursor.execute("select * from employee")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Employeeid","Name","Designation","Contact","Salary","Grade"]))
    
     
