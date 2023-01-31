import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",password="1234",database="project")
if mycon.is_connected():
    print("*Successfully connected*")
    print()
mycursor=mycon.cursor()



def createcustomer():
    try:
        q="create table customer(customerid int(2) primary key,firstname varchar(10),lastname varchar(20),phone int,checkin_date date,checkout_date date,Amount_paid int)"
        mycursor.execute(q)
        print("Successfully created Customer")
    except Exception as e:
        print(e)
        mycursor.execute("describe customer")
        data=mycursor.fetchall()
        for i in data:
            print(i)



def insertcustomer():
    c_id=int(input("Enter customer id:"))
    f_na=input("Enter first name:" )
    l_na=input("Enter last name:")
    no=int(input("Enter phone no.:"))
    cin=input("Enter check-In Date (dd/mm/yy):" )
    cout=input("Enter check-Out Date (dd/mm/yy):" )
    Amt=int(input("Enter amount paid by customer:"))
    q="insert into customer values({},'{}','{}',{},'{}','{}',{})".format(c_id,f_na,l_na,no,cin,cout,Amt)
    mycursor.execute(q)
    mycon.commit()

#def createroom():
#def createrestraunt():
    
def detailshotel():
    print("Hotel Secret Mirage,Dubai is home to 20 luxurious rooms including 5 suites, ranging from 39 square meters to 264 square meters. ")
    print("Towering majestically over the edge of Dubai's historic creek or overlooking the glorious Dubai skyline, this city resort offers the comfort and convenience that you seek.")
    print("Amenities such as Swimming pools,Gyms and playareas are also available.")
    print("Hotel Name: Hotel Secret Mirage")
    print("Address: Riyadh Street,Sheikh Zayed Road, Dubai, United Arab Emirates")
    print("Contact: +971 42475344")
    print("Email: dubai.secret@mirage.com")
    

#mainmenu:
print("**************************     Welcome to Hotel Secret Mirage    *****************************")
print()
user=input("Enter user(Admin/Customer):")
if user=="Admin":
    pasw=input("Enter password")
    if pasw=="1234":
        print("Welcome Admin")
        import employeetable
        ans="y"
        while ans=="y":
            print("1.View Employee Details")
            print("2.Add new Employee")
            print("3.Modify Employee Details")
            print("4.Delete Employee Record")
            choice=int(input("Enter choice(1/2/3/4):"))
            if choice==1:
                employeetable.displayempl()
            elif choice==2:
                employeetable.insertemployee()
            elif choice==3:
                employeetable.update()
            elif choice==4:
                employeetable.delete()
        ans=input("Do you want to continue?")
                
        
    
