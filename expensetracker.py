import time
#toread choice
while(True):
    print("------------------------------------------------------------------------------------------------")
    print("Menu\n1.Add Expense\n2.Add Income\n3.view Balance\n4.View Expense\n5.Edit/Delete Expense\n6.Edit/Delete Income\n7.Set Budget\n8.Exit")
    print("------------------------------------------------------------------------------------------------")
    choice=int(input("Enter your choice:"))
    if(choice==1): 
        print("calling")
        #call add expense()
    elif(choice==2):
         print("calling")
        #call add income()
    elif(choice==3):
        print("calling")
        #call view Balance()
    elif(choice==4):
         print("calling")
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