# Write a list comprehension to generate squares of numbers from 1 to 10
# l1=[ n for n in range(1,11)]
# print(l1)

# Create a list of even numbers between 1 and 50 using list comprehension.
# l1=[n for n in range(1,51) if n%2==0]
# print(l1)

 #  Convert all strings in a list to uppercase using list comprehension. 
# l1=["piyusj","juber","loeksh","kamil"]
# l2=[ s.upper() for s in l1  ]
# print(l2)

# Given a list of integers, create a new list that contains only the positive numbers. 
# l1=[-1,-2,-3,2,5,6,8]
# l2=[s for s in l1 if s>0]
# print(l2)

# Create a list of tuples (num, num^2) for numbers 1 to 5.
# l1=[ n for n in range(1,6)]
# l2=[(n,pow(n,2)) for n in l1]
# print(l2)

# Extract all vowels from a given string using list comprehension. 
# s="piyush"
# l1=[n for n in s  if n.lower() in 'aeiou' ]
# print(l1)

#  Flatten a 2D list using list comprehension.
# l1=[[1,2,3],[4,5,6]]
# l2=[n for s in l1 for n in s]
# print(l2)

#  Replace all negative numbers in a list with 0 using list comprehension.
# l1=[-1,-2,-3,2,5,6,8]
# l2=[s if s>0  else 0 for s in l1 ]
# print(l2)

# Given a list of words, create a list of lengths of each word
# l1=["piyush","juber","loeksh","kamil"]
# l2=[ len(s) for s in l1  ]
# print(l2)

#  Filter out words that start with the letter 'A' or 'a'. 
# l1=["piyush","aishwarya"]
# l2=[s for s in l1 if s.startswith('a')or s.startswith('A')]
# print(l2)

# From a list of numbers, generate a list of “even” or “odd” strings using list comprehension.
# l1=[n for n in range(1,11)]
# l2=['even' if n%2==0 else'odd' for n in l1]
# print(l2)

# Create a list of numbers divisible by both 3 and 5 in range 1–100.
# l1=[n for n in range(1,101) if n%3==0 and n%5==0] 
# print(l1)

#  Write a nested list comprehension to generate a multiplication table for 1–5. 
# l1=[n*m for m in range(1,6) for n in range(1,11) ]
# print(l1)

#  Convert a dictionary’s keys into a list using list comprehension.
# dict={
#     1:"piyush",
#     2:"juber",
#     3:"kamil",
#     4:"lokesh"
# }

# l1=[n for n in dict.keys() ]
# print(l1)

#  Extract numeric digits from a string using list comprehension.
# s="piyus123345"
# l=[n for n in s if n.isdigit()]
# print(l)

# Use list comprehension to remove all spaces from a string.
# s="  yo  uo "
# h=''.join([n for n in s if n.replace(" ","")])
# print(h)

#. Create a list of characters that appear more than once in a string.
# s="yooo"
# l1=[]
# n=len(s)
# for i in range(n):
#     count=0
#     for j in range(n):
#         if s[i]==s[j]:
#             count+=1
#     if count>1:
#         l1.append(s[i])
# print(list(set(l1)))

# 18. From a list of sentences, generate a list of all words (split using list 
# comprehension).
# l1=["hi how are you"]
# l2=[x for s in l1 for x in s.split()]
# print(l2)


# 19. Create a list of unique elements from a list using list comprehension + 
# condition. 
# l1=[1,2,2,3,3,4,4,5,5]
# l2=[l1[i] for i in range(len(l1)) if l1[i] not in l1[:i]]
# print(l2)

 
# 20. Generate all pairs (x, y) where x is from list A and y is from list B 
# (cartesian product)
# l1=[1,2,3]
# l2=[4,5,6]
# l=[(x,y) for x in l1  for y in l2]
# print(l)

# lambda Function
# 1. Write a lambda to add two numbers.
# add=lambda x,y:x+y
# print(add(6,7))

# 2. Create a lambda to check if a number is even. 
# check=lambda x:  "even" if x%2==0  else "odd"
# print(check(2))

# 3. Write a lambda to get the last character of a string. 
# last=lambda s: s[len(s)-1]
# print(last("helowhygtq"))

# 4. Use lambda with map() to square every number in a list. 
# l1=[1,2,3]
# sqe=map((lambda x:x**2),l1)
# print(list(sqe))

# 5. Use lambda with filter() to get only odd numbers from a list.
# l1=[x for x in range(11)]
# odd=filter((lambda a: a if a%2!=0 else "" ),l1)
# print(list(odd))

# 6. Use sorted() + lambda to sort a list of tuples by second value. 
# l1=[(1,2),(2,3),(1,1),(4,7),(5,4)]
# s=sorted(l1,key=lambda a:a[1] )
# print(s)


# 7. Create a lambda to check if a string is a palindrome. 
# pal=lambda s: "palindrome" if s==s[::-1] else "not paindrome"
# print(pal("madam"))

#8. Use lambda to find maximum of three numbers. 
# maxim=lambda x: max(x)
# print(maxim("153"))

# 9. Write a lambda to reverse a string. 

# rever=lambda s: s[::-1]
# print(rever("yooo"))

# 10. Use lambda with map() to convert a list of strings to integers.

# l1=['1','2','3','4']
# conv=map((lambda s: int(s)  if type(s)==str else "" ),l1)
# print(list(conv))

# 11. Use lambda with filter() to remove empty strings from a list.
# l1=lst = ["a", "", "b", "", "c", ""]
# c=filter((lambda a : a if len(a)!=0 else ""),l1)
# print(list(c))

# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner 
# madness). 
# from functools import reduce
# l1=[i for i in range(1,6)]
# s=reduce((lambda a,b:a*b),l1)
# print(s)


# 13. Write a lambda that returns the larger of two numbers.
# greater=lambda a,b: a if a>b else b
# print(greater(5,6) )


# 14. Use lambda to check if number is divisible by 5.
# divid=lambda a: "divisible" if a%5==0 else "not divisible"
# print(divid(10))

# 15. Use lambda + map() to add 10 to each element of a list. 
# l1=[1,2,3,4,5]
# s=map((lambda a:a+10),l1)
# print(list(s))

# 16. Use lambda to sort a list of dictionaries by a key (like "age").
# people = [
#     {"name": "Amit", "age": 25},
#     {"name": "Neha", "age": 19},
#     {"name": "Raj",  "age": 30}
# ]
# sorted_people = sorted(people, key=lambda x: x["age"], reverse=True)
# print(list(sorted_people))

# 17. Write a lambda that returns True if a character is a vowel. 
# vow=lambda a:"vowel" if a.lower() in['a','e','i','o','u'] else "not vowels"
# print(vow('e'))

# 18. Use lambda + filter to extract words of length > 5 from a list.
# l=['hellow','eye','horses','five','two']
# s=filter((lambda a:a if len(a)>5 else ""),l)
# print(list(s))

# 19. Use lambda to calculate the area of a circle (πr²). 
# area=lambda a : 3.142*a*a
# print(area(5))

# 20. Write a lambda to remove duplicates from a list using filter + set.
# l=[1,2,2,3,3,4,5,6,6,7]
# s=filter((lambda a:set(a)),l)
# print(list(s))

# 21. Use lambda with reduce() to find the product of all numbers in a list. 
# from functools import reduce
# l1=[1,2,3,4,5]
# s=1
# prod=reduce((lambda a,b: a*b),l1)
# print(prod)

# 22. Write a lambda that returns absolute value of a number. 
# abslt=lambda a: -1*a if a<0 else a
# print(abslt(5))

# 23. Use lambda to sort a list of strings by their length.
# l1=["hi","hello",'wow','s']
# sorted_words = sorted(l1, key=lambda x: len(x))
# print(sorted_words)

# 24. Use lambda to get only uppercase characters from a string.
# s="AbsCdkJ"
# upperchar=filter((lambda a: a if a.isupper() else ""),s)
# print(list(upperchar))

# 25. Write a lambda that returns the square if number is even, cube if odd.
# d=lambda a: a*a if a%2==0 else a*a*a
# print(d(3))


# 26. Use lambda with map to convert Celsius to Fahrenheit. 
# Fahrenheit_convt=lambda a:(a*9/5)+32
# print(Fahrenheit_convt(25))

# 27. Write a lambda to check if two strings are anagrams.
s=lambda a, b: sorted(a.lower()) == sorted(b.lower())
print(s("silent","listen"))


# 28. Use lambda to extract only numeric values from a mixed list.
# l1=['s',1,2.1,"hh"]
# numeric=filter((lambda a: a if type(a) in (int,float) else ""),l1)
# print(list(numeric))

# 29. Use lambda inside any() to check if any list element is negative. 
# l1=[1,2,3,-4,5]
# c=any(lambda a: a for a in l1 if a<0)
# print(c)

# 30. Use lambda to generate a function that multiplies any number by n
# d=lambda a : (lambda x: x*a ) 
# s=d(5)
# print(s(3))