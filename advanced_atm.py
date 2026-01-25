print("Welcome to ATM")

balance = 67.14
chances = 3
restart = 'Y'
correct_pin = 1234

while restart.upper() == 'Y' and chances > 0:
    pin = int(input('\nPlease enter your 4 digit pin: '))
    
    if pin == correct_pin:
        print('You have entered your Pin Correctly \n')
        
        while restart.upper() == 'Y':
            print("Please press 1 for your balance")
            print("Please press 2 for your Withdraw")
            print("Please press 3 for your Pay in")
            print("Please press 4 for your Return Card\n")
            
            option = int(input('What would you like to choose? '))
            
            if option == 1:
                print(f'\nYour balance is Rs. {balance:.2f}\n')
                restart = input('Would you like to go back? (Y/N): ')
                
            elif option == 2:
                withdraw = float(input('How much money would you like to withdraw? Rs. '))
                if withdraw in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
                    balance = balance - withdraw
                    print(f"\nYour balance is now Rs. {balance:.2f}")
                    restart = input('Would you like to go back? (Y/N): ')
                else:
                    print("Invalid Amount, please Re-try\n")
                    
            elif option == 3:
                pay_in = float(input('How much would you like to pay in? Rs. '))
                balance = balance + pay_in
                print(f"Your balance is now Rs. {balance:.2f}")
                restart = input('Would you like to go back? (Y/N): ')
                
            elif option == 4:
                print("Please wait while your card is returned...\n")
                print("Thank you for your service")
                restart = 'N'
                break
                
            else:
                print("Invalid option, please try again\n")
        break
    else:
        print("Incorrect password")
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
        print(f"Chances remaining: {chances}\n")

print("\nThank you for using ATM")
