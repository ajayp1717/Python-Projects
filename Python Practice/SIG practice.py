name="Ajay"
surname="Patil"
age=19
#concatenation=adding multiple strings and making an integer a string
print("Hello "+ name +" " +surname +" you are "+str(age)+"years old")
#Fstring
print(f"My name is {name} and I'm {age} years old")
#.format and Indexing
print("Im a {},{} and {}".format("dreamer","explorer","learner"))
#absolute function
a=-69
print(abs(a))
#Lenghts of data
print(len("mississipi"))
print("mississipi".count('s'))



#member ship operator
a=[7,9,'b',"5"]
print(7 not in a)

#Conditional Operator, if else...
# ''' if(condition)
#           print("output")
#        elif( condtion2)
#       print("output2")'''
print("enter ur age: ")
age=int(input())
if(age>=14 and age<18):

    print("teenager")
elif(age>0 and age<14):
    print("u r a child,go and hold ur milk bottle")
else:
    print("you are an adult and eligible to vote")







