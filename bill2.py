print("amazon online shopping")
x=input("enter your name")
y=int(input("enter your phone number"))
z=input("enter your address")
print("choose a category")
print("1.kids wear")
print("2.men's wear")
print("3.furniture")
print("4.sports utilities")
print("5.ornaments")
a=int(input("enter your choice"))
if a==1:
    print("1.shirt")
    ss="shirt"
    print("2.t-shirt")
    print("3.pant")
    print("4.shorts")
    b=int(input("enter your choice"))
    if b==1:
        n=int(input("enter the quantity"))
        k=input("enter the size")
        if  k=='s':
              p=n*280
              print("your total adds to",p)
              print("do you want to continue")
              print("1.yes")
              print("2.no")
              l=int(input("enter your choice"))
              if l==2:
                  print("you are now being directed to the shopping cart")
                  print("do you wish to review your products")
                  print("1.yes")
                  print("2.no")
                  r=int(input("enter your choice"))
                  if r==1:
                    if b==1:
                      print("items choosen:")
                      print(ss)
                      print("individual cost:280")
                      print("total:",p)
                      e=input("do you wish to procced for transaction")
                      if e=="yes":
                       print("directing to payment")
                       print("net total",p)
                       int(input("enter your card details"))
                       int(input("enter your pin"))
                       print("payment successful")
                       print("your product will reach you on 22.1.24")
                       print('\033[1m'+ 'for furthur details contact us on utthr@gmail.com')
                       print("thanking you for shopping with us")
                       import turtle  
                       tut = turtle.Screen() 
                       tut.bgcolor("White") 
                       pen = turtle.Turtle() 
                       pen.speed(10) 
                       pen.color("Green") 
                       pen.width(10) 
                       tut = turtle.Screen() 
                       for x in range(180): 
                          pen.forward(1) 
                          pen.right(1) 
                       pen.right(90) 
                       pen.forward(50) 
                       pen.right(90)
                       pen.forward(130)
                       pen.right(90) 
                       pen.forward(50) 
                       pen.left(90) 
                       for x in range(180): 
                         pen.backward(1) 
                         pen.right(1) 
  
                       turtle.done() 

if b==2:
        n=int(input("enter the quantity"))
if b==3:
        n=int(input("enter the quantity"))
if b==4:
        n=int(input("enter the quantity"))
if a==2:
    print("men's wear")
    print("1.shirt")
    print("2.t-shirt")
    print("3.pant")
    print("4.shorts")
    print("5.trek wears")
    print("6.sports wear")
    print("7.winter clothing")
    print("8.formals")
    print("9.casuals")
    int(input("enter your choice"))
    
if a==3:
    print("furniture")
if a==4:
    print("sports utilities")
if a==5:
    print("ornaments")
   
