# #შექმენით ბანკის პროექტი, გამოიყენეთ უკვე ნასწავლი მასალა და ინტერნეტის დახმარებით მოიძიეთ ახალი ინფორმაცია

# #დაბეჭდე პირველი მესიჯი რომელსაც კლიენტი ნახავს როდესაც მობაილ ბანკში შევა.


print("------Welcome to Mobile Bank!------")

 #დაბეჭდე ვარიანტები ნუმერაციით რათა კლიენტმა აირჩიოს სასურველი.


print("for registration press 1:")
print("to change password press 2:")
print("to check balance press 3: ")
print("for loan press 4:")
print("credit card 5:")

# #ინფუთ ფუნქციით მომხმარებელს შეაყვანინე  სასურველი ვარიანტი
operation=(input("choose an operation:"))

# #if, elif da else ოპერატორით შეამოწმე რომელი ოპერაცია აირჩია კლიენტმა.
if operation == "1":
     print("registration")
elif operation=="2":
     print("change password")
elif operation=="3":
     print("check balance")
elif operation=="4":
   print("loan")
elif operation==5:
     print("credit card")
else:
   print("invalid choise,please enter a valid number")


# print("welcome to the mobile banking registration")

# #რეგისტრაციისთვის კლიენტს შემოვატანინოთ პირადი მონაცემები

name=input("please enter your full name:")
phone_number=input("please enter your phone number:")
date_of_birth=input("please enter your date of birth:")


print("Congratulations! You have successfully registered for Mobile Banking")

# #დავპრინტოთ რამდენიმე ვარიანტი რათა კლიენტმა აირჩიოს სასურველი

print("Your account requires verification to proceed. Please complete the verification process to gain access.")


print("please select a verification method")

print("to select passport number press (1):") 
print("to select identification number press  (2):")
print("to select social security number press (3):")
# #input-ის დახმარებით მომხმარებელს შემოვატანინოთ სასურველი ვარიანტი032

verification_method = input("Enter your choice (1, 2, or 3): ")

if verification_method=="1":
         print("please enter passport number:")
elif verification_method=="2":
     print("please enter id number:")
elif verification_method=="3":
     print("please enter ssn number:")
else:
    
     print("selected number doesn't exist, please try again")

print("Your account has been successfully verified.")


#შევქმნათ ცვლადი და მივანიჭოთ მნიშვნელობა მომხმარებლის სახელი და პაროლი
user_name = "mariami"
password = 123321


input_user = input("Please enter your username: ")
input_password = input("Please enter your password: ")

# #შეამოწმე ემთხვევა თუ არა დეტალები ერთმანეთს

if input_user == user_name and int(input_password) == password:
    print("Welcome to your mobile bank")
else:
     print("User cannot be found")

#ინფუთით მომხმარებელს ვკითხოთ სურს თუ არა სცადოს ხელახლა
response=input("would you like to try again? yes/no :")

#შევქმნათ ცვლადი და შევინახოთ მომხმარებლის სახელი და პაროლი
user_name = "mariami"
password = 123321


input_user = input("Please enter your username: ")
input_password = input("Please enter your password: ")

if input_user==user_name:
     print("correct user")
elif input_password==password:
     print("correct password")
else:
     print("user can not be found,please contac costumer service")

#ჩატბოტში დავპრინტოთ ველქამ მესიჯი და ვარიანტები
print(".....Welcome to the Mobile Bank Chatbot.....!")
print("How can I assist you today? choose an options: ")
print("1. Balance")
print("2. Credit Card")
print("3. Password Reset")
print("4. Verification")
print("5. Transfer")
print("6. Exit")

#მომხმარებელს შემოვატანინოთ სასურველი ციფრი ინფუთის დახმარებით და if , elif , else  ოპერატორით დავუბეჭდოთ შედეგი.

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


#პაროლის შესაცვლელად მომხმარებელს შემოვატანინოთ სახელი, გვარი და იდენტიფიკაციის მეთოდი.


username=input("please enter your name:")
id_number=input("please enter your identification number:")



print("Please choose an identification method:")
print("1. Answer Security Question")
print("2. Receive Verification Code via Email")
print("3.receive verification code via phone number:")



choice = input("Enter the number of your choice:")

if choice=="1":
    print("please answer security questions")
elif choice=="2":
    print("enter code from Email")
elif choice=="3":
    print("please enter one-time password:")
else:
    print("Invalid choice. Please select a valid identification method.")

security=input("please enter one time password:")

#ცვლადში ვინახავ კოდს რომელიც მომხმარებელმა მიიღო მობილურ ნომერზე

otp=123321

###

print("congratulations! you have succesfuly verified your account")

password=input("please enter new password:")
password2=input("please repeat password:")

if password==password2:
   print("Great news! Your password has been successfully reset!")
else:
    print("Passwords don't match")

#შევქმნათ ცვლადი სადაც შევინახავთ თანხის მიმღების სახელს და ჩვენი ბალანსი.

print("...welcome to the money transfer service...")

name="nika keshelava"
your_balance=1000000

amount=int(input("please choose amount to send"))
receiver=input("please enter receivers name:")

#შევამოწმოთ თუ ტრანზაქცია წარმატებით განხორციელდა 
if name==receiver and your_balance>=amount:
  print("transaction went succesfully")
else:
   print("transaction failed")

