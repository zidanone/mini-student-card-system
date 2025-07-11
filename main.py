import csv
from pyfiglet import Figlet
from colorama import Fore , Style , init
import pyfiglet
import os



init(autoreset=True)
STUDENTS_ACCOUNTS = 'accounts.csv'
fonts = pyfiglet.FigletFont.getFonts()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


STUDENTS_ACCOUNTS = "accounts.csv"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def create_account():
    clear_screen()
    print("================Create Account Side==============\n")
    username = input(Fore.GREEN+"Username: ")
    password = input("Password: ")
    github = input("Github: ")
    email = input("Email: ")
    phone_number =input("Phone Number with (+ country code ): "+Style.RESET_ALL)    
            
    if not username or not password:
        input(Fore.RED+"Invalid info\nPress Enter to go back..."+Style.RESET_ALL)
        clear_screen()
        return
    elif password == username:
        input(Fore.YELLOW+"Password can't be same as username\nPress Enter to go back...."+Style.RESET_ALL)
        clear_screen()
        return
    else:
        usernames = set()
        if os.path.exists(STUDENTS_ACCOUNTS):
            with open(STUDENTS_ACCOUNTS, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    usernames.add(row["username"])

        if username in usernames:
            input(Fore.LIGHTRED_EX+"Username already exists. Try a different username.\nPress Enter to go back..."+Style.RESET_ALL)
            clear_screen()
            return

        
        file_exists = os.path.exists(STUDENTS_ACCOUNTS)
        with open(STUDENTS_ACCOUNTS, 'a') as file:
            fieldnames = ["username", "password","github","email","phone_number"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            if not file_exists or os.stat(STUDENTS_ACCOUNTS).st_size == 0:
                writer.writeheader()
            
            writer.writerow({"username": username, "password": password,"github":github,"email":email,"phone_number":phone_number})

        print(Fore.GREEN+"Account created successfully!"+Style.RESET_ALL)
        input("press Enter key to back ...")
        
        return

 
def admin():
    clear_screen()
    print("=============================================\n          Admin Center Side\n=============================================")
    adminuser = input(Fore.RED+"   *   Admin username : ").lower()
    password = input("   *   Admin password : ").lower()
    adminname = input("   *   Admin name please (Your name): ")
    if adminuser == 'admin' and password == "admin":
        clear_screen()    
            
            
    
        
        with open(STUDENTS_ACCOUNTS,'r') as rstudentsaccounts:
            reader = csv.DictReader(rstudentsaccounts)
            print(f"==========================================\n       Admin : {adminname}\n==========================================")
            admin_choice = int(input(Fore.GREEN+"   choice : \n     -1 ) Dispay all users info \n     -2 ) Search for one\n     -3 ) Display all just username are in\n     -9 ) Exit \n\n      - Your choice : "+Style.RESET_ALL))
        
        
            if admin_choice == 1: 
                for username in reader:
                    if username:
                        print(f"""-----------------------|* Students Info *|--------------------
                                @{username['username']}
                                        
                            # username : {username['username']}
                            # password : {username["password"]}
                            # Github : {username["github"]}
                            # Phone number : {username["phone_number"]}
                            # Email : {username["email"]}
                            
                                """)
                input("Press Enter key to back ...")
                
            elif admin_choice == 2:
                                
                admin_search = input(Fore.BLACK+"Enter a username to search: "+Style.RESET_ALL).lower()

                for users in reader:
                    if users["username"] == admin_search:
                    
                        print(f"""
                              
                               ---------------@---------------
                               ~ User : {users["username"]}               
                               ~ Password : {users["password"]}           
                               ~ Phone Number: {users["phone_number"]}    
                               ~ Github : {users["github"]}               
                               ~ Email : {users["email"]}""")
                        break
                else:
                    print("User not found , check for inputs")
            elif admin_choice == 3:
                for user in reader:
                    print(f"Users: {user["username"]}")
                print("That's all users in oue program")
            
            elif admin_choice == 9:
                clear_screen()
    
            else:
                print(f"hi {adminname} choice {admin_choice} is invalid")
                
            
    else:
        print("You'r not admin")
        input("press Enter key to back ...")



def students_info():
    
  
    print(f"--------------Welcome students @{username}.edu-------------")
    
    with open(STUDENTS_ACCOUNTS,'r') as rfile:
        reader = csv.DictReader(rfile)
        
        for name in reader:
            if name["username"] == username:
                print(f""" 
                      user : @{username}
                      Github : {name["github"]}
                      Email : {name["email"]}
                      Phone Number : {name["phone_number"]}
                      
                      """)
    student_choice = input("Do you when to take course's or not: (yes|no) ").lower()
    if student_choice.startswith('y'):
        courses = int(input(f"""
                {Fore.LIGHTYELLOW_EX+"!!! CS50 Courses !!!"}
                
                {Fore.BLUE+"1- CS50X"}
                {Fore.GREEN+"2- CS50"}
                {Fore.RED+"3- CS50P"} 
                
                {Fore.CYAN+"Choice one: "}"""))
        
        if courses == 1:
            
            print("\n     You have enroled CS50 Course")
            input("Press Enter to go back ...")
            clear_screen()
        elif courses == 2:
            print("      \nYou have enroled CS50 Course")
            input("Press Enter to go back ...")
            clear_screen()
        elif courses == 3:
            print('\n     You have enroled CS50P course')
            input("Press Enter to go back ...")
            clear_screen()
        else:
            print("Invalied Choice")
            input("Press Enter to go back ...")
            clear_screen()
    elif student_choice.startswith('n'):
        input(f"Ok , {username}\n\nPress Enter to go back")       
    else:
        print("have good day >>>")
        input("press Enter key to back...")
        clear_screen()
def load_accounts():
    clear_screen()
    global username 
    print("""=========================================\n        Welcome Student\n=========================================\n""")
    username = input("Enter your username: ")
    password = input("Enter password: ")
    with open(STUDENTS_ACCOUNTS, 'r') as loadstudentsinfo:
        reader = csv.DictReader(loadstudentsinfo)
        
        
        for user in reader:
            if user["username"] == username and user["password"] == password:
                clear_screen()
                students_info()
                break
        else:
            print("Ivnalid account. Try to create one..")
            
    return username
                
                
def help():
    clear_screen()
    print("=======================================================\n       HELP Center \n=======================================================")
    userhelp = int(input(f"\n        ^ 1 - Lost access to your account (Password reset)  \n        ^ 2 - Get free admin login account\n\n        * Enter your choice (Numbers only) : "))
    
    with open(STUDENTS_ACCOUNTS,'r') as accountsfile:
        
        reader = csv.DictReader(accountsfile)
        if userhelp == 1:   
            targetname = input("Enter your username to countine : ")
            for username in reader:
                if username["username"] == targetname:
                    clear_screen()
                    print(f"\n================== Password side ================\n Hello : {username['username']}\n your password is : {username['password']}\n=================================================")
                    input("Press Enter to go back ...")
                    clear_screen
                    break
                else:
                    print(f"{targetname} in not sing up")
                    break
        elif userhelp == 2:
            clear_screen
            print("""
                  =====================================================
                  =                   Admin account                   =
                  =            + User : Admin                         =
                  =            + password : Admin                     =
                  =                                                   =
                  =    NOTE : this free account has no effect         =
                  =====================================================
                  """)
            input("Press Enter to go back ...")
            
    clear_screen()
           
    
    
def show_contacts():
    clear_screen()
    print(Fore.YELLOW+"@ Contact Information")
    print("======================")
    print(Fore.BLUE+"@ Name: Mr. Zidane")
    print(Fore.GREEN+"@ Email: zidanestudentcs@gmail.com")
    print(Fore.CYAN+"@ GitHub: github.com/@zidanone")
    print(Fore.MAGENTA+"@ Instagram: @zidane.bak")
    print(Fore.RED+"\nPress Enter to go back...")
    input()
    clear_screen()
def main():
    clear_screen()
    while True:
        try:
            title = "---------------------Student Card---------------------\n    * Dev: Zidane barkat\n------------------------------------------------------"
            print(Fore.RED + title)
            print(f"""{Fore.BLUE + '\n      * 1- Create account\n'+Fore.GREEN+'\n      * 2- Add info\n'+Fore.YELLOW+'\n      * 3- Admin center\n'+Style.RESET_ALL+Fore.RED+Fore.BLACK+'\n      * 9- Help ( Info about our program )\n'+Style.RESET_ALL+Fore.RED+'\n      * 99- Exit\n'+Fore.CYAN+'\n      * 0- Contact us   -h '+Fore.RED+'(lost get help)'}""")
            user_choice = int(input(Fore.MAGENTA+"\n* Enter your choice as number: "+Style.RESET_ALL))
            
            if user_choice == 1:
                create_account()
            elif user_choice == 2:
                load_accounts()
            elif user_choice == 3:
                admin()
                
            elif user_choice == 99:
                break
            
            elif user_choice == 0:
                show_contacts()
            elif user_choice == 9:
                help()
            else:
                print("Invalid choice")
        except:
            pass


if __name__=="__main__":
    main()