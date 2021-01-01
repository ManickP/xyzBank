import sys


class Customer:
    clientDict = {}

    def __init__(self,name,age,amount):
        self.name = name
        self.age = age
        self.amount = amount

    @classmethod
    def clientDetails(cls): # Prints object created
        for k in Customer.clientDict:
            obj = Customer.clientDict[k]
            print(obj.name)
            print(obj.age)
            print(obj.amount)

    @classmethod
    def createClient(cls,clientName,clientAge,clientAmount): # Creates the Client object
        Customer.clientDict.update({clientName:Customer(clientName,clientAge,clientAmount)})
        print(f'\nHi {Customer.clientDict[clientName].name}. Welcome to XYZ bank. Please select which banking product you want to add')

    @staticmethod
    def welcomeScreen():
        print("\n"+"Welcome to XYZ bank".center(100)+"\n")
        optionList = ["Client","Admin","Quit Program"] # 1 is Client and 2 is Admin and 3 is quit program
        for eno, item in enumerate(optionList):
            print(f'{eno+1} - {item}')
        optionSelected = int(input("\nEnter an option number from above -> "))
        if optionSelected == 1:
            profile,uname,age,amount = Customer.client()
            return [profile,uname,age,amount] 
        elif optionSelected == 2:
            profile = Customer.admin()
            return [profile]
        elif optionSelected == 3:
            print("Quitting Program")
            sys.exit()

    @staticmethod
    def client():
        profile = "client"
        clientName = input("Enter your name -> ")
        clientAge = input("Enter your age -> ")
        clientAmount = input("Enter your annual income -> ")
        return profile,clientName,clientAge,clientAmount

    @staticmethod
    def admin():
        profile = "admin"
        adminUserName = adminPassword = "temp"
        while adminUserName != 'admin' or adminPassword != 'admin':
            adminUserName = input("Enter admin user name -> ")
            adminPassword = input("Enter admin password -> ")
            if adminUserName !='admin' or adminPassword !='admin':
                print("\nIncorrect username or password. Try again\n")
        print("Successfully authenticated")
        return profile

    @staticmethod
    def bankingProducts():
        bankingProductList = ['Chequing Account','Credit Card','Savings Account']

        
class Product(Customer):
    pass

retrunList = Customer.welcomeScreen() 
if retrunList[0] == 'client':
    Customer.createClient(retrunList[1],retrunList[2],retrunList[3])
#Customer.clientDetails()