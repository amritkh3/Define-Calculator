"""wap a program to make a calculator using(defining)a function
1.ask user to input the no and assign
 it to the variable ui1 and ui2 respectively for two number
2.ask user to input the operator.
3.define a function add where it will return where it will
 take two no and operator as parameter
4. now use if/else  condition 
   where if the operator is "add" it will  add two userinput
   else if operator is "sub" it will substract ui2 from ui1
   elif if operatoe is "mult" it will multiply ui1 and ui2
    and print the result 
"""
ui1=int(input("enter a number "))
ui2=int(input("enter another number "))
operator=input("enter action ")
def calculator(ui1,ui2,operator): 
  if   operator=="add":
        print(ui1+ui2)
  elif operator=="sub":
        print(ui1-ui2)
  elif operator=="mult":
        print(ui1*ui2)
  elif operator=="div":
        print(ui1/ui2) 

  elif operator=="squ":
        print(ui1*ui1,ui2*ui2)  
  else:
   print("")       
calculator(ui1,ui2,operator)



#second style
"""wap a program to make a calculator
1.ask user to input the no and assign
 it to the variable ui1 and ui2 respectively for two number
2.ask user to input the operator.
3.define a function add where it will return the addition of two number
4.def function similarly for substraction .multiplication and division 
5.now use if/else  condition 
   where if the operator is "add" it will call the add function
   else if operator is "sub" it will call sub fumction
   elif if operatoe is "mult" it will call multiplication function
and print the result.   
 """


# ui1=int(input("enter a number "))
# ui2=int(input("enter another number "))
# ui3=input("enter operation ")
# ui3=ui3.lower()

# def add(ui1,ui2):
#     print(ui1+ui2)
# def sub(ui1,ui2):
#     print(ui1-ui2)
# def mult(ui1,ui2):
#     print(ui1*ui2) 
# def div(ui1,ui2):
#     print(ui1/ui2)
# def squ(ui1,ui2):
#     print(ui1*ui1,ui2*ui2)

# if ui3=="add":
#     add(ui1,ui2)
# elif ui3=="sub":
#     sub(ui1,ui2)  
# elif ui3=="mult":
#     mult(ui1,ui2) 
# elif ui3=="div":
#     div(ui1,ui2) 
# elif ui3=="squ":
#     squ(ui1,ui2)    

# else:
#     print("sorry syntax error")   





                          


