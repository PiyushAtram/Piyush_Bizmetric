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
l1=lst = ["a", "", "b", "", "c", ""]
c=filter((lambda a : a if len(a)!=0 else ""),l1)
print(list(c))