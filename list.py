#change the item 
f =["apple","banana","cherry "]
print (f)
f[1]="orange "
print (f)
#add the item 
f=["apple","banana "]
f.append ("cherr")
print (f)
#insert
f.insert (1,"orrange ")
print (f)
#remove 
print (f)
#remove the last item 
f.pop()
print (f)

#loop through the list 
for x in f:
    print (x)
    numbers = [5, 3, 9, 1]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)
#tuple is similar to the list but cannot be modified after creation 
# it is represented by () insteadd of the []
f=("Salman",25,3.0)
for  y in f:
    print (y)

#count function use
print (f.count(3.0))
#set function used 
f={1,2,3,4,5}
print (f)
f={1,1,33,33,4444,5,5}
print (f)
f.add (60)
print (f)
#union 
a={1,121,2,2}
b={12,25,25}
print (a|b)
#intersection 
print (a&b)

#dictionary concept 
student = {
    "name":"Salman",
    "age":22,
    "cgpa":3.5
}
print (student ["name"])
#single by single acces the values 
#update the values 
student ["name "]="abdullah"
print (student )
#keys concept 
print (student.keys())
#values concept 
print (student.values())
#items concept 
print (student.items())
#loop through the dictionary
for key ,value in student.items():
    print (key ,":",value)
