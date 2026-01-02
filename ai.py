print("Comparison Operators in Python. \n")
print("1. Equal to (==)")
print("2. Not equal to (!=)")
print("3. Greater than (>)")
print("4. Less than (<)")
print("5. Greater than or equal to (>=)")
print("6. Less than or equal to (<=)\n")


print("Let's see some examples: \n")
100==100
print("100 == 100 : ", 100 == 100)  # True
100!=200
print("100 != 200 : ", 100 != 200)  # True
150>50
print("150 > 50 : ", 150 > 50)      # True
50<150
print("50 < 150 : ", 50 < 150)      # True
200>=200
print("200 >= 200 : ", 200 >= 200)  # True
100<=200
print("100 <= 200 : ", 100 <= 200)  # True
print("\nThese operators help in making decisions in code, like in if statements and loops.")
print("That's all for now on comparison operators!")
print("\n\nLogical Operators in Python. \n")
print("1. and")
print("2. or")
print("3. not\n")
print("Let's see some examples: \n")
True and False
print("True and False : ", True and False)  # False
True or False
print("True or False : ", True or False)    # True
not True
print("not True : ", not True)                # False
print("\nThese operators help combine multiple conditions in code.")
print("That's all for now on logical operators!")
print("\n\nMembership Operators in Python. \n")
print("1. in")
print("2. not in\n")
print("Let's see some examples: \n")
'a' in 'apple'
print("'a' in 'apple' : ", 'a' in 'apple')        # True
'b' not in 'apple'
print("'b' not in 'apple' : ", 'b' not in 'apple')  # True
print("\nThese operators check for presence of elements in sequences like strings, lists, etc.")
print("That's all for now on membership operators!")
print("\n\nIdentity Operators in Python. \n")
print("1. is")
print("2. is not\n")
print("Let's see some examples: \n")
a = [1, 2, 3]
b = a
a is b
print("a is b : ", a is b)            # True
a is not [1, 2, 3]
print("a is not [1, 2, 3] : ", a is not [1, 2, 3])  # True
print("\nThese operators check if two variables point to the same object in memory.")
print("That's all for now on identity operators!")
print("\n\nBitwise Operators in Python. \n")
print("1. AND (&)")
print("2. OR (|)")
print("3. XOR (^)")
print("4. NOT (~)")
print("5. Left Shift (<<)")
print("6. Right Shift (>>)\n")
print("Let's see some examples: \n")
a = 5  # In binary: 0101
b = 3  # In binary: 0011
a & b
print("5 & 3 : ", a & b)    # 1 (0001)
a | b
print("5 | 3 : ", a | b)    # 7 (0111)
a ^ b
print("5 ^ 3 : ", a ^ b)    # 6 (0110)
~a
print("~5 : ", ~a)          # -6 (inverts bits)
a << 1
print("5 << 1 : ", a << 1)  # 10 (1010)
a >> 1
print("5 >> 1 : ", a >> 1)  # 2 (0010)
print("\nThese operators perform bit-level operations on integers.")
print("That's all for now on bitwise operators!")
print("\n\nThat's all for today! You've learned about Comparison, Logical, Membership, Identity, and Bitwise operators in Python. Keep practicing to master them!")