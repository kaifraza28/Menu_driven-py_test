
def Area_rectangle():
    print("You choose to calculate the area of the rectangle\n")
    lenght = int(input("Please Enter the lenght of the rectangle:\n"))
    breadth = int(input("Please Enter the breadth of the rectangle:\n"))
    return lenght*breadth
def Peri_rectangle():
    print("You choose to calculate the perimeter of reactangle\n")
    lenght = int(input("Please Enter the lenght of the rectangle:\n"))
    breadth = int(input("Please Enter the breadth of the rectangle:\n"))
    perimeter = 2*(lenght+breadth)
    return perimeter
def Area_Square():
    print("You choose to calculate the area of the Square\n")
    lenght = int(input("Please Enter the lenght of the square:\n"))
    return lenght*lenght

print("Menu\n 1.Area of Rectangle\n 2.Perimeter of Reactangle\n 3.Area of Square")
x = int(input("Please Enter your Choice Given:\n"))
if x==1:
    a = Area_rectangle()
    print("The area of rectangle is",a)
elif x==2:
    b= Peri_rectangle()
    print("The perimeter of rectangle is",b)
elif x==3:
    c = Area_Square()
    print("The area of square is",c)
else:
    print("Its the wrong input")

