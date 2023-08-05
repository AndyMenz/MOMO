import os
def momo_menu():
    choice=int(input("""
     Welcome to MTN mobile money
     Please select from the options given;
     1. Send Money
     2. Withdraw Cash
     3. Buy Airtime or Data
     4. Make Payments
     5. Financial Services
     6. My Account
     7. Self Services
       """))
    os.system('cls')
    #SEND MONEY
    if choice == 1:
        choice1=int(input("""
        1. MTN Network
        2. Other Networks
        3. To Bank Account
        4. E-zwich
        5. From Linked Bank Account
        6. To Unregistered 
        0. Back
         """))
        #MTN NETWORK
        if choice1==1:
            choice1a=int(input("""
            1.To enter revipient number
            2.My list
            0. Return to Main Menu
            """))
            os.system('cls')
            #OTHER NETWORK
        elif choice1 == 2:
            choice1b = int(input("""
            Please choose network
            1.Vodafone
            2.AirtelTigo
            3.G-Money
            4.ZeePay
            5.GhanaPay
            0.Back
            """))
            os.system('cls')
            #TO BANK ACCOUNT
        elif choice1 == 3:
            choice1c = int(input("""
            Select your bank starting with alphabet:
            1. A-D
            2. E-F
            3. G-R
            4. S-Z
            0. Return to Main Menu
                """))
            os.system('cls')
        elif choice1==4:
            choice1d =input("""
            Enter Account Number
            """)
            os.system('cls')
        elif choice1==5:
            choice1e = int(input("""
            Select Option
            1. Insurance
            2. Pension
            3. Loans 
            4. Overdraft
            5. Savings
            6. Bank Sevices 
            0. Back
            """))
            os.system('cls')

        elif choice1==6:
            choice1f = int(input("""
            My Account
            1. Check Balance
            2. My Statements
            3. Change Pin
            4. Account Information
            5. My List
            6. Help
            7. Self-Service
            0. Back


            """))
            os.system('cls')
        elif choice1==7:
            choice1g=int(input("""
            Select Action
            1. Reset PIN 
            2. Self-Reversal(MTN/Voucher)
            """))
#WITHDRAW CASH
    elif choice == 2:
        choice2 =int(input("""
        Withdraw Cash
        1. From Agent
        2. From ATM
        0. Back
        
        """))
    elif choice==3:
        choice3=int(input("""
        Buy Airtime or Data
        1. Buy Airtime
        2. Buy Data/ 2Moorch
        3. Special offers
        
        """))
    else:
        print ('Wrong Entry')
momo_menu()
