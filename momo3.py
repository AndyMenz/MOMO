import os
def momo_menu1():
    while True:
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
        if choice == 1:
            choice1=int(input("""
            1 Vodafone Network
            2 Other Networks
            3 To Bank  Account
            4 E-zwich
            0 Back

             """))
            if choice1==1:
                choice11=int(input("""
                Choose the receiver
                1 To enter recipient number
                2 My List
                0 Return to Main Menu
                """))
                if choice11==0:
                    pass
            elif choice1==2:
                choice12=int(input("""
                Please choose network
                1 MTN
                2 AirtelTigo
                3 G-Money
                4 ZeePay
                5 GhanaPay
                0 Back
                """))
                if choice12==0:
                    pass
            elif choice1==3:
                choice13=int(input("""
                Select your bank starting with alphabet:
                1 A-D
                2 E-F
                3 G-R
                4 S-Z
                0 Return to Main Menu

                """))
                if choice13==0:
                    pass
            elif choice1==4:
                choice14=int(input("Enter Account Number"
                                   ))
            elif choice1==5:
                choice15=int(input("""
                Select your bank
                1 A-D
                2 E-G
                3 H-R
                4 S-Z
                """))
            elif choice1==6:
                choice16=int(input("""
                A voucher will be generated for withdrawal
                at an Agent Point by the receiver.
                1 TO enter receipient number
                2 My List
                """))
            elif choice1==0:
                pass


            
        elif choice==2:
            choice2=int(input("""
            Withdraw Cash
            1 From Agent
            2 From ATM
            0 Back

            """))
            if choice2==1:
                choice21=int(input("""
                Enter till no:

                """))
                if choice21==0:
                    pass
            elif choice2==2:
                choice22=int(input("""Please enter PIN to receive voucher.
                
                """))
            elif choice2==0:
                pass
        
        elif choice==3:
            choice3=int(input("""
            Buy Airtime ot Data
            1 Buy Airtime
            2 Buy Data/ 2 Moorch
            3 Special offers

            """))
            if choice3==1:
                choice31=int(input("""
                Buy Airtime
                1 My Phone
                2 Other Vodafone Number
                3 Landline
                4 Other Networks
                5 Back

                """))
                if choice31==5:
                    pass
            elif choice3==2:
                choice32=int(input("""
                Buy Data/2Moorch
                1 Buy Data/ 2 Moorch

                """))
        elif choice==4:
            choice4=int(input("""
            Make Payments
            1 Pay Bill
            2 Buy Goods
            3 Fun and Games
            4 Generate Voucher
            5 My List
            6 Pay Small Small
            7 Donations
            8 Complete Payment/Transaction
            9 Schemes
            10 School Payments
            0 Back

            """)) 
            if choice4==0:
                pass
        elif choice==5:
            choice5=int(input("""
            Select Option
            1 Insurance
            2 Pensions
            3 Loans
            4 Overdraft
            5 Savings
            6 Bank Services
            0 Back

            """))
            if choice5==0:
                pass
        elif choice==6:
            choice6=int(input("""
            My Account
            1 Check Balance
            2 My Statements
            3 Change Pin
            4 Account Information
            5 My List
            6 Help
            7 Self-Service
            0 Back

            """))
        elif choice==7:
            choice7=int(input("""
            Select Action
            1 Reset PIN
            2 Self-Reversal(Vodafone/Voucher)
            3 Request Reversal(Other Networks)
            """))
momo_menu1()


    