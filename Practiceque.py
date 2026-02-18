#  1.	If  name = ''' Hi How are you?
# Starterd learning python.
# It's really interesting.''' Then what is the output of following code

# name = ''' Hi How are you? Starterd learning python. It's really interesting.'''
# print(name[:] )
# print(name[-10:-5])
# print(name[3:12])
# print(name[12:3])
# print(name[5,6])
# print(name[-4:-12])
# print(name[::2])
# print(name[::-2] )


# 2.	 L1 = [‘a’ , ‘b’, 20, 30, ‘t’, 100, 300, 400, ‘Happy’, ‘major’]
# a.	L1[:]
# b.	L1[::3]
# c.	L1[::-2]
# d.	How to extract  value “Happy” based on index and negative index
# e.	How to check type of data in list at 4th position
# f.	Extract values for 100, 300, 400 

# L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
# print(L1[:])
# print(L1[::3])
# print(L1[::-2])
# print(L1[8])
# print(L1[-2])

# 3.	If l2 =[1,2,3,5,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”] then what is the output of following
# •	L2[4]
# •	L2[1:5]
# •	L2[7]
# •	L2[7][2]
# •	L7[7][2:]
# •	L2[ : 3]
# •	L2[3:]

# l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'success'] 
# print(l2[4])
# print(l2[1:5])
# print(l2[7])
# print(l2[7][2])
# print(l2[7][2:])
# print(l2[ : 3])
# print(l2[3:])

# 4.From the above l2 value ‘b’ must be changed to ‘BEE’.
# l2[4][1]='BEE'
# print(l2)

# 5.From l2 “BEE” has to discard.
# l2[4].remove('BEE')
# print(l2)

# 6.In l2 add a dictionary at the end 
# {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}

# l2.append({'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']})
# print(l2)

# 7.From l2 extract insect information.
# print(l2[8]['insect'])

# # 8.Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
# d1 = {'a':10, 'b':20, 'c': 30} 
# l2.insert(2,d1)
# print(l2)

# 9.Based on new l2 created here extract the value 10 from l2 dictionary.
# print(l2)
# print(l2[10])

# 10.	If l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 
# ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, (200,300, “Hundreds”)] 
# then what is the output of following
# •	L2[4][2]
# •	L2[5][:]
# •	L2[2] [:]
# •	L2[1:5]
# •	L2[5]
# •	L2[5][3:-1]
# •	L2[-1]
# •	L2[-4, -3]
# •	L2[-4: -10]
# •	L2[7][2]
# •	L7[-7][[2:]
# •	L2[ :- 3]
# •	L2[-3:]

# l2 =[1,2,3,5, (90,40,50,10),'python', 400  ,['a', 'b', 'work hard'],
#      100 , 200, 'success', (200,300, 'Hundreads')] 
# print(	l2[4][2])
# print(	l2[5][:])
# print(l2[2])
# print(l2[1:5])
# print(l2[5])
# print(l2[5][3:-1])
# print(l2[-1])
# print(l2[-4: -3])
# print(l2[-4: -10])
# print(l2[7][2])
# print(l2[-7][2:])
# print(l2[ :- 3])
# print(l2[-3:])


# 11.	Ask user to enter the marks and define if the user got distinction, first class, second class, pass, Fails
# If marks are more than 80 output must be “You got distinction”
# For marks more than 60 output must be “You got First class”
# Marks more than 40 will display “You got second class”
# Marks more than or equal to 35 “PASS” Otherwise Fail

# marks=input("enter the marks ")
# if (not marks.isalpha and not marks.isalnum()) or marks.isdigit():
#     marks=int(marks)
#     if (marks >100 or marks<0):
#       print("enter the proper marks")
#     elif marks>80:
#       print("you got the distinction class")
#     elif marks>70 :
#       print(" you got the first class")
#     elif marks>50 :
#       print(" you got the second class")
#     elif marks>35 :
#      print("pass")
#     else:
#       print("fail")
# else:
#   print("not number")

# 12.Ask user to enter information about salary of the employee per year and rating received as A, B, C, D
# If salary upto 5 lpa then increament based on ratings are  A = 16% , B=12%, C= 10%, D=6%
# If salary upto 10 lpa then increament based on ratings are  A = 14% , B=10%, C= 8%, D=6%
# If salary upto 15 lpa then increament based on ratings are  A = 8% , B=6%, C= 4%, D = no increment
# If salary upto 23 lpa then increament based on ratings are  A = 7% , B=5%, C= 4%, D=no


# salary=input("enter your salary ")
# ratings=input("enter your ratings ")
# if salary.isdigit():
#     salary=int(salary)
#     if salary>0:
#         if salary>2300000:
#             if ratings=='A':
#                 print("hike by 7%",salary*0.07)
#             elif ratings=='B':
#                  print("hike by 5%",salary*0.05)
#             elif ratings=='C':
#                 print("hike by 4%",salary*0.04)
#             elif ratings=='D':
#                 print("no hike in salary")
#             else:
#                 print("invalid ratings ")
#         elif salary>1500000:
#             if ratings=='A':
#                 print("hike by 8%",salary*0.08)
#             elif ratings=='B':
#                  print("hike by 6%",salary*0.06)
#             elif ratings=='C':
#                 print("hike by 4%",salary*0.04)
#             elif ratings=='D':
#                 print("no hike in salary")
#             else:
#                 print("invalid ratings ")
#         elif salary>1000000:
#             if ratings=='A':
#                 print("hike by 14%",salary*0.14)
#             elif ratings=='B':
#                  print("hike by 10%",salary*0.1)
#             elif ratings=='C':
#                 print("hike by 8%",salary*0.08)
#             elif ratings=="D":
#                 print("hike by 6",salary*0.06)
#             else:
#                 print("invalid ratings ")
#         elif salary>500000:
#             if ratings=='A':
#                 print("hike by 16%",salary*0.16)
#             elif ratings=='B':
#                  print("hike by 12%",salary*0.12)
#             elif ratings=='C':
#                 print("hike by 12%",salary*0.1)
#             else:
#                 print("hike by 6",salary*0.06)
#     else:
#         print("salary cannot be 0 ")
# else:
#     print("invalid entry ")


# 13.	Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR 
# analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees.
#  DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)

# L1 = ["HR", 'Finance', 'Marketing', 'DS']
# print(L1)
# s=input("enter your subject :")
# fees=200000
# if s in L1:
#     a=input("havig Analytics in yes or no : ")
#     if a=="yes":
#         fees=fees+fees*0.1
#     h=input("you want hostel in yes or no  : ")
#     if h=="yes":
#         d=int(input("for how many years you want just enter digit: "))
#         fees=fees+d*200000
#     f=input("you want food in hostel in yes or no: ")
#     if f=="yes":
#         c=int(input("for how many monts you want food in digits : "))
#         fees=fees+c*2000
#     t=input("you want transport fascility in yes or no : ")
#     if t=="yes":
#         p=int(input("for how many semester you want: "))
#         fees=fees+p*13000
    
# else:
#     print("please select the valid subject  from above list ")
# print("your Total annoul fees   is :",fees)



# 14.Digitalize the book allotment process for school. Charges are mentioned here in the given table:
# d={ "books":{1:{"hindi":60,"marathi":60,"english":80,"science":90,"math":100},
#              2:{"hindi":60,"marathi":60,"english":80,"science":90,"math":100},
#              3:{"hindi":60,"marathi":60,"english":80,"science":90,"math":100},
#              4:{"hindi":60,"marathi":60,"english":80,"science":90,"math":100},
#             5:{"hindi":100,"marathi":100,"english":100,"science":120,"math":140},
#             6:{"hindi":100,"marathi":100,"english":100,"science":120,"math":140},
#             7:{"hindi":100,"marathi":100,"english":100,"science":120,"math":140},
#              8:{"hindi":100,"marathi":100,"english":100,"science":120,"math":140},
#              9:{"hindi":150,"marathi":150,"english":150,"science":200,"math":250},
#              10:{"hindi":150,"marathi":150,"english":150,"science":200,"math":250}},
#        "notebooks":{100:{"square":40,"4lines":30,"2lines":30,"single lines":60,"A4 notebook":100},
#                     200:{"square":70,"4lines":50,"2lines":50,"single lines":100,"A4 notebook":180}}}


# without function
# amount=0
# u=input("you want to purchase : ")
# while(u=="yes"):
#     s=input("what do you want books are notebook : ")
#     if s=="books":
#         print(d["books"].keys())
#         n=int(input("which standard books you want  : "))
#         if n in  d["books"].keys() :
#             print( d["books"][n].keys())
#             r=input("which book you want : ")
#             e=1
#             e=int(input("how many yoy want: "))
#             if r in d["books"][n].keys():
#                 amount=amount+ e*d["books"][n][r]
#     elif s=="notebooks":
#         print(d["notebooks"].keys())
#         n=int(input("how many pages of notebooks you want : "))
#         if n in d["notebooks"].keys():
#             print(d["notebooks"][n].keys())
#             e=1
#             r=input("enter ehich type of notebooks you want : ")
#             e=int(input("how many yoy want: "))
#             if r in d["notebooks"][n].keys() :
#                 amount=amount+ e*d["notebooks"][n][r]
        
#     u=input("you want to purchase : ")
# e= "-----------------------------------"
# f="|"
# print(e)
# print("{:^20}".format("Shree Stationary"))
# print(e)
# print("{:10}".format(f),end="")

# print( "Total Amount is : ",amount)
# print("thank you.....")
# dic={}
# i=0
# while i<5:
#     d={'a':i}
#     i=i+1
#     dic.update(d)
# print(dic)

# with function
# dic={}
# amount=0
# def Selection():
#     """for choosing books and pricing """
#     global amount
#     global u
#     while(u=="yes"):
#         s=input("what do you want books are notebook : ")
#         if s=="books":
#             print(d["books"].keys())
#             n=int(input("which standard books you want  : "))
#             if n in  d["books"].keys() :
#                 print( d["books"][n].keys())
#                 r=input("which book you want : ")
#                 e=1
#                 e=int(input("quantity : "))
#                 if r in d["books"][n].keys():
#                    amount=amount+ e*d["books"][n][r]
#                    dic.update({r:(e,amount)})
#         elif s=="notebooks":
#             print(d["notebooks"].keys())
#             n=int(input("how many pages of notebooks you want : "))
#             if n in d["notebooks"].keys():
#                print(d["notebooks"][n].keys())
#                e=1
#                r=input("enter ehich type of notebooks you want : ")
#                e=int(input("how many yoy want: "))
#                if r in d["notebooks"][n].keys() :
#                   amount=amount+ e*d["notebooks"][n][r]
#                   dic.update({r:(e,amount)})
        
#         u=input("you want to purchase more somthing : ")
#         print(dic)
        
# g= "--------------------------------------------------"
# f="|"

# def Billing():
#     global amount
#     """for placing the bill"""
#     print(g)
#     print("{:^40}".format("shree stationary"))
#     print(g)
#     print(f,end=" ")
#     print("{:10} {:>10} {:>10} ".format("product","Quantity","Price"),end="")
#     print(f)
#     for i in dic:
#         print(f,end=" ")
#         print("{:10} {:>10} {:>10}".format(i,dic[i][0],dic[i][1]),end="")
#         print(f)
        
#     print(g)
#     print("\n",f,end=" ")
#     print("{:8} {:>22}".format("total",str(amount)),end="")
#     print(f)

# def Buying():
#     """ customer  want to purchase or not """
#     s=input("you want to purchase : ")
#     if s=='yes':
#         Selection()
#         m=input("print the bill ")
#         if m=="yes":
#             Billing()
#     else:
#         print("ok thank you.....")

# u="yes"
# Buying()

# 17.	Create a=100 
# •	Convert a to string 
# •	Convert a to list    
# •	Convert a to tuple  
# •	Convert a to dict 
# •	Convert a to set 
# •	Convert to float 
# Observe the errors and note it down for all conversions. 
# a=100
# print(str(a))

# print(list(a))
# 'int' object is not iterable

# print(tuple(a))
# 'int' object is not iterable

# print(dict(a))
# 'int' object is not iterable

# print(set(a))
# 'int' object is not iterable

# print(float(a))



# 8.	Create city = “Pune” 
# •	Convert to int     
# •	Convert float 
# •	Convert list  
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	Obsert errors and note it down for all conversions 

# city="pune"
# print(int(city))
# invalid literal for int() with base 10: 'pune'

# print(float(city))
# could not convert string to float: 'pune'

# print(list(city))
# print(tuple(city))
# print(set(city))

# print(dict(city))
# dictionary update sequence element #0 has length 1; 2 is required

# 9.	Create a list as marks = [20,18,15,17,18] 
# •	Convert to int 
# •	Convert float 
# •	Convert list 
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	observe : errors and note it down for all conversions 
# marks = [20,18,15,17,18] 

# print(int(marks))
# int() argument must be a string, a bytes-like object or a real number, not 'list'

# print(float(marks))
#  float() argument must be a string or a real number, not 'list'

# print(list(marks))
# print(tuple(marks))
# print(set(marks))

# print(dict(marks))
# object is not iterable

# 10.	Create the empty list snames 
# •	 Add value 20 in the list using append 
# •	 Add value 30 in the list using extend 
# •	Add values in the list using append 
# •	Add value “WORK" in the list using extend 
# •	 Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3] 
# •	Add sname to combo using addition operator 
# •	Add combo to snames using append 
# •	Add combo to snames using extend. 

# snanes=[]
# snanes.append(20)
# snanes.extend('30')
# snanes.append(1)
# snanes.append(2)
# snanes.extend("WORK")
# combo=[1, 'a', 'b' ,2 , 3] 
# combo=combo+snanes
# snanes.append(combo)
# snanes.extend(combo)
# print(snanes)

# 11.	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 
# l1=[1,2]
# l3=[3,4,5,6,7,8,9]
# l3.insert(4,l1)
# print(l3)

# 12.	Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] if the data is in integer or float then multiply with 5.  
# •	From the collection delete the record for “Nisha” 
# •	Find the location of 20.50 
# l=[1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ]

# for i in l:
#     if type(i) in [int,float]:
#         i*5
#     elif type(i)==list:
#         for j in i:
#             if type(j) in [int,float]:
#                 j*5

# l.remove("Nisha")
# print(l.index(20.50))
# print(l)

# 13.	Create a comprehensive list for square upto 10 
# l=[x**2 for x in range(1,11)]
# print(l)

# 14.	Create the comprehensive list to find number divisible by 13 till 200
# l=[x for x in range(1,101) if x%13==0]
# print(l)

# 15.	Create the list which is divisible by 4 from 300 to 400  
# l=[x for x in range(300,401) if x%4==0]
# print(l)

# 16.	Create a comprehensive list to generate list up to x, y as a number. For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]
# Then generate a new list based on all combination of x and y.
# For example: if x = 1 and y =2  then x_list = [0] and y_list = [0,1]
# And output will be [[0,0],[0,1]]

# If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]

# x=int(input("enter the value of x : "))
# y=int(input("enter the value of y : "))
# x_list=[i for i in range(x)]
# y_list=[j for j in range(y)]
# l3=[]
# for i in x_list:
#     for j in y_list:
#         l3.append((i,j))
# print(l3)


# 21.	How to create empty set? 
# s=set()
# print(type(s))


# 22.	Create the set s1 and s2 and perform set operations like union, intersection, difference.
# s1={1,2,3,4,5}
# s2={1,3,5}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))

# 23.	Create l2 as a list and perform set operation on s1 with l1 
# s1={1,2,3,4,5}
# l1=[4,5,6]

# print(s1.difference(l1))
# print(s1.intersection(l1))
# print(s1.union(l1))

# 24.	Ask user to enter the name and DOB and generate the password based on first name 4 characters and  @ddmm. 
# For example name = SURESH and DOB = 05-05-1978 then password will be SURE@0505 

# name=input("enter your name: ")
# dob=input("enter dob in dd-mm-yyyy: fromat ")
# c=""
# for i in dob:
#     if i.isnumeric():
#         c=c+i

# pas=name[:4]+"@"+c[:4]
# print(pas)


# 25.	Ask user to enter the name and DOB and generate the password based on first name 4 characters and  
# last 4 digits of DOB or year @yyyy. For example name = SURESH and DOB = 05-05-1978 then password will be SURE@1978 
# name=input("enter your name: ")
# dob=input("enter dob in dd-mm-yyyy: fromat ")
# n=len(dob)
# pas=name[:4]+"@"+dob[n-4:n]
# print(pas)

# 26.	Create the format mentioned here.
# *
# * *
# * * *
# * * * *

# for i in range(1,5):
#     print("* "*i)


# 27.	Create the format as mentioned below:
# ****
# ***
# **
# *
# for i in range(4,0,-1):
#     print("* "*i)

# 28.	Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D
# Str_val = "ABCD"
# c=""
# for i in Str_val:
#     c=c+i
#     print(c)


# 29.	Create the format mentioned below:
# A
# BB
# CCC
# DDDD
# Str_val = "ABCD"
# c=''
# for i in Str_val:
#     c=c+i
#     print(i*len(c)) 

# 30.	Create the format mentioned below:
# 1
# 22
# 333
# 4444

# for i in range(1,5):
#     print(f"{i}"*i)

# 31.	Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA
# val="ABCD"
# n=len(val)
# c=""
# for i in range((n-1),-1,-1):
#     c=c+val[i]
#     print(c)


# 32.	Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU

# s=input("enter the string : ")
# n=len(s)
# c=""
# for i in range(n-1,-1,-1):
#     c=c+s[i]
#     print(c)

# 33.	Create a list of odd numbers from 1 to 10
# 1.	Using for loop
# 2.	Using comprehensive list

# for i in range(1,11):
#     if i%2!=0:
#         print(i)
# l=[x for x in range(1,11) if x%2!=0]

# 34.	Create even number list using for loop from 200 to 250
# l=[]
# for i in range(200,251):
#     if i%2==0:
#         l.append(i)
# print(l)

# 35.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element by 2 and display the answer
# List2 = [2,70,'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# for i in List2:
#     if type(i) in (int,str,float):
#         print(i*2)
#     elif type(i)==dict:
#         for j in i:
#             print(i[j]*2)
#     else:
#         for j in i:
#            print(j*2)

# 36.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element from list2 by 2 and store the answer in list3
# List2 = [2,70,'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# list3=[]
# for i in List2:
#     if type(i) in (int,str,float):
#         list3.append(i*2)
        
#     elif type(i)==dict:
#         for j in i:
#             list3.append(i[j]*2)
#     else:
#         for j in i:
#            list3.append(j*2)
# print(list3)


# 39.	Create a function to accept mobile number. Mobile number should contain 10 digits. 
# No Special character, alphabets and space. 
# n=input("enter the number: ")
# def ValidateNumber(n):
#     if(not n.isalpha and not n.isalnum) or n.isdigit() and  len(n)==10: 
#         return n
#     else:
#         return "invalid number"
# ValidateNumber(n)

# 40.	Create a function to generate auto-password based on specific person details. Ask user to enter name, DOB.
# And password must be First name 4 characters and year of birth.
# def PasswordCreater(name,dob):
#     n=len(dob)
#     return(name[:4]+dob[n-4:n])
# n=input("enter your name: ")
# m=input("enter your dob in DD-YY-YYYY fromat: ")
# PasswordCreater(n,m)

# 41.	Create a empty dictionary and ask user to enter values as name, DOB, mobile number 
# add all the details in dictionary with customer number as 1 for first time. If user try to enter another value,
#  then number should increase as 2 with new details and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}

# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}
# dic={}
# while True:
#     name = input("Enter name: ")
#     dob = input("Enter DOB (dd-mm-yyyy): ")
#     mobile = input("Enter mobile number: ")

#     cust_no = len(dic) + 1   

#     dic[cust_no] = {
#             "name": name,
#             "DOB": dob,
#             "mobile": mobile
#         }
#     print(dic)
#     more = input("\nAdd another customer? (yes/no): ").lower()
#     if more != "yes":
#         break

# 42.	Based on the above example create the dictionary and save the same in a cust_info.txt or cust_info.log
# dic={}
# while True:
#     name = input("Enter name: ")
#     dob = input("Enter DOB (dd-mm-yyyy): ")
#     mobile = input("Enter mobile number: ")

#     cust_no = len(dic) + 1   

#     dic[cust_no] = {
#             "name": name,
#             "DOB": dob,
#             "mobile": mobile
#         }
#     print(dic)
#     more = input("\nAdd another customer? (yes/no): ").lower()
#     if more != "yes":
#         break
# f=open("cust_info.txt","x")
# f.write(str(dic))

# 43.	Based on the above example read the file cust_info.txt . check if dictionary any information is available in the file. 
# If there is information then read the dictionary store into one variable and then append new information of customer if added.


# 45.	Dict1= {“Key”: {“subkey”:20} ,  “k2”:{“sub2” : 5}, “k3” : {“sub4” :16},  “k4” : {“sub4” : 6}}
# Sort elements based on values
# Output must be {,  “k2”:{“sub2” : 5}, “k4” : {“sub4” : 6},  “k3” : {“sub4” : 16}, “Key”:{“subkey”:20}}
# Dict1= {'Key': {'subkey':20} ,  'k2':{'sub2' : 5}, 'k3' : {'sub4' :16},  'k4' : {'sub4' : 6}}
# keys = list(Dict1.keys())
# for i in range(len(keys)):
#     for j in range(i+1, len(keys)):

#         a = list(Dict1[keys[i]].values())[0]
#         b = list(Dict1[keys[j]].values())[0]

#         if a > b:
#             keys[i], keys[j] = keys[j], keys[i]

# sorted_dict = {}
# for k in keys:
#     sorted_dict[k] = Dict1[k]

# print(sorted_dict)

# 46.	Create a function to calculate age till now.
# from datetime import date
# from datetime import datetime

# def AgeCalculator(n):
#     s=datetime.now().date()
#     return ("The Current Age is : ",s.year-n.year)
# AgeCalculator(date(2003,12,17))

         
# 47.	Create a function to check age eligibility for given customer 
# based on DOB. Function will take two input DOB and ELIGIBILITY age.


# 48.	Create a function to check if string is palindrome or not ? For example, if
# input is NITIN then reverse of the string is same then it is palindrome. If input is 
# ANIL then reverse is LINA which is not same then it is not palindrome.  

# def Palindrome(n):
#     s=""
#     m=len(n)
#     for i in range(m-1,-1,-1):
#         s=s+n[i]
#     if s==n:
#         return (n, " is palindrome")
#     else:
#         return "not palindrome"
# s=input("Enter the string ")
# Palindrome(s)

# 49.	Create a function to generate a Fibonacci Series. 0 1 1 2 3 5 8 13 21 34 …..  upto 100
# def Fibonacci(n):
#     a=0
#     b=1
#     print(a,b)
#     for i in range(2,n+1):
#         c=a+b
#         print(c)
#         a,b=b,c
# s=int(input("enter numbers"))
# Fibonacci(s)

# 50.	Write a code to generate factorial of the number  For example: factorial of 5 = 5! = 5*4*3*2*1
# def Factorial(n):
#     fact=1
#     for i in range(n,0,-1):
#         fact=fact*i
#     return fact
# m=int(input("enter the number: "))
# Factorial(m)

# 51.	Write a program to find largest number in the list.
# l1=[1,2,3,4,5]
# print(max(l1))

# 52.	Write a program to check frequency of each element in the list.
# l1=[1,2,2,2,3,3,4,5,5]
# dic={}
# for i in l1:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)

# 53.	There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9] 
# then write a program to find common elements in the list.
# l1 =[ 1,2,3,4,5]
# l2 =[3,2,8,7,9] 
# print(set(l1).intersection(l2))

