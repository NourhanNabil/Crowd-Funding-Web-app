import datetime
import json
global data
def check_first_name():
    ''' 
    check for first name if the input is not digits
    '''
    while True:
     first_name=input("Enter your first name\n")
     if first_name.isalpha():
         return first_name
     else:
         print("Enter a valid name")    
def check_last_name():
    ''' 
    check for last name if the input is not digits
    '''
    while True:
       last_name=input("Enter your last name\n")
       if last_name.isalpha():
         return last_name
       else:
         print("Enter a valid name")        
def phone_check():
    ''' 
    check for phone number if the input is digits and contains 11 numbers startswith 011,012,015,010
    '''
    while True:
      mobile_phone=input("Enter your mobile phone\n")
      if  mobile_phone.startswith(("011","012","015","010")):
          if len(mobile_phone) == 11 and mobile_phone.isdigit:
              return mobile_phone 
          else:
             print("Please enter a valid mobile phone")
      else:
         print("please enter a mobile phone in Egypt")            
def email_check():
    ''' 
    check for email if the input contains "@" and ".com,.net,.org"
    '''
    flag=False
    while True:
        email=input("Enter your email\n")
        checkforat=email.find("@")
        checkfordotcom=email.endswith(".com") or email.endswith(".net") or email.endswith(".org") 
        try:
            with open("registration.json", "r") as file:
                data=file.read()
                data= json.loads(data)
            if checkforat != -1 and checkfordotcom != -1:
                if checkfordotcom is True:
                    for i in range(len(data)):
                        if data[i]["email"] == email:
                            flag=True 
                    if flag == True:
                        print("this email already exist")
                    else:
                        return email                  
                else:
                    print("Enter a valid email")    
            else:
             print("please enter a valid email")   
        except json.decoder.JSONDecodeError:
            if checkforat != -1 and checkfordotcom != -1:
                if checkfordotcom is True:
                     return email                 
                else:
                    print("Enter a valid email")    
            else:
             print("please enter a valid email")
def password_check():
  while True:
       ''' 
       check for password if the input is at least 8 characters
       '''
       global password
       password=input("Enter your password\n")
       if len(password) >= 8: 
            return password
       else: 
           print("Enter at least 8 characters")              
def confirm_password():
    ''' 
       check for confirm password if the input is the same as password
    '''
    while True:
        confirm=input("Re-enter your password for confirmation\n")
        if confirm == password:
            return confirm
        else:
            print("Enter the exact password")    
def check_project_title():
    while True:
        title=input("Enter the project title\n")
        if str(title):
            return title
        else:
            print("Title can not be null")
def check_project_details():
    while True:
        details=input("Enter the project details\n")   
        if str(details):
            return details
        else:
            print("Details can not be null")      
def check_total_target():
    while True:
        total_target=input("Enter the total target\n")
        if total_target.isdigit():
            if int(total_target) > 2000:
                return total_target 
            else:
                print("Enter a value bigger than 2000")      
        else:
            print("Enter numbers only") 
def check_start_date():
    global start_date
    while True:
        start_date=input("Enter the start-date\n")
        try:
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
            return start_date
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")          
def check_end_date():
    while True:
        end_date=input("Enter the end-date\n")
        try:
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
            if start_date < end_date:
                return end_date
            else:
                print("end-date must come after {}".format(start_date))    
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")
# For Registration 
def registration():
    first_name=check_first_name()
    last_name=check_last_name()
    email=email_check()
    password=password_check()
    confirm=confirm_password()
    mobile_phone=phone_check()
    record=[first_name,last_name,email,password,mobile_phone]
    key=["firstname","lastname","email","password","mobile_phone"]
    dict={}
    for i in range(len(record)):
         dic={key[i]:record[i]}
         dict.update(dic) 
    try:
        with open("registration.json", "r") as file:
            data=file.read()
            data= json.loads(data)
            data.append(dict)
    except json.decoder.JSONDecodeError:     
            data=[]
            data.append(dict)
            print("String could not be converted to JSON")     
    with open("registration.json", "w") as file:
            json.dump(data, file, indent=4, separators=(',',': ') )   
    print("registered successfully!")
    answer=input("choose 1 to login or 2 to end\n")
    if answer == "1":
        return login()
    elif answer == "2":
        return None
    else:
        print("choose either 1 or 2")        
# For email check while Login
def email_login_check():
    global login_email
    flag=False
    while True:
        login_email=input("Enter your email\n")
        try:
            with open("registration.json", "r") as file:
                data=file.read()
                data= json.loads(data)
            for i in range(len(data)):
                        if data[i]["email"] == login_email:
                            flag=True  
            if flag == True:
                return login_email     
            else:
                print("this email does not exist")
                return None 
        except json.decoder.JSONDecodeError:
            print("this email does not exist")
            return None
# For password check while Login                     
def password_login_check():
    flag=False
    while True:
        password=input("Enter your password\n")
        with open("registration.json", "r") as file:
            data=file.read()
            data= json.loads(data)
        for i in range(len(data)):
            if data[i]["email"] == login_email and data[i]["password"] == password:
                flag=True    
            else:
                None 
        if flag == True:
            return password     
        else:
            print("password is not correct try again")  
            return None                     
# To Create Projects 
def create_projects(): 
    title=check_project_title()
    details=check_project_details()
    total_target=check_total_target()
    start_date=check_start_date()
    end_date=check_end_date()
    record=[title,details,total_target,start_date,end_date,login_email]
    key=["title","details","total_target","start_date","end_date","Created-by"]
    dict={}
    for i in range(len(record)):
         dic={key[i]:record[i]}
         dict.update(dic) 
    try:
        with open("projects.json", "r") as file:
            data=file.read()
            data= json.loads(data)
            data.append(dict)
    except json.decoder.JSONDecodeError:     
            data=[]
            data.append(dict) 
    with open("projects.json", "w") as file:
            json.dump(data, file, indent=4, separators=(',',': ') )   
    print("project created successfully!")
    view_or_create_projects()
# To View Projects     
def view_projects():
    try:
     with open("projects.json", "r") as file:
            data=file.read()
            data= json.loads(data)
            print(data)
            view_or_create_projects()
    except json.decoder.JSONDecodeError: 
        print("No projects yet")
        view_or_create_projects()
# For Login      
def login():
    email=email_login_check()
    if email == None:
        start()
    else:    
        password=password_login_check()
    if password == None:
        start()
    else:
        with open("registration.json", "r") as file:
            data=file.read()
            data= json.loads(data)
        flag=False    
        for i in range(len(data)):
            if data[i]["email"] == email:
                first_name= data[i]["firstname"]
                last_name= data[i]["lastname"]
                flag=True
        if flag == True:
            print("Welcome back {} {}!".format(first_name,last_name))
            return view_or_create_projects()
        else:
            return None  
# To choose between view or create projects after login            
def view_or_create_projects():
   while True: 
    answer=input("choose 1 to create projects or 2 to view projects or 3 to end\n")
    if answer == "1":
        return create_projects()
    elif answer == "2":
        return view_projects()
    elif answer == "3":
        return None    
    else:
        print("choose either 1 or 2 or 3") 
# Start with either login or registration         
def start():
    while True:
        choice=input("choose: 1 for Registration 2 for Login\n")
        if choice == "1":
         return registration()
        elif choice == "2":
         return login()  
        else:
            print("Enter either 1 or 2")   
start()            