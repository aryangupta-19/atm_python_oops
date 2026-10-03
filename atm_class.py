class Atm:
    # Here in python can declare variable in method only not outside like c++
    def __init__(self):         # In python constructor's name is fixed __init__, constuctor is a magic method -> (__abc___)
        self.__pin = ""
        self.__balance = 0
        self.menu()
        
    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin Changed")
    
    def menu(self):
        # while True:
            user_input = input("""
                    Hello would You like to proceed?
                    1) Enter 1 to create __pin
                    2) Enter 2 to deposit 
                    3) Enter 3 to withdraw
                    4) Enter 4 to check __balance
                    5) Enter 5 to exit    
            """)
            
            if user_input == '1':
                self.create___pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check___balance()
            elif user_input == '5':
                print("Bye")
            else:
                print("Invalid option")
        
    def create___pin(self):
        self.__pin = input("Enter your __pin: ")        
        print("__pin set succesfully!")
        
    def deposit(self):
        temp = input("Enter your __pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount 
            print("Deposit Succesfull")
        else: print("Invalid __pin!")
        self.menu()
                
    def withdraw(self):
        temp = input("Enter your __pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount 
                print("Withdraw Succesfull")
            else: print("Insufficient __balance")
        else: print("Invalid __pin!")
        self.menu()
        
    def check___balance(self):
        temp = input("Enter Your __pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else: print('Invalid __pin') 
        self.menu()
    
    
# Now if created sbi = Atm() and deposit 100 also created hdfc = Atm() then deposited 200 
# sbi.check___balance() will give 100 and hdfc.check___balance() gives 200 though there is only one variable __balance but here all instances have their own __balance attribute or field 

# Note magic_methods (__m__) all magic methods are auto invoked they are not invoked manually by object
# We generally add things in constructor for which we can't rely on user, user can't access and control these things, in contructor we try to add functionality which we want to auto execute without user's interference  

# self is actually the object -> means self ka address = sbi ka address 
# also self ka address vahi hota hai jis object ke sath hum abi kam kr rhe hai 

# Why self is required -> we know each class have data attributes + method also we know methods of particular class can be accesed by only that class's object also note one method of class can't access other method of same class
# therefore we use self as object so that different methods to same class can access eachother 

# Python can't store numbers in fractional it converts all fraction into decimal 
# Now we will make a class that will store fractions 

# Note first of all in python to make private variables in class -> __varname
# Lets make our __pin and __balance private so that no one can access it outside class 

# How it hides -> see python converts it intenally to _Atm__pin
# sbi.__balance = 10 -> will create a new variable __balance but all out methods are using _atm__balance so no problem with creation of this variable

# but sbi._Atm__balance = 100 will actually save 100 in balance -> hence nothing in python is truely private one can access pvt variables using _className__variables 

# Recall we create getter and setter for private variables therefore protected directly and provided access using functions therefore if you want to access my variables go through code functionality and change according to my rules only 

# Therefore here data methods and variables are working together -> this is encapsulation 

