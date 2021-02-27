input_number1=input("Enter 1st Number:\n")
operation=input("Enter the operation, you want to perform:\n")
input_number2=input("Enter 2nd Number:\n")

if int(input_number1) == 43 and int(input_number2) == 3 and operation=="*":
    print("555")
elif int(input_number1) == 56 and int(input_number2) == 9 and operation=="+":
    print("77")
elif int(input_number1) == 56 and int(input_number2) == 6 and operation=="/":
    print("4")
elif operation=="+":
    print(int(input_number1)-int(input_number2))
elif operation=="-":
    print(int(input_number1)-int(input_number2))
elif operation=="*":
    print(int(input_number1)*int(input_number2)) 
elif operation=="/":
    print(int(input_number1)/int(input_number2))   