from random import *
class User:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def show_User_Details(self):
        print('\n')
        print('*** Personal Details ***')
        print('Name : ',self.name)
        print('Age : ', self.age)
        print('Gender : ', self.gender)
        print('Address : ', self.address)
        print('\n')
class Bank(User):
    def __init__(self,name,age,gender,address):
        super().__init__(name,age,gender,address)
        self.balance=0
    def Deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print('\n')
        print(self.amount,'Amount is Deposited , Your Account Balance is : ₹',self.balance)
        print('\n')
    def Withdrawal(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print('\n')
            print('Not Sufficient Balance In Your Account, Add More funds to withdrawal')
            print('\n')
        else:
            self.balance=self.balance-self.amount
            print('\n')
            print(self.amount,' is Withdrawal , Remaining Amount In Your Account is : ₹',self.balance)
            print('\n')
    def view_balance(self):
        if self.balance==0:
            print('\nYour Current balance is : ₹',self.balance)
            print('\nAdd Some Money To Your Account')
        else:
            self.show_User_Details()
            print('\nYour Current balance is : ₹', self.balance)
    def UpdateDetails(self,uname,uage):
        self.name=uname
        self.age=uage
        print('\nYour Data is Updated \n')
        self.show_User_Details()








print('\n*** WELCOME TO BANK MANAGEMENT SYSTEM ***\n')
print('*** Please Create an Account ***')
Name=input('Enter Your Name :')
Age=int(input('Enter Your Age :'))
Gender=input('Enter Your Gender :')
Address=input('Enter Your Address :')
bank=Bank(Name,Age,Gender,Address)
a=randint(1,10)
print('** Verification Number **')
print(a)
print('**  **')
print('Enter the Number on screen to create your account')
b=int(input('Enter  Number '))

if b==a:
    print('Account is created')
    while True:
        if bank:

            print('To Do More Action with Your Account Choose the Below ,press the keys')
            print('1.See Details\n2.Deposit\n3.Withdrawal\n4.View balance\n5.Update Details\n 6.To Exit')
            n=int(input('Enter Your Choice:'))
            if n==1:
                bank.show_User_Details()
            elif n==2:
                print('\n** DEPOSIT SECTION **')
                amount=int(input('Enter Your Amount To deposit :'))
                bank.Deposit(amount)
            elif n==3:
                print('\n** WITHDRAWAL SECTION **')
                withdrawal_amount = int(input('Enter Your Amount To Withdrawal :'))
                bank.Withdrawal(withdrawal_amount )
            elif n==4:
                bank.view_balance()
            elif n == 5:
                name=input('Enter Your Updated Name :')
                age = int(input('Enter Your Updated Age :'))
                bank.UpdateDetails(name,age)
            elif n==6:
                print('\nYou Are Exited From bank')
                print('\n*** THANK YOU VISIT AGAIN ***')
                break
            else:
                print('\nYou Are Exited From bank')
                print('\n*** THANK YOU VISIT AGAIN ***')
                break


        else:
            print('Error in Creating')
else:
    print('Your Account is not created')