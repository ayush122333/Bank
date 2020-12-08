class Banks:
    def __init__(self, name):
        self.name = name
        self.info = {}

    def disInfo(self, user):
        try:
            amountLeft = self.info.pop(user)
            print(f"Name: {user}, Amount left: {amountLeft}")
        except Exception as e:
            print("oops!! looks like you don't have an account associated with this bank.")

    def deposit(self, user, amount):
        self.info.update({user:amount})

    def withdraw(self, user, amount):
        try:
            amountLeft = self.info.pop(user) - amount
            self.info.update({user:amountLeft})
            print("updated")
        except Exception as e:
            print("oops! you don't have an account.")

ayush = Banks("Ayush")

if __name__ == "__main__":
    while True:
        print("In which Bank you want to deposit the money? ")
        print("Associated Banks:-")
        print("1: Dena Bank")
        print("2: SBI")
        print("3: BOB")
        print("4: YES Bank")
        print("5: Vijaya Bank")

        inp = int(input("enter the nummber from 1 to 5: "))

        if inp==1:
            choice = int(input("press 1 to see info, 2 to deposit and 3 to withdraw: "))

            if choice==1:
                name = input("Enter your name: ")
                ayush.disInfo(name)

            elif choice==2:
                name = input("Enter your name: ")
                amount = int(input("enter the amount: "))
                print(f"amount: {amount} has been added to your account.")
                ayush.deposit(name, amount)

            elif choice==3:
                name = input("Enter your name: ")
                amount = int(input("Enter the amount: "))
                ayush.withdraw(name, amount)
            
        elif inp==2:
            choice = int(input("press 1 to see info, 2 to deposit and 3 to withdar: "))

            if choice==1:
                name = input("Enter your name: ")
                ayush.disInfo(name)

            elif choice==2:
                name = input("enter your name: ")
                amount = input("enter the amount: ")
                print(f"amount: {amount} has been added to your account.")
                ayush.deposit(name, amount)

            elif choice==3:
                name = input("Enter your name: ")
                amount = int(input("Enter the amount: "))
                ayush.withdraw(name, amount) 

        elif inp==3:
            choice = int(input("press 1 to see info, 2 to deposit and 3 to withdar: "))

            if choice==1:
                name = input("Enter your name: ")
                ayush.disInfo(name)

            elif choice==2:
                name = input("enter your name: ")
                amount = input("enter the amount: ")
                print(f"amount: {amount} has been added to your account.")
                ayush.deposit(name, amount)

            elif choice==3:
                name = input("Enter your name: ")
                amount = int(input("Enter the amount: "))
                ayush.withdraw(name, amount)  

        elif inp==4:
            choice = int(input("press 1 to see info, 2 to deposit and 3 to withdar: "))

            if choice==1:
                name = input("Enter your name: ")
                ayush.disInfo(name)

            elif choice==2:
                name = input("enter your name: ")
                amount = input("enter the amount: ")
                print(f"amount: {amount} has been added to your account.")
                ayush.deposit(name, amount)

            elif choice==3:
                name = input("Enter your name: ")
                amount = int(input("Enter the amount: "))
                ayush.withdraw(name, amount)    

        elif inp==5:
            choice = int(input("press 1 to see info, 2 to deposit and 3 to withdar: "))

            if choice==1:
                name = input("Enter your name: ")
                ayush.disInfo(name)

            elif choice==2:
                name = input("enter your name: ")
                amount = input("enter the amount: ")
                print(f"amount: {amount} has been added to your account.")
                ayush.deposit(name, amount)

            elif choice==3:
                name = input("Enter your name: ")
                amount = int(input("Enter the amount: "))
                ayush.withdraw(name, amount)     

        else:
            print("oops!! invalid choice.")
            inp = input("press 'q' to quit and 'c' to continue: ")    

            if inp == 'q' or inp == 'Q':
                exit()
            elif inp == 'c' or inp == 'C':
                continue                 



