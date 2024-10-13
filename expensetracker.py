import time
addexpense=[]
addincome=[]
class expense:
    def addexpense():
        expense=int(input("Enter the your Expense:"))
        addexpense.append(expense)
        total=sum(addexpense)
        print(total)
    def addincome():
        income=int(input("Enter your income:"))
        addincome.append(income)
        totalin=sum(addincome)
    def balance():
        balance=sum(addincome)-sum(addexpense)
        print("The remaining amount:",balance)
    def viewexpense():
        for i in range(len(addexpense)):
            print(addexpense[i])
        
#toread choice
while(True):
    print("------------------------------------------------------------------------------------------------")
    print("Menu\n1.Add Expense\n2.Add Income\n3.view Balance\n4.View Expense\n5.Edit/Delete Expense\n6.Edit/Delete Income\n7.Set Budget\n8.Exit")
    print("------------------------------------------------------------------------------------------------")
    choice=int(input("Enter your choice:"))
    if(choice==1): 
        print("calling")
        expense.addexpense()
    elif(choice==2):
         print("calling")
         expense.addincome()
    elif(choice==3):
        print("calling")
        expense.balance()
    elif(choice==4):
         print("calling")
         expense.viewexpense()
        #call view Expense()
    elif(choice==5):
        print("calling")
        #call Edit/Delete Expense()
    elif(choice==6):
        print("calling")
        #call Edit/Delete Income()
    elif(choice==7):
        print("calling")
        #call Set Budget()
    elif(choice==8):
        break
    else:
        print("Invalid input")
    time.sleep(2)