# This is a fun hello script!
print("Hello! What's your name?")  # Ask the kid for their name
name = input()  # Take input from the user
print("Nice to meet you, " + name + "!")  # Greet them

print("Let's do a simple math question")
print("What's 2 + 3?")
answer = input()
if answer == "5":
    print("Correct! 🎉")
else:
    print("Oops! The answer is 5.")

print("Now let's do a harder one! This will give you 5 tries")
i = 1
print("What is 6 x 12?")
while i<=5: 
    answer = input()
    if answer == "72":
        print("Correct! 🎉")
        break
    elif i == 5:
        print("Oops! You have exhausted all the tries. The answer is 72.")
        break
    elif i == 4:
        i=i+1
        print("Last try!!!!!!")
    else:
        i = i+1
        result = 6 - i
        print("Try again! You have " + str(result) + " tries left!!!")
print ("Now lets do a extream one. This will give you 10 tries.")
i=1
print("What is 175 x 14")
while i<=10:
    answer = input()
    if answer == "2450":
        print ("Correct! 🎉")
        break
    elif i == 10:
        print ("Oops! You have exhausted all the tries. The answer is 2450")
        break
    elif i == 9:
        i=i+1
        print("Last try!!!!!!")
    else:
        i=i+1
        result = 11-i
        print("Try again! you have " + str(result) + "  tries left!!!")
print("Next is an insane Question!!! This will give you 15 tries")
i=1
print("What is 789 x 456")
while i<=20:
    answer == input()
    if answer == "359784"
        print ("Correct!🎉")
        break
    elif i == 15:
        print ("Oops! You have exhausted all the tries. The answer is 359784")
        break
    elif