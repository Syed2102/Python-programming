# colours = ["red", "yellow","green","blue"]
# for colour in colours:
#     print(colour) 
#     for i in colour:
#         print(i)
# for i in range(1,2001):
#     print(i)
# for i in range(1,12,3):
#     print(i)

# ====================================================================================

# hour=int(input("Enter the number(0-23):"))
# if hour >= 5 and hour < 12:
#     print("good morning")
# elif hour >= 12 and hour < 17:
#     print("good afternoon")
# elif hour >=17 and hour < 21:
#     print("good evening")
# else:
#     print("ggod night!")
# name='alfia'
# for i in name:
#     print(i)
# i=0
# while(i<=4):
#     print(i)
#     i=i+1

# print("done with the loop")
# i=int(input("enter the number"))
# while(i<=50):
#     i=int(input("enter the number:"))
#     print(i)

# print("done with the loop")
# count=5
# while(count>0):
#     print(count)
#     count=count-1
# else:
#     print("i am inside else")
# break and continue
# for i in range(12):
#     if(i==5):
#         break
#     print("5 x",i+1,"=",5 * (i+1))
# print("loop chodne wala hai")
# for i in range(12):
#     if(i==5):
#         print("skip the iteration")
#         continue
#     print("5 x",i+1,"=",5 * (i+1))
# print("hum bhi coder bn rhe haI")

# =========================================================================================

# i=0
# while True:
#     print(i)
#     i=i+1
#     if(i%100==0):
#         break
# def calculation_gmean(a,b):
#     mean =(a*b)/(a+b)
#     print(mean)
# a=8
# b=9
# calculation_gmean(a,b)
# c=7
# d=9
# calculation_gmean(c,d)
# print("geomatric mean is done")
# def calculation_gmean(a,b):
#     mean =(a*b)/(a+b)
#     print(mean)
# def isgreater(a,b):
#     if(a>b):
#         print("first number is greater")
#     else:
#         print("second number is greater or equal")
# a=8
# b=9
# isgreater(a,b)
# calculation_gmean(a,b)
# c=7
# d=9
# isgreater(c,d)
# calculation_gmean(c,d)
# print("geomatric mean is fuck")
# default argument
# def average(a=12,b=100):
#     print("the average of functin",(a+b)/2)
# average(13)
# def average(*number):
#     print(type(number))
#     sum=0
#     for i in number:
#         sum=sum+i
#     print("average is",sum/len(number))
# average(5,10)
# lists
# mark =[1,23,4,"faiz",True]
# print(mark)
# print(mark[-3])
# print(mark[5-3])
# print(mark[2])
# mark =[1,23,4,"faiz",True]
# print(mark)
# print(mark[-3])
# print(mark[5-3])
# print(mark[2])
# if 7 in mark:
#     print("yes")
# else:
#     print("no")

# ==========================================================================================
# kBC
# ==========================================================================================

# questions = [["what is the capital of india?","delhi",1000],
#              ["which is known as red planet","mars",2000],
#              ["who is the father of nation in india?","mahatma gandhi",5000],
#              ["which is the ocean in the world","pacific",100000],
#              ["which programming language is 'mother of AI'","lisp",20000]]
# amount=0
# print("welcome to kbc quiz")
# for i in questions:
#     print("question for $",i[2])
#     print(i[0])
#     answer=input("your answer:")
#     if answer.strip().lower()==i[1].lower():
#         print("answer is the correct:")
#         amount=i[2]
#     else:
#         print("answer is wrong")
#         print("correct answer:",i[1])
#         break
# print("game over ")
# print("you are taking home",amount)
# KON BANEGA COREPATI
# questions = [["which langauge was used to create fb?","python","frech","javascript","php","none",4],
#  ["which langauge was used to create fb?","python","frech","javascript","php","none",4],
#  ["which langauge was used to create fb?","python","frech","javascript","php","none",4],
# ["which langauge was used to create fb?","python","frech","javascript","php","none",4],
#  ["which langauge was used to create fb?","python","frech","javascript","php","none",4],
#  ["which langauge was used to create fb?","python","frech","javascript","php","none",4]
# ]
# level = [1oo,]
# without f-stringno
# letter="hey my name{} and i am from {}"
# country="india"
# name="faiz"
# print(letter.format(name,country))
# using f-string
# name="faiz"
# country="russia"
# print(f"hey my name is {name} and i am from {country}")
# price=500
# a=100
# print(f"wheat={price} and bajra={a}")
# doc string
# def square(n):
#     '''take the number of n,returns square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)
# #recusion of function
# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#      return n*factorial(n-1)
    
# print(factorial(3))
# fabonacci 
# def fobanacci(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fobanacci(n-1)+fobanacci(n-2)
# print(fobanacci(5))
# set 
# set1={"tokye","berlin","soul","jamshedpur"}
# set2={"delhi","tokye","jakarta","soul"}
# print(set1.union(set2))
# set3=set1.intersection(set2)
# print(set3)
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.isdisjoint(set2))
# print(set1.issuperset(set2))
# print(set1.update(set2))
# del set1
# print("its deleted sucessfull")
# dictionaries
# dic = {344:"faiz"}
# print(dic[344])
# dic = {344:"faiz",234:"topper",111:"reach advantage"}
# print(dic[344])
# print(dic.keys())
# for loop with else:
# for i in range(10):
#     print(i)
# else:
#     print("sorry no i")
# for i in range(10):
#     print(i)
#     if i == 9:
#         break
# else:
#     print("sorry no i")
# exception handling:
# a = input("enter the number:")
# print(f"multiplication table of {a} is :")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i}={int(a)*i}")
# except Exception as e:
#     print(e)
# print("same imp line of code")
# print("end of program")
# try:
#     a=int(input("enter the number:"))
# except ZeroDivisionError:
#     print("cannot divide successful")
# else:
#     print("divison successful")
# finally:
#     print("execution completed")
# try:
#     a = int(input("enter the number:"))
#     b = int(input("enter the number:"))
#     print("two number enter sucessfull")
#     result = a/b
#     print("result")
# except ZeroDivisionError:
#     print("cannot divide by zero!")
# bank withdrawal:- custom exception
# Encoding
# import random
# import string
# print("Encoding")
# word = input("Enter the word:")
# if len(word)<3:
#     print("dont change the word")
# else:
#     new_word = word[1:] + word [0]
#     print(new_word)
#     random_chars = ''.join(random.choices(string.ascii_letters, k=3))
#     encoded_word = random_chars + new_word + random_chars
# print(encoded_word)
# import pandas as pd
# print(pd.__version__)
# st = input("Enter the number:")
# words = st.split(" ")
# coding = input(" 1 for encoding and 0 for decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if (coding):
#     nword=[]
#     for word in words:
#         if (len(word)>=3):
#             r1="lauda"
#             r2="laura"
#             stnew = r1+word[1:]+word[0]+r2
#         else:
#             nword.append(word[::-1])
#     print(" ".join(word))
# else:
#     nword = []
#     for word in words:
#         if (len(word)>=3):
#             stnew = word [5:-5]
#             stnew = stnew [-1]+stnew[:-1]
#             nword.append(stnew)
#         else:
#             nword.append(word[::-1])
#             print(" ".join(nword))

# ==============================================================================================
# GLOBAL VS LOCAL VARIABLE
# ==============================================================================================

# x=10 #global variable
# print(x)
# def my_function():
#     x=100
#     print(f"the local x is {x}")
#     print("hello faiz")
# print(f"the global x is {x}")
# my_function()
# x=100
# print(f"the global x is {x}")

# print(x)
# def my_function():
#     global x
#     print(x)
#     x=1000
#     y=100
#     print(y)
# my_function()
# print(x)
# print(f"the global x is {x}")
# print(f"the local y is {y}") # this will show error in this code

# ==============================================================================================
# armstrong numder
# =============================================================================================

# n=int(input("Enter the number:"))
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if n==sum:
#     print(n,"is an armstrong number")
# else:
#     print(n,"is not armstrong number")

# ==============================================================================================
# funtion(lambda function,map,filter)
# ==============================================================================================

# def function_new(x):
#     return x*x
# double=lambda x:x*2
# print(double(5))
# l=[1,2,3,4,5]
# newl=list(map(lambda x:x*2,l))
# print((newl))
# l=[1234,12346,75767,647383.8757838937748]
# newl=list(filter(lambda x:x>12345,l))
# print(newl)
# reduceFunction
# from functools import reduce
# l=[1,2,3,4,5,6]
# newl=reduce(lambda x,y:x+y,l)
# print(newl)

# ===================================================================================
# "is" vs "==" operator in python
# ===================================================================================

# a=[1,2,3]
# b=[1,2,3]
# print(a is b) # exact location of memory store value(it give true value if object is immutable)
# print(a==b) # only value 

# ====================================================================================
# sum and average of marks
# ====================================================================================

# total=0
# count=0
# while True:
#     num=int(input("Enter the number:"))
#     if num==0:
#         break
#     total=total+num
#     count=count+1
# average=total/count
# print("Sum",total)
# print("Average",average)

# =====================================================================================
# ROck,Paper,Scissor
# =====================================================================================

# import random
# items=["rock","paper","scissor"]
# computer=random.choice(items)
# user=input("Rock Paper Scissor:").lower()
# print("Computer Choices",computer)
# if user=="rock" and computer=="scissor":
#     print("User winzz!!")
# elif user==computer:
#     print("Match draws!!")
# elif user=="paper" and computer=="rock":
#     print("User Winzz!!")
# elif user=="scissor" and computer=="paper":
#     print("User Winzz!!")
# else:
#     print("Computer winzzz!!")

# ==========================================================================================
# Object Oriented Programmimng(OOPs)
# ==========================================================================================

# class person:
#     name="faiz"
#     occupation="Information technology"
#     networth=1000000
# a=person()
# a.name="harry"
# print(a.name,a.occupation)

# class person:
#     name="faiz"
#     occupation="Information technology"
#     networth=1000000
#     def info(self):
#         print(f"{self.name} is an {self.occupation}")

# a=person()
# a.name="harry"
# a.occupation="Information Technology"
# a.info()

# ===============================================
# Decorator 
# ===============================================

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("good morning")
#         fx(*args,**kwargs)
#         print("Thnks for using this function")
#     return mfx
# @greet
# def hello():
#     print("hello world")
# def add(a,b):
#     print(a+b)
# hello()
# greet(add)(12,13)

# =============================================
# Getter And Setter 
# ============================================

# class myclass:
#     def __init__(self,value):
#         self._value=value
#     def show(self):
#         print(f"value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10*self._value
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10
# obj=myclass(10)
# obj.ten_value=67
# print(obj.ten_value)
# obj.show()

# ==========================================================================
# LIBRARY MANAGEMENT
# =========================================================================

# class library:
#     def __init__(self):
#         self.books = []
#         self.number_of_books = 0
#     def add_book(self,book):
#         self.books.append(book)
#         self.number_of_books += 1
#     def show_books(self):
#         print("book in the library :")
#         for book in self.books:
#             print(book)
#     def get_number_of_books(self):
#         return self.number_of_books

# #Create a library object

# library = library()

# # Add books

# library.add_book("python programming")
# library.add_book("data science")
# library.add_book("machine learning")

# #Print all books

# library.show_books()

# # Get a number of books

# print("number of books", library.get_number_of_books())
#                              -------------xxx-----------------