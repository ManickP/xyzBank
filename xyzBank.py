import sys
import random


def quitProgram():
    print("Quitting Program")
    sys.exit()


class Customer:
    clientDict = {}

    def __init__(self, name, age, amount):
        self.name = name
        self.age = age
        self.amount = amount

    @staticmethod  # Error validation function for int check
    def inputCheckInt(message, listCount):
        while True:
            try:
                optionSelected = input(f'{message}')
                optionSelected = int(optionSelected)
                if optionSelected in list(range(1, listCount+1)):
                    break
                else:
                    print(
                        f"{optionSelected} is incorrect. Enter numbers between 1 and {listCount}")
            except ValueError:
                print(f'{optionSelected} is incorrect. Try again')
                continue
        return optionSelected

    @staticmethod  # Error validation function for float check
    def inputCheckFloat(message):
        while True:
            try:
                optionSelected = input(f'{message}')
                optionSelected = float(optionSelected)
                break
            except ValueError:
                print(f'{optionSelected} is incorrect. Try again')
                continue
        return optionSelected

    @staticmethod  # To generate a new client key by checking class attribute clientDict if the key is present or not
    def createClientID():
        id = 1
        while f'xyz_{id}' in Customer.clientDict:
            id += 1
            continue
        return f'xyz_{id}'

    @staticmethod  # Prints object created based on client id passed
    def clientDetails(client_id):
        for k in Customer.clientDict:
            if k == client_id:
                obj = Customer.clientDict[client_id]
                return [client_id, obj.name, obj.age, obj.amount]

    @classmethod  # Creates the Client object
    def createClient(cls, client_id, clientName, clientAge, clientAmount):
        Customer.clientDict.update(
            {client_id: cls(clientName, clientAge, clientAmount)})
        print(
            f'\nHi {Customer.clientDict[client_id].name}. Welcome to XYZ bank.')

    @staticmethod  # Welcome Screen prompting user for Client / Admin or quit the program i.e. option 1,2 and 3
    def welcomeScreen():
        print("\n"+"Welcome to XYZ bank".center(100)+"\n")
        optionList = ["Client", "Admin", "Quit Program"]
        for eno, item in enumerate(optionList):
            print(f'{eno+1} - {item}')
        optionSelected = Customer.inputCheckInt(
            "\nEnter an option number from above -> ", len(optionList))
        if optionSelected == 1:
            profile, uname, age, amount = Customer.client()
            return [profile, uname, age, amount]
        elif optionSelected == 2:
            profile = Customer.admin()
            return [profile]
        elif optionSelected == 3:
            quitProgram()

    @staticmethod
    def client():
        profile = "client"
        clientName = input("Enter your name -> ")
        clientAge = Customer.inputCheckInt("Enter your age -> ", 100)
        clientAmount = Customer.inputCheckFloat("Enter your annual income -> ")
        return profile, clientName, clientAge, clientAmount

    @staticmethod
    def admin():
        profile = "admin"
        while True:
            adminUserName = input("Enter admin user name -> ")
            adminPassword = input("Enter admin password -> ")
            if adminUserName != 'admin' or adminPassword != 'admin':
                print("\nIncorrect username or password. Try again\n")
            else:
                print("\nSuccessfully authenticated")
                return profile
                break


class Product:
    clientProdDict = {}

    def __init__(self, productCode, productNumber):
        self.productCode = productCode
        self.productNumber = productNumber

    @classmethod
    def clientProductMapping(cls, client_id, productCode, productNumber):
        Product.clientProdDict.update(
            {client_id: cls(productCode, productNumber)})

    @staticmethod  # Prints object created based on client id passed
    def productDetails(client_id):
        for k in Product.clientProdDict:
            if k == client_id:
                obj = Product.clientProdDict[client_id]
                return [obj.productCode, obj.productNumber]

    @staticmethod
    def productsToEnroll():
        prodList = [
            "Checking Account (CHQ)", "Credit Card (CBK/CBW)", "Saving Account (SAV)"]
        print("\nSelect from the following banking product")
        for eno, product in enumerate(prodList):
            print(f'{eno+1} - {product}')
        message = "\nEnter an option number from above -> "
        optionSelected = Customer.inputCheckInt(message, len(prodList))
        return optionSelected

    @staticmethod
    def chqAccount():
        productCode = "CHQ"
        chqAccountNumber = random.randint(40000000, 49999999)
        return productCode, chqAccountNumber

    @staticmethod
    def ccAccount(amount):
        if amount < 60000:
            productCode = "CBK"
        else:
            productCode = "CBW"
        ccCardNumber = random.randint(5360000000000000, 5360999999999999)
        return productCode, ccCardNumber

    @staticmethod
    def savAccount():
        productCode = "SAV"
        savAccountNumber = random.randint(30000000, 39999999)
        return productCode, savAccountNumber


def fileWriter(client_id):  # File writer based on client_id updates value in a list combining customer and product details for the specific client
    with open(fileName, "a") as db_txt_file:
        lineEntryToFile = []
        lineEntryToFile.extend(Customer.clientDetails(client_id))
        lineEntryToFile.extend(Product.productDetails(client_id))
        line = ",".join(str(entry) for entry in lineEntryToFile)
        db_txt_file.write(line+'\n')


class AdminOptions():  # no initialization of object in this class is created to group functions together

    @staticmethod
    def adminWelcomeScreen():
        print("\nHello Admin")
        adminOptions = ["Show total CHQ account", "Show total client",
                        "Show total based on product code CHQ,CBK,CBW,SAV", "Show customer more than annual income", "Quit Program"]
        for eno, product in enumerate(adminOptions):
            print(f'{eno+1} - {product}')
        optionSelected = Customer.inputCheckInt(
            "\nEnter an option number from above -> ", len(adminOptions))
        return optionSelected

    @staticmethod
    def fileReader(filename):
        try:
            with open(filename, "r") as db_txt_file_read:
                all_lines_in_list = []
                all_lines = db_txt_file_read.readlines()
                for items in all_lines:
                    lineItem = items.rstrip().split(',')
                    all_lines_in_list.append(lineItem)
                return all_lines_in_list
        except:
            print(f'\nError in finding or opening file - {filename}')

    @staticmethod
    # all_lines are all the entry in the input file it is a list of list format
    def totalByProductCode(all_lines, productCode):
        totalAccount = 0
        for entry in all_lines:
            if entry[4] == productCode:
                totalAccount += 1
        return productCode, totalAccount

    @staticmethod
    def totalCustomerAnnualIncome(all_lines, input_income):
        totalCustomers = 0
        for entry in all_lines:
            if float(entry[3]) >= input_income:
                totalCustomers += 1
        return totalCustomers


def clientInteractions():
    client_id = Customer.createClientID()
    Customer.createClient(
        client_id, returnList[1], returnList[2], returnList[3])  # 1,2 and 3 represent uname, age, amount
    optionSelected = Product.productsToEnroll()
    if optionSelected == 1:
        productCode, chqAccountNumber = Product.chqAccount()
        print(
            f'\nHi {returnList[1]} a new Chequing account ({productCode}) with number {chqAccountNumber} is created.')
        Product.clientProductMapping(
            client_id, productCode, chqAccountNumber)
        fileWriter(client_id)
    elif optionSelected == 2:
        productCode, ccCardNumber = Product.ccAccount(returnList[3])
        print(
            f'\nHi {returnList[1]} a new {productCode} credit card with number {ccCardNumber} is created.')
        Product.clientProductMapping(client_id, productCode, ccCardNumber)
        fileWriter(client_id)
    elif optionSelected == 3:
        productCode, savAccountNumber = Product.savAccount()
        print(
            f'\nHi {returnList[1]} a new Savings account ({productCode}) with number {savAccountNumber} is created.')
        Product.clientProductMapping(
            client_id, productCode, savAccountNumber)
        fileWriter(client_id)


def adminInteractions():
    all_lines_in_list = AdminOptions.fileReader(fileName)
    optionSelected = AdminOptions.adminWelcomeScreen()
    if optionSelected == 1:
        productCode, totalAccount = AdminOptions.totalByProductCode(
            all_lines_in_list, "CHQ")
        print(
            f'The total number of CHQ accounts = {totalAccount}')
    elif optionSelected == 2:
        print(f'The total number of clients = {len(all_lines_in_list)}')
    elif optionSelected == 3:
        validProdCodes = ["CHQ", "CBK", "CBW", "SAV"]
        while True:
            adminInputCode = input("\nEnter a product code -> ").upper()
            if adminInputCode not in validProdCodes:
                print(f'{adminInputCode} is not a valid code. Try again.')
                continue
            else:
                break
        productCode, totalAccount = AdminOptions.totalByProductCode(
            all_lines_in_list, adminInputCode)
    elif optionSelected == 4:
        adminInputCode = Customer.inputCheckFloat(
            "\nEnter the annual income amount -> ")
        totalCustomers = AdminOptions.totalCustomerAnnualIncome(
            all_lines_in_list, adminInputCode)
        print(
            f'The total number of clients with amount >= ${adminInputCode} = {totalCustomers}')
    elif optionSelected == 5:
        quitProgram()


fileName = "xyz_database.txt"
counter = 0
while True:
    if counter == 0:  # To print the welcome screen only on the first run
        returnList = Customer.welcomeScreen()
        counter += 1
    if returnList[0] == 'client':
        clientInteractions()
    elif returnList[0] == 'admin':
        adminInteractions()
    continueLoop = input(
        "\nDo you want to continue? Type Y for yes or hit any other key to quit program ")
    if continueLoop.upper() == "Y" and returnList[0] == 'client':
        counter += 1
        print(f'\nEnter details on {counter} client')
        returnList = Customer.client()
    elif continueLoop.upper() == "Y" and returnList[0] == 'admin':
        adminInteractions()
    else:
        quitProgram()
