#INTRO PAGE
def intro():
    
    print('-'*50)
    print('Siup Ris Management Software 2024-25')
    print('-'*50)
    print('1. Create User')                                     #Displaying Menu Options  
    print('2. Login')                                        
    print('3. Quit')
    choice=input('Enter choice')
    print()
    
    if choice=='1':
        db=input('Enter username')
        import mysql.connector as mysql
        Mydb=mysql.connect(host='localhost',user='root',password='1234')        #Creating Database
        com='Create database {};'.format(db)
        mycursor=Mydb.cursor()
        try:
            mycursor.execute(com)                               #Error Handling for Creating Existing Database
        except:
            print('Username already exists')
        passwd=input('Enter password')
        com="Create table Password(Password varchar(150);"
        mycursor.execute(com)
        com="Insert into Password values('{}')".format(passwd)
        mycursor.execute(com)
        print('User created successfully')
        
    elif choice=='2':
        db=input('Enter Username')
        
        import mysql.connector as mysql
        Mydb=mysql.connect(host='localhost',user='root',password='1234')
        com='use {};'.format(db)                                        #Selecting an existing Database
        mycursor=Mydb.cursor()
        mycursor.execute(com)
        passwd=input('Énter passwd')
        mycursor.execute("Select * from Password;")
        rec=mycursor.fetchall()
        if passwd==rec[0][0]:
            try:
                mycursor.execute(com)   
                global c
                c='Initiate'                                   #To signal LMS is ready to use
                print('Username chosen sucessfully')
                global database
                database=db
            except:
                print('User doesn\'t exist')                     #Error Handling for Using Non-existitent Database
        else:
            print('Wrong Password')

    elif choice=='3':
        print('Thank you for using Siup Ris Management Software')
        c='End'
    else:
        print('Invalid input')

#DISPLAYING MENU OPTIONS OF LMS
def menu():
    print('-'*50)
    print('Siup Ris Management Software 2024-25 DATABASE: {}'.format(database))
    print('-'*50)
    print('1. Manage Books')
    print('2. Manage Members')
    print('3. Exit')
    choice=input('Enter choice ')
    print()
    global C
    C=''
    if choice=='1':
        C='Books'
    elif choice=='2':
        C='Members'
    elif choice=='3':
        C='Quit'

#DISPLAYING BOOK MANAGEMENT OPTIONS
def booksmenu():
    print('-'*100)
    print('Siup Ris Management Software 2024-25 DATABASE: {} OPTION: Books'.format(database))
    print('-'*100)
    print('1. Add Book')
    print('2. View Book')
    print('3. Borrow Book')
    print('4. Return Book')
    print('5. Delete Books')
    print('6. Exit')
    choice=input('Enter Choice')
    print()
    global C
    if choice=='1':
        addbook()
    elif choice=='2':
        viewbook()
    elif choice=='3':
        registerbook()
    elif choice=='4':
        returnbook()
    elif choice=='5':
        deletebook()
    elif choice=='6':
        C='Exit'
    else:
        print('Invalid Input')

        
#DATABASE INITIALISATION FOR BOOKS
def Initializebook():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    try:
        com='Create table Primary_Table(Book_ID char(7) Primary Key, Name_of_Book varchar(150), Author varchar(150), Genre varchar(150), Status varchar(150));'
        mycursor.execute(com)
    except:
        pass
    try:
        com='Create table Borrowed_Table(Book_ID char(7) Primary Key, Name_of_Book varchar(150), Borrower varchar(150), Date_Borrowed date, Expected_Return_Date date);'
        mycursor.execute(com)
    except:
        pass
    try:
        com='Create table Available_Table(Book_ID char(7) Primary Key, Name_of_Book varchar(150), Author varchar(150), Genre varchar(150));'
        mycursor.execute(com)
    except:
        pass

#DATABASE INITIALISATION FOR MEMBERS
def Initializemember():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    try:
        com='Create table Member_Table(Member_ID char(7) Primary Key,Name varchar(150),Passport_No char(8),DOB date,Address varchar(300),Fee_Status varchar(150),Book_Borrowed varchar(150));'
        mycursor.execute(com)
    except:
        pass
    

#ADD BOOKS
def addbook():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    BOOKS_Id=input("(Format: #WRD_No) enter book id")
    Name_of_Book=input("enter book name")
    Author=input("enter author")
    Genre=input("enter genre")
    Status="Available"
    try:
        Record="insert into Primary_Table values(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(BOOKS_Id,Name_of_Book,Author,Genre,Status)
        mycursor.execute(Record)
        Record="insert into Available_Table values('{}','{}','{}','{}')".format(BOOKS_Id,Name_of_Book,Author,Genre)
        mycursor.execute(Record)
    except:
        print('Invalid Input. Try again')
    Mydb.commit()

#DELETE BOOKS
def delbook():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    BOOKS_ID=input("enter ID of the book to be removed")
    try:
        com="delete from Primary_Table where Book_ID='{}'".format(BOOKS_ID)
        mycursor.execute(com)
        print('Book deleted successfully')
        try:
            com="delete from Available_Table where Book_ID='{}'".format(BOOKS_ID)
            mycursor.execute(com)
        except:
            pass
        try:
            com="delete from Borrowed_Table where Book_ID='{}'".format(BOOKS_ID)
            mycursor.execute(com)
        except:
            pass

    except:
        print('Invalid Input')
    Mydb.commit()

#REGISTER BOOK
def registerbook():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    Book_ID=input('Enter Book_ID')
    try:
        com="Delete from Available_Table where Book_ID='{}';".format(Book_ID)
        mycursor.execute(com)
    except:
        print('The Book has been already borrowed or the book does not exist')
        
    com="Update Primary_Table set Status='Borrowed' where Book_ID='{}';".format(Book_ID)
    mycursor.execute(com)
    Mydb.commit()
    
    com="Select * from Primary_Table where Book_ID='{}';".format(Book_ID)
    mycursor.execute(com)
    data=mycursor.fetchall()
    Name_of_Book=data[0][1]


    
    Borrower=input('Enter Name of Borrower')
    D_Bor=input('Enter Date Borrowed (YYYY-MM-DD): ')
    D_Ret=input('Enter Expected Date of Return (YYYY-MM-DD): ')
    try:
        com="Insert into Borrowed_Table values('{}','{}','{}','{}','{}');".format(Book_ID,Name_of_Book,Borrower,D_Bor,D_Ret)
        mycursor.execute(com)
    except:
        print('Error Occured due to Invalid Inputs. Try again')
    Mydb.commit()

#RETURN BOOK
def returnbook():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    Book_ID=input('Enter Book_ID (format: #WRD_No): ')
    if '#WRD_' in Book_ID:
        com="Update Primary_Table set Status='Available' where Book_ID='{}';".format(Book_ID)
        mycursor.execute(com)
        Mydb.commit()

        com="Select * from Borrowed_Table where Book_ID='{}';".format(Book_ID)
        mycursor.execute(com)
        data=mycursor.fetchall()
        data=data[0]

        com="Delete from Borrowed_Table where Book_ID='{}';".format(Book_ID)
        mycursor.execute(com)
        Mydb.commit()

        D_Ret=input('Enter Date Returned (YYYY-MM-DD): ')
        fine=calculate(D_Ret,data[-1])
        fine=fine*5
        print('Fine to be paid:',fine,'Rupees')

        com="Select * from Primary_Table where Book_ID='{}';".format(Book_ID)
        mycursor.execute(com)
        data=mycursor.fetchall()
        data=data[0]
        com="Insert into Available_Table values('{}','{}','{}','{}');".format(data[0],data[1],data[2],data[3])
        mycursor.execute(com)
        Mydb.commit()
    else:
        print('Invalid Input. Try Again')

#CALCULATING FEE
def calculate(x,y):
    from datetime import date
    d1=date(int(x[0:4]),int(x[5:7]),int(x[8::]))
    fee=d1-y
    return fee.days
        
#VIEWING BOOKS
def viewbook():
    import mysql.connector
    from tabulate import tabulate
    Mydb = mysql.connector.connect(host='localhost',user='root',password='1234' ,database=database)
    mycursor = Mydb.cursor()
    print("1.Display all details","2.Display as per condition",sep="\n")
    choose = input("enter your desired option")
    if choose == '1':
        mycursor.execute('select * from Primary_Table')
        result = mycursor.fetchall()
        header=['BOOKS_ID','Name_of_Book','Author','Genre','Status']
        print(tabulate(result,header,tablefmt='orgtbl'))
    elif choose=='2':
        cond={}
        try:
            n=int(input('Enter Number of Conditions'))
            for i in range(n):
                condition=''
                print('Filter Options:','1.Book_ID','2.Name_of_Book','3.Author','4.Genre','5.Status',sep='\n')
                choice= input("enter choice ")
                if choice=='1':
                    Book_ID=input('Enter Book ID (format #WRD_No): ')
                    condition="Book_ID='{}'".format(Book_ID)
                    cond={}
                    break
                elif choice=='2':
                    Name=input('Enter Name')
                    cond['Name_of_Book']=Name
                elif choice=='3':
                    Author=input('Enter Author Name')
                    cond['Author']=Author
                elif choice=='4':
                    Genre=input('Enter Genre')
                    cond['Genre']=Genre
                elif choice=='5':
                    Status=input('Enter Status (Available/Borrowed): ')
                    cond['Status']=Status
                else:
                    print('Invalid Input')
            l=list(cond.keys())
            if len(l)>0:
                for i in l: #forming condition statement
                    if i==l[-1]:
                        condition+="{}='{}'".format(i,cond[i])
                    else:
                        condition+="{}='{}' and ".format(i,cond[i])
            query="select * from Primary_Table where {};".format(condition)
            mycursor.execute(query)
            result1 = mycursor.fetchall()
            header=['BOOKS_ID','Name_of_Book','Author','Genre','Status']
            print(tabulate(result1,header,tablefmt='orgtbl'))
        except:
            print('Invalid Input. Try Again')
    else:
        print('Invalid Input. Try Again')



#DISPLAYING MEMBER MANAGEMENT OPTIONS
def membersmenu():
    print('-'*100)
    print('Siup Ris Management Software 2024-25 DATABASE: Library OPTION: Members')
    print('-'*100)
    print('1. Add Member')
    print('2. View Member')
    print('3. Register Membership Payment')
    print('4. Modify Member Details')
    print('5. Remove Members')
    print('6. Exit')
    choice=input('Enter Choice')
    print()
    global C
    if choice=='1':
        addmember()
    elif choice=='2':
        viewmember()
    elif choice=='3':
        membershippay()
    elif choice=='4':
        modifymember()
    elif choice=='5':
        delmember()
    elif choice=='6':
        C='Exit'
    else:
        print('Invalid Input')




#ADDING MEMBER
def addmember():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    Mycursor=Mydb.cursor()
    Member_ID=input("enter Member_id (format: #MBR_No): ")
    if '#MBR_' in Member_ID:
        try:
            Name=input("enter name ")
            Passport_No=input("enter passport number")
            DOB=input("enter date of birth (YYYY-MM-DD)")
            Address=input("enter address")
            Fee_Status=input("enter fee status")
            Phone_No=int(input('Enter Phone Number'))
            Data="insert into Member_Table values('{}','{}','{}','{}','{}','{}','{}');".format(Member_ID,Name,Passport_No,DOB,Address,Fee_Status,Phone_No)
            Mycursor.execute(Data)
            Mydb.commit()
        except:
            print('Inavlid Input. Try Again')
    else:
        print('Invalid Input. Try Again')

#DELETE MEMBER
def delmember():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    Member_ID=input("enter the ID of member to be removed")
    
    com="Select * from Member_Table where Member_ID='{}';".format(Member_ID)
    mycursor.execute(com)
    data=mycursor.fetchall()
    
    Rec="delete from Member_Table where Member_ID='{}'".format(Member_ID)
    mycursor.execute(Rec)
    
    if data!=[]:
        Mydb.commit()
        print('Member Removed Successfully')
    else:
        print('Invalid Input. Try Again')

#MEMBERSHIP PAY
def membershippay():
    MBR_ID=input('Enter Member ID (format: #MBR_No)')
    import mysql.connector 
    Mydb = mysql.connector.connect(host='localhost',user='root',password='1234' ,database=database)
    mycursor = Mydb.cursor()
    try:
        com='Update Member_Table set Fee_Status=\'Paid\' where Member_ID=\'{}\';'.format(MBR_ID)
        mycursor.execute(com)
        Mydb.commit()
    except:
        print('Invalid Input. Try Again')
        

#VIEW MEMBER
def viewmember():
    from tabulate import tabulate 
    import mysql.connector 
    Mydb = mysql.connector.connect(host='localhost',user='root',password='1234' ,database=database)
    mycursor = Mydb.cursor()
    print("1.Display all details","2.Display as per condition",sep="\n")
    choose = input("enter your desired option")
    if choose == '1':
        mycursor.execute('select * from Member_Table;')
        result = mycursor.fetchall()
        header=['Members_ID','Name','Passport_No','DOB','Address','Fee_Status','Phone_No']
        print(tabulate(result,header,tablefmt='orgtbl'))
    elif choose=='2':
        cond={}
        try:
            n=int(input('Enter Number of Conditions'))
            for i in range(n):
                condition=''
                print('Filter Options:','1.Member_ID','2.Name','3.Passport_No','4.DOB','5.Address','6. Fee Status','7. Phone_No',sep='\n')
                choice= input("enter choice ")
                if choice=='1':
                    Member_ID=input('Enter Member ID (format #MBR_No): ')
                    condition="Member_ID='{}'".format(Member_ID)
                    cond={}
                    break
                elif choice=='2':
                    Name=input('Enter Name')
                    cond['Name']=Name
                elif choice=='3':
                    Passport_No=input('Enter Passport_No')
                    cond['Passport_No']=Passport_No
                elif choice=='4':
                    DOB=input('Enter Genre (YYYY-MM-DD)')
                    cond['DOB']=DOB
                elif choice=='5':
                    Address=input('Enter Address: ')
                    cond['Address']=Address
                elif choice=='6':
                    Fee_Status=input('Enter Fee Status (Paid/Unpaid): ')
                    cond['Fee_Status']=Fee_Status
                elif choice=='7':
                    Phone_No=int(input('Enter Phone No:'))
                    cond['Phone_No']=Phone_No
                else:
                    print('Invalid Input')
            l=list(cond.keys())
            if len(l)>0:
                for i in l: #forming condition statement
                    if i==l[-1]:
                        condition+="{}='{}'".format(i,cond[i])
                    else:
                        condition+="{}='{}' and ".format(i,cond[i])
            query="select * from Member_Table where {};".format(condition)
            mycursor.execute(query)
            result = mycursor.fetchall()
            header=['Members_ID','Name','Passport_No','DOB','Address','Fee_Status','Phone_No']
            print(tabulate(result,header,tablefmt='orgtbl'))
        except:
            print('Invalid Input. Try Again')
    else:
        print('Invalid Input')
    

#MODIFY MEMBER
def modifymember():
    import mysql.connector as mysql
    Mydb=mysql.connect(host='localhost',user='root',password='1234',database=database)
    mycursor=Mydb.cursor()
    Member_ID=input("enter Member_id (format: #MBR_No): ")
    com="Select * from Member_Table where Member_ID='{}';".format(Member_ID)
    print()
    print('1. Change Address','2. Change Phone Number',sep='\n')
    choice=input('Enter choice')
    if '#MBR_' in Member_ID:
        try:
            if choice=='1':
                Address=input('Enter New Address')
                com="Update Member_Table set Address='{}' where Member_ID='{}';".format(Address,Member_ID)
                mycursor.execute(com)
            elif choice=='2':
                Phone=int(input('Enter New Phone number'))
                com="Update Member_Table set Phone_No='{}' where Member_ID='{}';".format(Phone,Member_ID)
                mycursor.execute(com)         

            Mydb.commit()
        except:
            print('Inavlid Input. Try Again')
    else:
        print('Invalid Input. Try Again')




    

#PROCESSING LOOP
while True:
    c=''
    intro()
    if c=='Initiate':
        while True:
            Initializebook()
            Initializemember()
            menu()
            if C=='Books':
                while True:
                    booksmenu()
                    if C=='Exit':
                        break
            elif C=='Members':
                while True:
                    membersmenu()
                    if C=='Exit':
                        break
            elif C=='Quit':
                print('Book Management Application Closed Successfully')
                break
            else:
                print('Invalid Input')        
    elif c=='End':
        break
