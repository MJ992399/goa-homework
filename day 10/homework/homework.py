
    # 1) შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდი
    # ნარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 , და შემოიტანს მოქმედებას მაგალითად 
    # დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12



first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
    print(result)
elif operation == "-":
    result = first_number - second_number
    print(result)
elif operation == "*":
    result = first_number * second_number
    print(result)
else:
    result=first_number / second_number
    print("result")
   