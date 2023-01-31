import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",password="1234",database="project")
if mycon.is_connected():
    print("*Successfully connected*")
    print()
mycursor=mycon.cursor()
import customernbooking
import facilities
import employeetable
import roomtable
    
def detailshotel():
    print("                                                                     HOTEL SECRET MIRAGE                      " )
    print("                                                                    *********************                      ")
    print("Hotel Secret Mirage,Dubai is home to 14 luxurious rooms including 6 suites, ranging from 39 square meters to 264 square meters. ")
    print("Towering majestically over the edge of Dubai's historic creek or overlooking the glorious Dubai skyline, this city resort offers the comfort and convenience that you seek.")
    print("Amenities such as Swimming pools,Gyms and play areas are also available.")
    print()
    print("Hotel Name: Hotel Secret Mirage")
    print("Address: Riyadh Street,Sheikh Zayed Road, Dubai, United Arab Emirates")
    print("Contact: +971 42475344")
    print("Email: dubai.secret@mirage.com")

#mainmenu:
print("**************************     Welcome to Hotel Secret Mirage    *****************************")
print()
user=input("Enter user(Admin/Customer):")
if user.lower()=="admin":
    olp=input("Enter current password:")
    q1="select * from pass"
    mycursor.execute(q1)
    data=mycursor.fetchall()
    for i in data:
     
     if olp==i[0]:
      ch=input("Want to change password?")
      if ch=="y":
            np=input("Enter new password:")
            q="update pass set pass={}".format(np)
            mycursor.execute(q)
            mycon.commit()
            print("Password Updated!")
      else:
       ans="y"
       while ans=="y":
        print()
        print("--------------  Welcome Admin  ----------------                 ")
        print("1.Employee Management")
        print("2.Room Information")
        print("3.Continental Restaurant Info." )
        print("4.Al Gazebo Restaurant Info." )
        print("5.Concierge Info.")
        print("6.Edit Customer Details" )
        print("7.View Bookings")
        print("-----------------------------------------------                 ")
        ch=int(input("Enter choice:"))
        if ch==1:
             print("1.View Employee Details")
             print("2.Add new Employee")
             print("3.Modify Employee Details")
             print("4.Delete Employee Record")
             choice=int(input("Enter choice(1/2/3/4):"))
             if choice==1:
                employeetable.displayempl()
             elif choice==2:
                employeetable.insertemployee()
                print("Employee Added!")
             elif choice==3:
                employeetable.update()
                print("Employee Details updated!")
             elif choice==4:
                employeetable.delete()
                print("Employee deleted!")
        elif ch==2:
            print("View Room Details:")
            roomtable.display()
        elif ch==3:
           print("View Menu:")
           facilities.discont()
            
        elif ch==4:
            print("View Menu")
            facilities.disalg()
            
        elif ch==5:
            print("View Table:")
            facilities.discon()
        elif ch==6:
             print("a.View Customer table")
             print("b.Search for customer details")
             print("c.Update customer details")
             ans=input("Enter choice(a/b/c):")
             if ans=="a":
                 customernbooking.discus()
             elif ans=="b":
                  customernbooking.search()
             elif ans=="c":
                 customernbooking.updatee()
        elif ch==7:
            customernbooking.disbkng()
        else:
            print("Enter valid choice!")
        
        ans=input("Do you want to continue?")
        if ans=="n":
          print("Exiting,Thank You!")
     else:
        print("Invalid Password!")
elif user.lower()=="customer":
   ans="y"
   while ans=="y":
    print()
    print("----------------------  Welcome Customer  -------------------------")
    print("MAIN MENU")
    print("1.Hotel information")
    print("2.Check In")
    print("3.View continental restaurant bill")
    print("4.View Al Gazebo restaurant bill")
    print("5.View concierge bill")
    print("6.Check out")
    print("-------------------------------------------------------------------")
    ch=int(input("Enter choice:"))
    if ch==1:
        detailshotel()
    elif ch==2:
        customernbooking.book()
    elif ch==3:
        print("Welcome to Continental Restaurant!")
        facilities.conpr()
    elif ch==4:
        print("Welcome to Al Gazebo Restaurant!")
        
        facilities.algpr()
    elif ch==5:
        print("**Concierge Services**")
        
        facilities.concpr()
    elif ch==6:
        
        print("We hope you had a pleasant stay")
        print("Do come again and enjoy your day!")
        customernbooking.checkout()
    ans=input("Do you want to continue?")
    if ans=="n":
     print("Exiting!") 
        
       
            
    
           
        
                
        
    
