
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
                withdraw = float(input('How much money would you like to withdraw? $_.__ '))
                if withdraw in [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00, 24.00, 25.00, 26.00, 27.00, 28.00, 29.00, 30.00, 31.00, 32.00, 33.00, 34.00, 35.00, 36.00, 37.00, 38.00, 39.00, 40.00, 41.00, 42.00, 43.00, 44.00, 45.00, 46.00, 47.00, 48.00, 49.00, 50.00, 51.00, 52.00, 53.00, 54.00, 55.00, 56.00, 57.00, 58.00, 59.00, 60.00, 61.00, 62.00, 63.00, 64.00, 65.00, 66.00, 67.00, 68.00, 69.00, 70.00, 71.00, 72.00, 73.00, 74.00, 75.00, 76.00, 77.00, 78.00, 79.00, 80.00, 81.00, 82.00, 83.00, 84.00, 85.00, 86.00, 87.00, 88.00, 89.00, 90.00, 91.00, 92.00, 93.00, 94.00, 95.00, 96.00, 97.00, 98.00, 99.00, 100.00]:
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
