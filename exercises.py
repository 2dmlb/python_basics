#calculate age

birth_year=input("Enter your birth year: ")
birth_year=int(birth_year)

current_year=2025

print("Your age is: ",current_year-birth_year)



#calculate area of rectangle

short_side=input("Enter short side of rectangle: ")
short_side=int(short_side)

long_side=input("Enter long side of rectangle: ")
long_side=int(long_side)

area=short_side*long_side

print("Area of rectangle is: ",area)



#roll a dice
import random

dice=random.randrange(1,7)
print("You rolled a dice and got: ",dice)



#length of string
length_of_word=input("Enter a word for length of the word: ")
print("Length of the word is: ",len(length_of_word))



#name cleanup and uppercase
name=input("Enter your name: ")
clean_name=name.strip().upper()
print("HELLO ",clean_name)



#enter your password

user_pass=input("Enter your password: ")

if user_pass==password:
    print("Login Successful")
else:
    print("Login Failed")



#secret message system
password="dml002"
user_pass=input("Enter your password: ")

if user_pass==password:
    secret_mess=input("Enter your secret messages: ")
    print(secret_mess.lower())
else:
  print("Wrong answer")

    
    




