#String
s=str("abhinav")
print(s)

#creating empty string
name=str()

#string in python is immutable

str1="abhinav"
str1=str1+"khandekar"
print(str1)

# + and * in string

str2="Welcome"
print(str2+" Home") # + is used to concanate string

str3="Abhi"
print(str3*2) # * is used for mulpla time

#Indexing String

str5="Jenkins"
print(str5[1:3]) #print e and n
print(str5[:6]) #print ony 6 char
print(str5[2:]) #skip first 2 char and print others chars

#max (), min(), len()
print(max("abc"))         #c
print(min("Abhinav"))     #A
print(len("Welcome"))     #7

#Example - in,not in

z="Welcome"
print("come" in z) #true
print("xyz" in z) #false

#String Comparison

print("Abhi"=="Khandekar") #false
print("ak"=="ak") #true
print("ak"!="bk") #true
print("ak">"cd") #false
print("ak">="ak") #true
print("yz"<"ab") #false
print("yz"<="ab") #flase

#String Testing
d="Welcome to Pythone"
x="123"
z="abhi"
y="ABHI"
#chek num in string
print(x.isalnum()) #true in x string numbers are contain
#chek aplhabates
print(d.isalpha())

#chek digit
print(d.isdigit()) #flase
print(x.isdigit()) #true

#chek lower chr
print(d.islower()) #flase
print(z.islower()) #true

#check upper char
print(y.isupper()) #true

#chek space in betwwen string
print(d.isspace()) #flase







