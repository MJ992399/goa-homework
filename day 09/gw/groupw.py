#ვამოწმებთ არის თუარა შემოსული პირი რობოტი.
name = input("checking are you robot or not > please enter the equal sign ")
if name == ("="):

    print("you are not robot : WELCOME")
 #დაბეჭდე ვარიანტები ნუმერაციით რათა კლიენტმა აირჩიოს სასურველი.





 #შექმენით ბანკის პროექტი, გამოიყენეთ უკვე ნასწავლი მასალა და ინტერნეტის დახმარებით მოიძიეთ ახალი ინფორმაცია


# #დაბეჭდე პირველი მესიჯი რომელსაც კლიენტი ნახავს როდესაც მობაილ ბანკში შევა.


print("------Welcome to Mobile Bank!------")

 #დაბეჭდე ვარიანტები ნუმერაციით რათა კლიენტმა აირჩიოს სასურველი.
#გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()


print("for registration press 1:")
print("to change password press 2:")
print("to check balance press 3: ")
print("for loan press 4:")
print("credit card 5:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

# #ინფუთ ფუნქციით მომხმარებელს შეაყვანინე  სასურველი ვარიანტი
operation=(input("choose an operation:"))


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
# #if, elif da else ოპერატორით შეამოწმე რომელი ოპერაცია აირჩია კლიენტმა.
if operation == "1":
     print("registration")
     
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
     print()
elif operation=="2":
     print("change password")
     
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
     print()
elif operation=="3":
     print("check balance")
     
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
     print()
elif operation=="4":
     print("loan")
   
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
     print()
elif operation==5:
     print("credit card")

     
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
     print()
else:
   print("invalid choise,please enter a valid number")


# print("welcome to the mobile banking registration")

# #რეგისტრაციისთვის კლიენტს შემოვატანინოთ პირადი მონაცემები



 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

name=input("please enter your full name:")
phone_number=input("please enter your phone number:")
date_of_birth=input("please enter your date of birth:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

print("Congratulations! You have successfully registered for Mobile Banking")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
# #დავპრინტოთ რამდენიმე ვარიანტი რათა კლიენტმა აირჩიოს სასურველი


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
print("Your account requires verification to proceed. Please complete the verification process to gain access.")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

print("please select a verification method")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
print("to select passport number press (1):") 
print("to select identification number press  (2):")
print("to select social security number press (3):")
# #input-ის დახმარებით მომხმარებელს შემოვატანინოთ სასურველი ვარიანტი032

 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

verification_method = input("Enter your choice (1, 2, or 3): ")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
if verification_method=="1":
    print(" passport number:")
elif verification_method=="2":
     print(" id number:")
elif verification_method=="3":
     print("ssn number:")
else:
    print("selected number doesn't exist, please try again")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
id=input("Please enter identification number:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
print("Your account has been successfully verified.")

 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

#შევქმნათ ცვლადი და მივანიჭოთ მნიშვნელობა მომხმარებლის სახელი და პაროლი
user_name = "mariami"
password = 123321


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

input_user = input("Please enter your username: ")
input_password = input("Please enter your password: ")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
# #შეამოწმე ემთხვევა თუ არა დეტალები ერთმანეთს


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

if input_user == user_name and int(input_password) == password:
    print("Welcome to your mobile bank")
    
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
    print()
else:
     print("User cannot be found")

 
 
 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

#ინფუთით მომხმარებელს ვკითხოთ სურს თუ არა სცადოს ხელახლა
response=input("would you like to try again? yes/no :")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
#შევქმნათ ცვლადი და შევინახოთ მომხმარებლის სახელი და პაროლი
user_name = "mariami"
password = 123321


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

input_user = input("Please enter your username: ")
input_password = input("Please enter your password: ")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
if input_user==user_name:
     print("correct user")
elif input_password==password:
     print("correct password")
else:
     print("user can not be found,please contac costumer service")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
#ჩატბოVტში დავპრინტოთ ველქამ მესიჯი და ვარიანტები


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
#ჩატბოტში დავპრინტოთ ველქამ მესიჯი და ვარიანტები
print(".....Welcome to the Mobile Bank Chatbot.....!")
print("How can I assist you today? choose an options: ")
print("1. Balance")
print("2. Credit Card")
print("3. Password Reset")
print("4. Verification")
print("5. Transfer")
print("6. Exit")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
#მომხმარებელს შემოვატანინოთ სასურველი ციფრი ინფუთის დახმარებით და if , elif , else  ოპერატორით დავუბეჭდოთ შედეგი.


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
options=input("choose an option:")

if options=="1":
     print("checking the balance")
elif options=="2":
    print("opening credit card")
elif options=="3":
     print("reseting your password")
elif options=="4":
         print("verifying your account")
elif options=="5":
    print("transfering money")
elif options=="6":
    print("exit")
else:
    print("invalid number")

print("To reset your password, you need to verify your identity.")


#პაროლი შესაცვლელად მომხმარებელს შემოვატანინოთ სახელი, გვარი და იდენტიფიკაციის მეთოდი.


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

username=input("please enter your name:")
id_number=input("please enter your identification number:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

print("Please choose an identification method:")
print("1. Answer Security Question")
print("2. Receive Verification Code via Email")
print("3.receive verification code via phone number:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

choice = input("Enter the number of your choice:")


if choice=="1":
    print("please answer security questions")
elif choice=="2":
    print("enter code from Email")
elif choice=="3":
    print("please enter one-time password:")
else:
    print("Invalid choice. Please select a valid identification method.")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
security=input("please enter one time password:")


#ცვლადში ვინახავ კოდს რომელიც მომხმარებელმა მიიღო მობილურ ნომერზე


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
otp=123321

###


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
print("congratulations! you have succesfuly verified your account")

password=input("please enter new password:")
password2=input("please repeat password:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()
if password==password2:
   print("Great news! Your password has been successfully reset!")
else:
    print("Passwords don't match")

#შევქმნათ ცვლადი სადაც შევინახავთ თანხის მიმღების სახელს და ჩვენი ბალანსი.

print("...welcome to the money transfer service...")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

name="nika keshelava"
your_balance=1000000


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

amount=int(input("please choose amount to send"))
receiver=input("please enter receivers name:")


 #გამოვიყენე პრინტ ფუნქცია რათა ხაზის გამოტოვებით გამოეტანა ტერმინალში
print()

#შევამოწმოთ თუ ტრანზაქცია წარმატებით განხორციელდა 
if name==receiver and your_balance>=amount:
  print("transaction went succesfully")
else:
   print("transaction failed")
