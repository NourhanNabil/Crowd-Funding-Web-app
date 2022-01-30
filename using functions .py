import datetime
import json
def check_first_name():
    ''' 
    check for first name if the input is not digits and not a null value
    '''
    while True:
     first_name=input("Enter your first name\n")
     if first_name.isalpha():
         return first_name
     else:
         print("Enter a valid name")    
def check_last_name():
    ''' 
    check for last name if the input is not digits and not a null value
    '''
    while True:
       last_name=input("Enter your last name\n")
       if last_name.isalpha():
         return last_name
       else:
         print("Enter a valid name")        
def phone_check():
    ''' 
    check for phone number if the input is digits and contains 11 numbers startswith 011,012,015,010 and not a null value
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
    check for email if the input contains "@" and ends with ".com,.net,.org" and not null value
    '''
    flag=False
    while True:
        try:
            email=input("Enter your email\n")
            checkforat=email.find("@")
            checkfordotcom=email.endswith(".com") or email.endswith(".net") or email.endswith(".org") 
            with open("registration.json", "r") as file:
                data=file.read()
                data= json.loads(data)
            if checkforat != -1 and checkfordotcom != -1:
                if checkfordotcom is True:
                    ''' 
                    check if email already exist
                    '''
                    for i in range(len(data)):
                        if data[i]["email"] == email:
                            flag=True 
                    if flag == True:
                        print("this email already exist")
                        flag=False
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
       check for password if the input is at least 8 characters and not a null value
       '''
       global password
       password=input("Enter your password\n")
       if len(password) >= 8: 
            return password
       else: 
           print("Enter at least 8 characters")              
def confirm_password():
    ''' 
       check for confirm password if the input is the same as password and not a null value
    '''
    while True:
        confirm=input("Re-enter your password for confirmation\n")
        if confirm == password:
            return confirm
        else:
            print("Enter the exact password")    
def check_project_title():
    ''' 
       check for project title is not a null value
    '''
    while True:
        title=input("Enter the project title\n")
        if str(title):
            return title
        else:
            print("Title can not be null")
def check_project_details():
    ''' 
       check for project details is not a null value
    '''
    while True:
        details=input("Enter the project details\n")   
        if str(details):
            return details
        else:
            print("Details can not be null")      
def check_total_target():
    ''' 
       check for total target is not a null value and accept only numbers and more than 2000
    '''
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
    ''' 
       check for start date is not a null value and in the right date format
    '''
    while True:
        global start_date
        start_date=input("Enter the start-date\n")
        try:
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
            return start_date
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")          
def check_end_date():
    ''' 
       check for end date is not a null value and in the right date format and comes after the start date
    '''
    while True:
        end_date=input("Enter the end-date\n")
        try:
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
            if start_date < end_date:
                return end_date
            else:
                print(f"end-date must come after {start_date}")    
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
    ''' 
       record is the values entered by the users and assigned to the key value
    '''
    record=[first_name,last_name,email,password,mobile_phone]
    key=["firstname","lastname","email","password","mobile_phone"]
    dict={}
    for i in range(len(record)):
         dic={key[i]:record[i]}
         dict.update(dic) 
    try:
        ''' 
         if the file is not empty it will append the new record dictionary into it the previous one
        '''
        with open("registration.json", "r") as file:
            data=file.read()
            data= json.loads(data)
            data.append(dict)
    except json.decoder.JSONDecodeError:  
            ''' 
              if the file is empty it will add an empty array and append the dictionary into it
            '''   
            data=[]
            data.append(dict)   
    with open("registration.json", "w") as file:
            json.dump(data, file, indent=4, separators=(',',': ') )   
    print("registered successfully!")
    while True:
        ''' 
          after registration choose between to login or to end 
        '''
        answer=input("choose 1 to login or 2 to end\n")
        if answer == "1":
            return login()
        elif answer == "2":
            return None
        else:
            print("choose either 1 or 2")        
# For email check while Login
def email_login_check():
    ''' 
     check if the email exist before or not to allow the user to create or view projects
    '''
    flag=False
    while True:
        global login_email
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
            ''' 
             if there is no users yet will check in json file
            '''
            print("this email does not exist")
            return None
# For password check while Login                     
def password_login_check():
    ''' 
        check if the password match the user email entered in login to allow the user to create or view projects
    '''
    flag=False
    while True:
        login_password=input("Enter your password\n")
        with open("registration.json", "r") as file:
            data=file.read()
            data= json.loads(data)
        for i in range(len(data)):
            if data[i]["email"] == login_email and data[i]["password"] == login_password:
                flag=True    
            else:
                None 
        if flag == True:
            return login_password     
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
    ''' 
       record is the values entered by the users and assigned to the key value
    '''
    record=[title,details,total_target,start_date,end_date,login_email]
    key=["title","details","total_target","start_date","end_date","Created-by"]
    dict={}
    for i in range(len(record)):
         dic={key[i]:record[i]}
         dict.update(dic) 
    try:
        ''' 
         if the file is not empty it will append the new record dictionary into it the previous one
        '''
        with open("projects.json", "r") as file:
            data=file.read()
            data= json.loads(data)
            data.append(dict)
    except json.decoder.JSONDecodeError:  
            ''' 
              if the file is empty it will add an empty array and append the dictionary into it
            '''   
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
        ''' 
          if the file is empty it will print this message
        '''
        print("No projects yet")
        view_or_create_projects()
# For Login      
def login():
    email=email_login_check()
    ''' 
    if the login email not found it will go back to the start function else will ask for password
    '''
    if email == None:
        start()
    else:    
        login_password=password_login_check()
    ''' 
    if the password does not match the login email enterd it will go back to the start function else will open the view or create function
    '''    
    if login_password == None:
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
            print(f"Welcome back {first_name} {last_name}")
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
