#Revrse String

#method 1 by using loop
s="Welcome"
rev_str=" "
for i in s:
    rev_str=i+rev_str
print("Revrsed string is : ",rev_str)

#method 2 by using Slicing Operator
x="Abhi"
rev=x[::-1] #x[starting:ending:-1]
print(rev)

