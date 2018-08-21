#Q=1
list1=[1,2,3,4,5]
print("Entered list is :",list1)
list1.reverse()
print("Reversed list is :",list1)

#Q=2
String="Hello My namE iS arpit Garg"
upper=""
for letter in String:
    if letter.isupper():
        upper=upper+letter+','
print("All uppercase letters:",upper)

#Q=3
value=input("Enter input:")
a=value.split(',')
b=[]
print(a)
for i in a:
    b.append(int(i))
print(b)

#Q=4
String="nitin"
rev=String[::-1]
if String==rev:
    print('String is a palindrome')
else:
    print('String is not a palindrome')

#Q=5
import copy as c
list1=[1,2,3,[4,6],5]
list2=c.deepcopy(list1)
list1[3][1]='Hey'
list1[2]='Hi'
print(list1)
print(list2)













