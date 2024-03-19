
#choice=>pin=>witham/depost

pin=223344
mainbalance=30000
print("welcome to ATM")
print (" 1.withdraw\n 2.deposit\n 3.mainbalancen \n 4.exit")
choice=int(input("enter your choice"))
yourpin=int(input("ENTER YOUR PIN :"))
if pin==yourpin:
    if choice==1:
        withamount=int(input("Enter your withdraw amount:"))#30000
        if(withamount>0 and withamount<=mainbalance):
            mainbalance=mainbalance-withamount
            print("Withdraw successfully")
            print("After withdraw mainbalance",mainbalance)
        else:
            print("insufficent amount")
    elif choice==2:
         deposit=int(input("enter your deposit ammount"))
         if(deposit>0 and mainbalance>=deposit):
             mainbalance = mainbalance+deposit
             print("deposit succesfull")
             print("after deposit mainbalance",mainbalance)
         else:
             print("enter valid ammount")

    elif choice==3:
          print ("your main balance is ",mainbalance)
    elif choice==4:
          print("thanks for visiting our ATM")
    else:
         print("enter valid choice")

else:
    print("your pin is incorrect")


             
   
    




