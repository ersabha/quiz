# 1.code to convert an Integer to string in Python
s = 11
str(s)

#2. Mr. Robben in a variable age = 33 and code to output a string Age of Mr. Robben is 33 years.
age = 33
print ("age of Mr. Robben is :- " + str(age))

# 3. code to input a number and return a string +ve if the number is > o, -ve if the number is < 0 and Aryabhatta otherwise.
a = int(input("Enter number: "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Aryabhatta")
