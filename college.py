# COLLEGE MANAGEMENT SYSTEM
management=[5,7,9]
faculty={}
student={}
marks={}
relation={}
def Management():
    mId=int(input("Enter ID : "))    
    while 1:  
        if mId in management:      
            print("\t---Management Options-----")
            print("1.Add faculty","2.Show faculty","3.Exit",sep="\n")
            opt=int(input("Enter your option : "))
            if(opt==1):
                print(addFaculty(int(input("enter ID :")),input("Enter name :")))
            elif(opt==2):
                showfaculty()
            elif(opt==3):
                break
            else:
                print("Invalid option")
        else:
            print("!!!Unauthorized access!!!")
            mId=int(input("Enter ID : ")) 

def Faculty():
    fId=int(input("Enter ID : "))    
    while 1:  
        if fId in faculty:        
            print("\t---Faculty Options-----")
            print("1.Add Student","2.Show students","3.Exit",sep="\n")
            opt=int(input("Enter your option : "))
            if(opt==1):
                print(addStudent(fId,int(input("enter ID :")),input("Enter name :"),int(input("enter Marks :"))))
            elif(opt==2):
                showStudents(fId)
            elif(opt==3):
                break
            else:
                print("Invalid option")
        else:
            if faculty=={}:
                print("\tNo faculty is registered","\n\t---returning to home login")
                homeLogin()
            else:
                print("!!!NO faculty with this Id!!!")
                fId=int(input("Enter ID : ")) 
                

def Student():
    sId=int(input("Enter ID : "))    
    while 1:  
        if sId in student:  
            print("\t---Student  Options-----")
            print("1.Show marks","2.Exit",sep="\n")
            opt=int(input("Enter your option : "))
            if(opt==1):
                showMarks(int(input("enter ID :")))
            elif(opt==2):
                break
            else:
                print("Invalid option")
        else:
             if faculty=={}:
                print("\tNo student is registered","\n\t---returning to home login")
                homeLogin()
             else:
                print("!!!No student with this Id!!!") 
                sId=int(input("Enter ID : ")) 
def addFaculty(id,name):
    faculty[id]=name
    relation[id]=[]
    return "Successfully added"
def showfaculty():
    if faculty=={}:
        print("No faculty")
    for i in faculty:
        print("ID---2",i,"\tName--",faculty[i])
def addStudent(fid,id,name,mark):
    student[id]=name
    marks[id]=mark
    l=relation[fid]
    l.append(id)
    relation[fid]=l
    return "Successfully added"
def showStudents(fid):
    if relation[fid]==[]:
        print("No students")
    else:
        records=relation[fid]
        for i in records:
            print("ID--",i,"\tName--",student[i])
def showMarks(id):
    for fid in relation:
        if id in relation[fid]:
            faculty_name = faculty[fid]  # Correctly find the faculty name
            break
    else:
        print("No faculty found for this student.")
        return
    print("---Details-----\n", "ID : ", id, "\nName : ", student[id])
    print("Subject : Computer Science\n", "Marks :", marks[id], "\nFaculty name : ", faculty_name)

def homeLogin():
    while 1:
        print("\t-----Available Logins-----","1.Management","2.Faculty","3.Student","4.Exit",sep="\n")
        login=int(input("Enter the login : "))
        if(login==1):
            Management()
        elif login==2:
            Faculty()
        elif login==3:
            Student()
        elif login==4:
            print("<--------Exiting-------->")
            break
#Execution start from here
homeLogin()
