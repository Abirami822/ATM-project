print("Welcome To Central Bank Of India.....")
acc_type="s"
x=input("Enter the account type:")
if (acc_type==x):
    print("This is a savings account.")

    print("1-Withdraw")
    print("2-Check balance")
    print("3-Deposit")
    print("4-Change pin")
    print("5-Exit")
    for i in range(5):
        ch=int(input("Enter your choice:"))
        bal = 50000
        m = 2000
        if(ch==1):
            print("You have chosen withdraw!")
            w=int(input("Enter the Withdraw amount:"))
            p = int(input("Enter your 4 digit pin number:"))
            if(p==1020):
                wa=bal-w
                if (wa<=m):
                     print("Less than minimum balance.")
                else:
                    print(f"Amount withdraw is {w}")
                    q=input("press 'y' or 'n' for check balance:")
                    if (q=='y'):
                        print("balance = ",wa)
                        print("Thank You For Visiting Central Bank Of India ATM!")
                    elif (q=='n'):
                        print("Thank You For Visiting Central Bank Of India ATM!")


        elif(ch==2):
            print("You have chosen check Balance!")
            p = int(input("Enter your 4 digit pin number:"))
            if (p == 1020):
                print(f"The Balance amount in your account is {bal}")
                print("Thank You For Visiting Central Bank Of India ATM!")
            else:
                print("Enter the valid pin")

        elif(ch==3):
            print("You have chosen Deposit!")
            d=int(input("Enter the deposit amount:"))
            p = int(input("Enter your 4 digit pin number:"))
            if(p==1020):
                tot=bal+d
                print(f"The amount deposited in your account is {d}")
                print(f"The total amount in your account is {tot}")
                print("Thank You For Visiting Central Bank Of India ATM!")
            else:
                print("Enter the valid pin")

        elif(ch==4):
            print("You have chosen Change Pin!")
            old_pin=int(input("Enter the old pin:"))
            if(old_pin==1020):
                new_pin=int(input("Enter the new pin:"))
                if(new_pin>=1000 and new_pin<=9999):
                    new_pin1=int(input("Enter the new pin again:"))
                    if(new_pin==new_pin1):
                        print("Pin changed successfully!")
                    else:
                        print("Enter the same pin mentioned in new_pin")
                else:
                    print("Enter valid 4 digit pin number")
            else:
                print("Invalid pin number")

        elif(ch==5):
            break

        else:
            print("Enter valid Choice")

else:
    print("Enter valid account type")