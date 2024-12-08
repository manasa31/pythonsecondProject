print("Omsai rama")
print("AMMA ")

print("==================================")
###STRING METHOD##

#Length string
s="python"
print("Length of the string:-",len(s))

#Replace
s="python"
print("Replace the string:-",s.replace("h","d"))

#Split method
s="Pyt.don.tell"
print("split the text after dot:-",s.split("."))

text="Apple,banana,grapes"
print("split the after comma:-",text.split(","))

print("==================================")

####STRING FORMATTING####

def sum(a,b):
    c=a+b
    print("firstvalve {},secondvaluve {},totalvalue {},".format(a,b,c))
sum(3,4)

print("==================================")

####DICTIONARYMETHODS#####

d={'a':'APPLE','b':'BALL'}

print(d['a'])#slect the key  to print value
print(d['b'])

print("Print the key",d.keys())
print("print the value",d.values())
print("print the item",d.items())
print("----------------")
print("Print the key in list",list(d.keys()))
print("Print the Value in list",list(d.values()))
print("Print the item in list",list(d.items()))
#o/p:- print the keys and values in tuple format dict_items([('a', 'Apple'), ('b', 'Ball')])



print("=====================================")
###SET METHOD###

#ADD
set1={1,2}
set1.add(3)
print("ADD in set method",set1)
print("----------")
#UPDATE
set1={1,2}
set1.update([3,4])
print("update in set method",set1)
print("----------")
#discard
set1={1,2,3,4}
set1.discard(3)
print("Remove the specifiy value:-",set1)
print("----------")
#clear
set1={1,2,3}
set1.clear()
print("Remove the all elements",set1)

print("----------")
#issubset
set1={1,2}
set2={1,2,3,4}
print("Set1 is subset of set2:-",set1.issubset(set2))
print("----------")
#issuperset
set1={1,2}
set2={1,2,3}
print("Set1 is superset of set2:-",set1.issuperset(set2))

set1={1,2,3,4}
set2={1,2,3}
print("Set1 is superset of set2:-",set1.issuperset(set2))

print("==========================")

######FOR LOOP IN LIST#########

list=[1,2,3,4,5]
for i in list:
    print(i)

print("-----------")

fruits=["Aplle","Banana","Grapes"]
for i in fruits:
    print(f"I like {i}")



####String_Slicing######

print("====String_Slicing===================")

s="Monkey man"

print(s[0:3])
print(s[1:6])
print(s[3:8])
print(s[:7])
print(s[:])
print("-----Negative--index----")
#---Negativeindex--

print(s[-10:-4])
print(s[-2:])

#####what is type casting ?#######
print("====what is type casting ====")

a=[2,3]#list
print("Convert list to tuple",tuple(a))#tuple

# Input: Float to Integer
pi=20.2# Float type
pi_int=int(pi)# Explicit type casting (truncates decimal part)
print(f"Float to integer: {pi_int},Type:{type(pi_int)}")
pi_float=float(pi_int)
print(f"Integer to float:{pi_float},Type:{type(pi_float)}")

print("-----------")
a=2#int
b="4"#string
print(f"Integer to string: {a}, Type:{type(a)}")#convert integer to string
print(f"String to Integer: {b}, Type:{type(b)}")#convert string to integer


print("-----------")
# Input: Integer to String
num =456 # Integer type
num_str=str(num)# Explicit type casting
print(f"Interger to string: '{num_str}', Type:{type(num_str)}")

print("-----------")
# Input: List to Set
num_list = [2,3,3,4,3,3] # List type
num_set=set(num_list) # Explicit type casting (removes duplicates)
print(f"list to set:{num_set},Type:{type(num_set)}")

print("-----------")
# Input: String to Integer
num_str="123"
num_int=int(num_str)
print(f"string to integer: {num_int},Type:{type(num_int)}")

print("-----------")

# Invalid Casting Example
try:
    invalid_int = int("abc")  # Cannot convert non-numeric string to integer
except ValueError as e:
    print(f"Invalid casting error: {e}")


######Forloop####

#for loop in string
string="manasa"
for i in string:
    print("String:",i)

print("-------------")
#for loop with range Specifying Start and Stop
for i in range(1,10):
    print("Print the range Specifying Start and Stop",i)

print("--------------")

#forloop with range Basic Iteration

for i in range(5):
    print("print the range Basic Iteration",i)





