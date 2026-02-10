print("Welcome to ATM")
restart = ('Y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input('Please enter your 4 digit pin:'))
    if pin == (1234):
            print('You have entered your Pin Correctly \n')

            while restart not in ('n', 'no', 'No', 'N'):
                  print("Please press 1 for your balance \n")
                  print("Please press 2 for your Withdrawl \n")
                  print("Please press 3 for your Pay in  \n")
                  print("Please press 4 for your Return Card /n")
                  option = int (input('What would you like to choose?'))
                  if option == 1:
                        print ('Your balance is Rs.', balance, '\n')
                        restart = input('Would you like to go back?')
                        if restart in  ('n', 'no', 'No', 'N'):
                              print ("Thank you")
                              break
                  elif option == 2:
                        option2 = ('Y')
                        Withdrawl = float(input('How much money would you like to withdraw? \n Rs. 10/Rs. 20/Rs. 30/Rs. 40/Rs. 50/Rs. 60/Rs. 70/Rs. 80/Rs. 90/Rs. 100'))
                        if Withdrawl in [10,20,30,40,50,60,70,80,90,100]:
                              balance = balance - Withdrawl
                              print("\n your balance is now Rs.", balance)
                              if restart in ('n', 'no', 'No', 'N'):
                                    print("Thank you")
                                    break
                        elif Withdrawl != [10,20,30,40,50,60,70,80,90,100]:
                              print("Invalid Amount, please Re-try\n")
                              restart = ('Y')
                        elif Withdrawl == 1:
                              Withdrawl = float(input('Please enter desiered amount:'))
                  elif option == 3:
                        Pay_in = float(input("How much would you like to pay in?"))
                        balance = balance + Pay_in
                        print("your balance is now Rs.", balance)
                        restart = input("Would you like to go back?")
                        if restart in ('n', 'no', 'No', 'N'):
                              print ("Thank you")
                              break
                  elif option == 4:
                        print("Please wait while your card is reterun...\n")
                        print("Thank you for your service")
                        break 
      elseif:
            restart = ('Y')
      else:
            if pin != (1234):
                  print("Incorrect password")
                  chances = chances-1
            if chances == 0:
                  print('\n No more tries')
                  break 
    
    