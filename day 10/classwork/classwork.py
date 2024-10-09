#ჩატბოტი
#ბანკის პროექტი
#



   # 1) შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდი
    # ნარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 , და შემოიტანს მოქმედებას მაგალითად 
    # დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12


num1=int(input("enter number:"))
num2=int(input("enter number 2:"))
operation=(input("enter operation( +,-,/,*: "))



if operation=="+":
    result=num1+num2
    print(result)

elif operation=="-":
    result=num1-num2
    print(result)

elif operation=="/":
    result=num1/num2
    print(result)

elif operation=="*":
    result=num1*num2
    print(result)

else:
    print("error")