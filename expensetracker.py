import time
addexpense=[]
addincome=[]
class expense:
    def addexpense():
        expense=int(input("Enter the your Expense:"))
        addexpense.append(expense)
        total=sum(addexpense)
        print("Expense Added successfully...!")
    def addincome():
        income=int(input("Enter your income:"))
        addincome.append(income)
        totalin=sum(addincome)
        print("Income Added successfully...!")
    def balance():
        balance=sum(addincome)-sum(addexpense)
        print("The remaining amount:",balance)
    def viewexpense():
        for i in range(len(addexpense)):
            print(i+1,".",addexpense[i])
        print("Total:",sum(addexpense))
    def viewincome():
        for i in range(len(addincome)):
            print(i+1,".",addincome[i])
        print("Total:",sum(addincome))
    def editexpense():
        print("1.Edit\n2.Delete")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            edit=int(input("Enter the value to Edit:"))
            edit1=int(input("Enter the value to change:"))
            while(True):
                for i in range(len(addexpense)):
                    if(edit in addexpense):
                        if addexpense[i]==edit:
                         addexpense[i]=edit1
                         break
                    else:
                         print("Enter the correct value..!")
                         expense.editexpense()
                break
        elif(choice==2):
              edit=int(input("Enter the value to Delete:"))
              if(edit in addexpense):
                    addexpense.remove(edit)
              else:
                  print("The Entered Value is not in expense list:")
                  expense.editexpense()
    def editincome():
        print("1.Edit\n2.Delete")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            edit=int(input("Enter the value to Edit:"))
            edit1=int(input("Enter the value to change:"))
            while(True):
                for i in range(len(addincome)):
                    if(edit in addincome):
                        if addincome[i]==edit:
                         addincome[i]=edit1
                         break
                    else:
                         print("Enter the correct value..!")
                         expense.editincome()
                break

        elif(choice==2):
              edit=int(input("Enter the value to Delete:"))
              if(edit in addincome):
                    addincome.remove(edit)
              else:
                  print("The Entered Value is not in expense list:")
                  expense.editincome()        
            
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
        expense.viewexpense()
        expense.editexpense()
    elif(choice==6):
        expense.viewincome()
        expense.editincome()
    elif(choice==7):
        print("calling")
        #call Set Budget()
    elif(choice==8):
        break
    else:
        print("Invalid input")
    print("please wait for 2 sec")
    time.sleep(2)