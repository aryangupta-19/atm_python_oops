class Atm:
    # Here in python can declare variable in method only not outside like c++
    def __init__(self):         # In python constructor's name is fixed __init__, constuctor is a magic method -> (__abc___)
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        # while True:
            user_input = input("""
                    Hello would You like to proceed?
                    1) Enter 1 to create Pin
                    2) Enter 2 to deposit 
                    3) Enter 3 to withdraw
                    4) Enter 4 to check balance
                    5) Enter 5 to exit    
            """)
            
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Bye")
            else:
                print("Invalid option")
        
    def create_pin(self):
        self.pin = input("Enter your pin: ")        
        print("Pin set succesfully!")
        
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance = self.balance + amount 
            print("Deposit Succesfull")
        else: print("Invalid Pin!")
        self.menu()
                
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount < self.balance:
                self.balance = self.balance - amount 
                print("Withdraw Succesfull")
            else: print("Insufficient balance")
        else: print("Invalid Pin!")
        self.menu()
        
    def check_balance(self):
        temp = input("Enter Your pin: ")
        if temp == self.pin:
            print(self.balance)
        else: print('Invalid Pin') 
        self.menu()
    
    
# Now if created sbi = Atm() and deposit 100 also created hdfc = Atm() then deposited 200 
# sbi.check_balance() will give 100 and hdfc.check_balance() gives 200 though there is only one variable balance but here all instances have their own balance attribute or field 

# Note magic_methods (__m__) all magic methods are auto invoked they are not invoked manually by object
# We generally add things in constructor for which we can't rely on user, user can't access and control these things, in contructor we try to add functionality which we want to auto execute without user's interference  

# self is actually the object -> means self ka address = sbi ka address 
# also self ka address vahi hota hai jis object ke sath hum abi kam kr rhe hai 

# Why self is required -> we know each class have data attributes + method also we know methods of particular class can be accesed by only that class's object also note one method of class can't access other method of same class
# therefore we use self as object so that different methods to same class can access eachother 

# Python can't store numbers in fractional it converts all fraction into decimal 
# Now we will make a class that will store fractions 

