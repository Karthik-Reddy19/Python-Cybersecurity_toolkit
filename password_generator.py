import random
import string
letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation
all_characters=letters+digits+symbols
def password_gen(n):
    password=""
    for i in range(n):
        password+=random.choice(all_characters)
    return password
n=int(input("Enter the number of characters required:"))
print(password_gen(n))
# no=int(input("ENter the number of passwords you wwant"))
# for i in range(no):
#     print(password_gen(8))
choose=input("Enter the y/no")
while(choose!="y"):
    print(password_gen(n))
# if (choose=="no"):
#     print(password_gen(n))
# else:
#     print("Thank You for using password generator")