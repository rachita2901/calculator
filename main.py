def add(num1, num2): 
    return num1 + num2 
   
def subtract(num1, num2): 
    return num1 - num2 

def multiply(num1, num2): 
    return num1 * num2 

def divide(num1, num2): 
    return num1 / num2 

def mod (num1,num2):
	return(num1%num2)
  
print("Please select operation")
print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")
print("5. Mod")

  
   
select = input("Select operations form 1, 2, 3, 4 ,5:")
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == '2': 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == '3': 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == '4': 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2))
elif select =='5':
    print(number_1, "%", number_2, "=",
          mod(number_1, number_2))

else: 
    print("Invalid input") 