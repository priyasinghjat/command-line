# factorial number
# fact=1
# n=1
# while n<=5:
#     fact=fact*n
#     n=n+1
# print(fact)

# Fibonacci sequence
# a = 0
# b = 1
# n = 1

# while n <= 5:
#     a, b = a + b, a
#     print(a)
#     n += 1

# a=0
# b=1
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     a,b=a+b,a
#     print(a)

# fact=1
# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     fact=fact*i
   
# print(fact)


# l=[1,2,3,4]
# for i in range(4):
#     print(l[i])

# l={1,2,3,4,5,6}
# for i in l:
#     print(i)
    # print(type(l))
# student=['neha','priya','jai','kshitiz','piyush']
# employee=['manager','clerk','head','ceo']
# demo={"class":student,
#       "office":employee}
# for i,j in demo.items():
#     print(j[3])


# s="hello this priya singh jat"
# l=len(s)
# for i in range(l):
#     print(s[i])

# s="hello this is priya"
# count={}
# for char in s:
#     if char.isalpha():
#          count[char]=count.get(char,0)+1
# for char,i in count.items():
#      print(char,i)

# def demo(n):
#     name=input("enter a name: ")
#     n.append(name)
#     return n
# n1=[]
# for i in range(5):
#     n1=demo(n1)
#     print(n1)

# def demo(n,a):
#     for i in range(a):
#         name=input("enter your name: ")
#         n.append(name)
#     return n

# n1=[]
# a=int(input("how many student name you want: "))
# n1=demo(n1,a)
# print(n1)


# def demo(list_name):
#     name=input("enter your name:")
#     list_name.append(name)
#     return list_name
# name=[]
# n=int(input("enter your number"))
# for i in range(n):
#     name=demo(name)
# print(name)
        


# assignment

# find the sum of even number which is present in list

# l=[1,2,3,4,5,6]
# sum=0
# sums=0
# for i in l:
#     if i%2==0:
#         sum+=i
#     if i%2==1:
#         sums+=i
# print(sum)
# print(sums)

# count the number of occurance of each element in a listt

# l="hey priya how are you"
# count={}
# for char in l:
#     if char.isalpha():
#         count[char]=count.get(char,0)+1
#     for char,i in count.items():
#         print(char,i)


# check if the tuple contain only unique element

# def unique_element(tup):
#     count=set()
#     for element in tup:
#         if element in count:
#             return False
#         count.add(element)
#     return True
            
# tup=(1,2,3,3,4)

# if contain_unique_element(tup):
#     print("it has unique element")
# else:
#     print("not unique element")


# def has_unique_elements(tup):
#     seen_elements = set()
#     for element in tup:
#         if element in seen_elements:
#             return False
#         seen_elements.add(element)
#     return True

# tup = (1, 2, 3, 4, 5)

# if has_unique_elements(tup):
#     print("The tuple contains only unique elements.")
# else:
#     print("The tuple contains duplicate elements.")


# def unique_element(tup):
    # container=set()
    # for element in tup:
    #     if element in container:
    #         return False
    #     container.add(element)
    # return True
    # container=[]     wrong
    # for element in tup:
    #     if element not in container:
    #         container.append(element)
    # return container

# import random

# l=[1,2,3,4,5.5,'lnb']
# print(random.choice(l))


# import pickle
# lst=['priya','neha','sonam','raju']
# with open('lst.pkl','wb') as file:
#     pickle.dump(lst,file)

# with open('lst.pkl','rb') as file:
#     unpickled_file=pickle.load(file)
# print(unpickled_file)
      
      
# tup=(1,2,3,4,4,5,5)

# if unique_element(tup):
#     print("unique")
# else:
#     print("duplicate")
# res=unique_element(tup)
# print(res)

# REMOVE DUPLICATE FROM THE LIST
 
# def duplicate_element(lst):
#     count=[]
#     for element in lst:
#         if element not in count: 
#             count.append(element)
#     return count
# lst=[1,1,2,3,4]

# if duplicate_element(lst):
#     print("exist duplicate")
# else:
#     print(" duplicate")

# res=duplicate_element(lst)
# print(res)





        




    
    


