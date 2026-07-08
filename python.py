#string indexing 
name = "Python"
print (name [0])
print (name [1])
#negative indexing 
print (name [-1])
print (name [-2])

rollnumber = "Fa22-bcs-101"
print (rollnumber [1])
print (rollnumber [-1])
#sring slicing 
print (name [0:4])
# slicing from the begning 
a="abcdefghaijklmnopqrstuvwxyz"
print (a[:15])
#slice to end 
print (a[3:])
#entire string 
print (a[:])
#reverse string 
print (a[::-1])
#upper function 
print (a.upper())
#count  function 

print (a.count ("a"))
#start with function 
print (a.startswith ("a"))
#length of the string 
print (len (a))
# check whether all the charachterrs are letters or number
print (a.isalnum()) 
# check the digit 
print (a.isdigit())
#check the letter
print(a.isalpha())