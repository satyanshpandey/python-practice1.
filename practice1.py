#THIS IS PRACTICE OF DICTIONARY,LIST AND STRING...

print("Practice1")


#practice1:-
'''a=[3,4,5,"SATYU"]
b=[3,4,5,"SATYU"]
print(a in b)
print(a is b)'''
'''#practice2:-
#right way for declaring tuple means that:
tuple1=(1)#this is wrong way for declaring tuple becouse each and every element is seprated by collumn','
print(tuple1)
tuple2=(1,)#this is wright way for declaring tuple
print(tuple2)
'''
'''
#for declaring the type of the variable's and datatype
t1=()
print(type(t1))
d1={}
print(type(d1))
l1=[]
print(type(l1))
a=12
print(type(a))
b=1.2
print(type(b))
c='satyansh'
print(type(c))
'''


print("LIST")



''' LIST
# list in python
list1=["banana","apple","guavava","grapes","water malean",56,55,77,88]
list2=[2,5,4,7,9,8,6,1,0,3]
print(list1)
print(list2)
print(list1[0],list1[1],list1[2])
list1.append('orange')

list1.append(55)
list1.remove('orange')
list1.remove(55)
list2.sort()#for sorting list means list arrange in proper manner
print(list2)
list2.reverse()#for reverse list
print(list2)
print(max(list2))#for maximum length of string
print(min(list2))#for minimum length of string
print(list2.insert(0,10))#for insert any value in the list we use insert function ex:= list2.insert(position,value)
list2.remove(0)#we use 'remove' function for removing any value from list
print(list2)
list2.reverse()
list2.pop()#we use pop function for remove the last number list
print(list2)
#mutable=can change
#immutable=can not change
#for swapping of two number in python
a=2
b=4
print(a ,b)
temp=a
a=b
b=temp
print(a,b)
#for swapping of two number in python 2nd method
a,b=b,a
print(a,b)

'''



print("string")



''' STRING
#string is a data type
#string couning start with the '0' last digit is 'n-1'
mystring="this is my frist string"
mystring2="this_is_my_2nd_string"
print(mystring)
print(mystring[0:5])#print '0' index to '5' index
print(mystring[0:23:2])#print skeep 2 step from start to destination
print(len(mystring))#for count length of string
print(mystring[:])#print(mystring[0:
print(mystring[::])#print(mystring[0:23:1])
print(mystring[::-1])
print(mystring[::-2])
print(mystring[:5])
print(mystring[5:])
print(type(mystring))
print(mystring.isalnum())
print(mystring2.isalnum())
print(mystring.isalpha())
print(mystring.endswith("string"))
print(mystring2.endswith("string"))
print(mystring.count('r'))
print(mystring2.count('t'))
print(mystring.capitalize())
print(mystring2.capitalize())
print(mystring.replace("is","are"))
print(mystring.replace("string","int"))
print(mystring.lower())
print(mystring2.lower())
print(mystring.upper())
print(mystring2.upper())


'''




print("variable")



'''
VARIABLE

#we use variable as like place holder.
#how many type of the variable.........?
#find the type of the variable we use 'type' function
var1='hello python!'
var4=' i am satyansh pandey '
var2=3
var3=3.4
print(type(var1))
print(type(var2))
print(type(var3))
#for string concatination
print(var1+var4)
#for printing many times string
#print('hello python!...'*100)
#for adding two numbers.
print("enter 1st number")
n1=input()
print("enter 2nd number")
n2=input()
print("your addition is the ",int(n1)+int(n2))


'''

print("DICTIONARIES")
'''

#dictionary is a data type
#dictionary is nothing but key value pairs

#dictionary:::---
#dictionaries is nothing but key value pairs
d1={"satyansh":"samosa","neeraj":"keela","sawan":"pomogranate","ashwani":{"breakfast":"bread","lunch":"rooti","dinner":"Panner"}}
print(d1)
print(d1["sawan"])
print(d1["satyansh"])
print(d1["neeraj"])
print(d1["ashwani"])
print(d1["ashwani"]["breakfast"])
print(d1["ashwani"]["lunch"])
print(d1["ashwani"]["dinner"])
# for inserting the element in the middle of dictionaries
#this methode is used for insert in the dictionary value
d1["pandey"]="Junk Food"
print(d1)
d1["auranzeb"]="kabab"

print(d1)
d1[420] = "this is integer"
print(d1)
#   for update the value of the dictionary
d1.update({"pranjeev":"Is a Good Boy"})
print(d1)
print(d1["pranjeev"])
print(d1["ashwani"])
print(d1["ashwani"]["dinner"])

print(d1.keys())#FOR PRINT WHOLE KEYS OF THE DICTIONARIES
print(d1.items())#FOR PRINT WHOLE ITEMS OF THE Dictionary

'''




print("THANKS PYTOHN...!")