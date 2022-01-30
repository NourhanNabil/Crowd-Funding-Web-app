import json
import datetime
class projects():
    @staticmethod
    def check_project_title():
        ''' 
         check for project title is not a null value
        '''
        while True:
            global title
            title=input("Enter the project title\n")
            if str(title):
                return title
            else:
                print("Title can not be null")
    @staticmethod            
    def check_project_details():
        ''' 
        check for project details is not a null value
        '''
        while True:
            global details
            details=input("Enter the project details\n")   
            if str(details):
                return details
            else:
                print("Details can not be null")
    @staticmethod                  
    def check_total_target():
        ''' 
         check for total target is not a null value and accept only numbers and more than 2000
        '''
        while True:
            global total_target
            total_target=input("Enter the total target\n")
            if total_target.isdigit():
                if int(total_target) > 2000:
                    return total_target 
                else:
                    print("Enter a value bigger than 2000")      
            else:
                print("Enter numbers only")
    @staticmethod             
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
    @staticmethod                      
    def check_end_date():
        ''' 
        check for end date is not a null value and in the right date format and comes after the start date
         '''
        while True:
            global end_date
            end_date=input("Enter the end-date\n")
            try:
                datetime.datetime.strptime(end_date, '%Y-%m-%d')
                if start_date < end_date:
                    return end_date
                else:
                    print(f"end-date must come after {start_date}")    
            except ValueError:
                print("Incorrect date format, should be YYYY-MM-DD")
    def view_or_create_projects(self):
        while True: 
            answer=input("choose 1 to create projects or 2 to view projects or 3 to end\n")
            if answer == "1":
                return self.create_projects()
            elif answer == "2":
                return self.view_projects()
            elif answer == "3":
                return None    
            else:
                print("choose either 1 or 2 or 3") 
    def create_projects(self): 
        self.check_project_title()
        self.check_project_details()
        self.check_total_target()
        self.check_start_date()
        self.check_end_date()
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
        self.view_or_create_projects() 
    def view_projects(self):
        try:
            with open("projects.json", "r") as file:
                    data=file.read()
                    data= json.loads(data)
                    print(data)
                    self.view_or_create_projects()
        except json.decoder.JSONDecodeError: 
            ''' 
            if the file is empty it will print this message
            '''
            print("No projects yet")
            self.view_or_create_projects() 
class members(projects):
    @staticmethod    
    def first_name_check():
        ''' 
         check for first name if the input is not digits and not a null value
        '''
        while True:
            global first_name
            first_name=input("Enter your first name\n")
            if first_name.isalpha():
                return first_name
            else:
                print("Enter a valid name") 
    @staticmethod             
    def last_name_check():
        ''' 
          check for last name if the input is not digits and not a null value
        '''
        while True:
            global last_name
            last_name=input("Enter your last name\n")
            if last_name.isalpha():
                return last_name
            else:
                print("Enter a valid name")    
    @staticmethod                     
    def email_check():
        ''' 
        check for email if the input contains "@" and ends with ".com,.net,.org" and not null value
        '''
        flag=False
        while True:
            global email
            email=input("Enter your email\n")
            checkforat=email.find("@")
            checkfordotcom=email.endswith(".com") or email.endswith(".net") or email.endswith(".org") 
            try:
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
    @staticmethod              
    def password_check():
        ''' 
        check for password if the input is at least 8 characters and not a null value
        '''
        while True:
            global password
            password=input("Enter your password\n")
            if len(password) >= 8: 
                    return password
            else: 
                print("Enter at least 8 characters")  
    @staticmethod                
    def confirm_password_check():
        ''' 
        check for confirm password if the input is the same as password and not a null value
        '''
        while True:
            confirm=input("Re-enter your password for confirmation\n")
            if confirm == password:
                return confirm
            else:
                print("Enter the exact password")  
    @staticmethod              
    def mobil_phone_check():
         ''' 
            check for phone number if the input is digits and contains 11 numbers startswith 011,012,015,010 and not a null value
         '''
         while True:
            global mobile_phone
            mobile_phone=input("Enter your mobile phone\n")
            if  mobile_phone.startswith(("011","012","015","010")):
                if len(mobile_phone) == 11 and mobile_phone.isdigit:
                    return mobile_phone 
                else:
                    print("Please enter a valid mobile phone")
            else:
                print("please enter a mobile phone in Egypt")            
    def registration(self):
        self.first_name_check()
        self.last_name_check()
        self.email_check()
        self.password_check()
        self.confirm_password_check()
        self.mobil_phone_check()
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
                return self.login()
            elif answer == "2":
                return None
            else:
                print("choose either 1 or 2")
    def email_login_check(self):
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
    def password_login_check(self):
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
    def login(self):
        login_email=self.email_login_check()
        ''' 
        if the login email not found it will go back to the start function else will ask for password
        '''
        if login_email == None:
            start()
        else:    
          login_password=self.password_login_check()
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
                if data[i]["email"] == login_email:
                    first_name= data[i]["firstname"]
                    last_name= data[i]["lastname"]
                    flag=True
            if flag == True:
                '''
                view_or_create_projects() inherited from the projects' class
                '''
                print(f"Welcome back {first_name} {last_name}")
                return self.view_or_create_projects()
            else:
                return None                                       
class start(members):
    def __init__(self):
        self.start()    
    def start(self):
        while True:
            choice=input("choose: 1 for Registration 2 for Login\n")
            '''
            registration() and login() inherited from the members' class
            '''
            if choice == "1":
             return self.registration() 
            elif choice == "2":
             return self.login()  
            else:
                print("Enter either 1 or 2")
start()                