#Create Bank Account Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance= balance

#Deposit method to deposit money 
    def deposit(self, amount):
        self.balance += amount
        print(f"Money deposited succesfully {amount} rupees. New balance: {self.balance} rupees.")
    
#Withdrow method for withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent funds.")
        else:
            self.balance -= amount
            print(f"Money withdraw succesfully {amount} rupees. New balance: {self.balance} rupees.")
      
#Check Balance 
    def check_balance(self):
        print(f"Current Balance: {self.balance} rupees.")
      

#Create main function to handle user interaction 
#Users can choose to create an account, Log In, or Exit 
def main():
    accounts = {}
    
    while True:
        print("\nWelcome to the Axis Bank")
        print("1. Create Account")
        print("2. Log in")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        #Now using 'if-elif' to respond
        if choice == "1":
            name = input("Enter your name: ")
            if name in accounts:
                print("Account already exists.")
            else:
                accounts[name] = BankAccount(name)
                print("Acount created successfully.")
        elif choice == "2":
          name=input("Enter your name:")
          if name in accounts:
             accounts = accounts[name]
             print(f"Welcome Back, {name}!")
          #Noe adding user intarection for deposit or withdraw money 
             while True:
                print("\n1.Check balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                option = input("Enter your option: ")

                if option == "1":
                    accounts.check_balance()
                elif option == "2":
                    amount = float(input("Enter the amount of deposit: "))
                    accounts.deposit(amount)
                elif option == "3":
                    amount = float(input("Enter amount to withdraw: "))
                    accounts.withdraw(amount)
                elif option == "4":
                    print("Looged out succesfully.")
                    break
                else:
                    print("Invalid Option. Please try again.")

#Now adding error handeling
             else:
                    print("Account not found. Please create an account first. ")

        elif choice == "3":
                    print("Thank You for using Axis Bank!")
                    break
        else:
            print("Invalid choice. Please try again")

#Now add logic to run our main function
if __name__ == "__main__":
    main()
                

            

