# python_assignment_1

# Bhavyasree N - 321810304042

###  1.Simple Calculator
num1=int(input("Enter first number :")) # input first number
num2=int(input("Enter second number :")) # input second number
print("Sum=",num1+num2) #Addition
print("Difference=",num1-num2) #Subtraction
print("Division=",num1/num2) #Division
print("Product=",num1*num2) #Multiplication
print("Modulus=",num1%num2) #Modulus
print("Exponent=",num1**num2) #Exponentiation
print("Floor Division=",num1//num2) #Floor Division


###  2.Simple Interest
P=100  #principal amount
R=2 # Rate of Interest
T=3 #Time period
SI=(P*T*R)/100 # Simple interest
print("Simple interest is :",SI)


###  3.Area of Circle
PI=3.14
R=float(input("Enter the Radius of the circle")) #Radius of the Circle
Area=PI*R*R #Area of Circle
print("%.2f" %Area)


###  6.Area of Rectangle
L=float(input("Enter the length :")) # length of the rectangle
B=float(input("Enter the breadth :")) # breadth of the rectangle
Area=L*B
print("Area of the Rectangle is %0.2f :" %Area)


###  5.Temperature in Celsius to Fahrenheit
Celsius=float(input("Enter the Temperature"))
Fahrenheit=(Celsius*9/5)+32
print("%.2f of Celsius is : %.2f of Fahrenheit" %(Celsius,Fahrenheit))


###  4.Area of Triangle
# three sides of a triangle be as : a, b, and c
a=float(input('Enter first side :'))
b=float(input('Enter second side :'))
c=float(input('Enter third side :'))
# calculate Semi-Perimeter
s=(a+b+c)/2
# calculate Area
Area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The Area of Triangle is %.2f' %Area)


###  7.Perimeter of a Square
A=int(input("Enter length of Square :"))  #side of a square
Perimeter=4*A  #Perimeter of a Square
print('Perimeter of Square is %d' %Perimeter)


###  8.Circumference of a Circle
PI=3.14
R=float(input("Enter Radius of circle :"))  # Radius of a Circle
Circumference=2*PI*R
print("Circumference of a Circle %.2f" %Circumference)


###  9.Swapping of Two Numbers
A=input("Enter the first number :")  #input the values
B=input("Enter the second number :")
print("Value of A before Swapping :", A)  #before Swapping the value
print("Value of B before Swapping :", B)
temp = A #temporary variable for Swapping
A = B
B = temp
print("Value of A after Swapping :", A)  #after Swapping the value
print("Value of B after Swapping :", B)


                                      
                                 #  python_assignment_1

                                 #  Nanjundareddy Bhavyasree
                                 # 2nd year
                                 # Sec...D
                                 # Roll. no...321810304042
_____________________________________                    