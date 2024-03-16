'''
1.) Python program to capitalize the first and last character of each
# word in a string
# 2.) Input : 128 # Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
s1=("hello world")
s2=s1[0].upper()
s3=s1[-1].upper()

print(s2+s1[1:len(s1)]+s3)

n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")


n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
    print("yes")
else:
    print("no")


l1=[1,2,3,4]
l2=[5,6,7,8]

l3=[]
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)


---->set

charctristics of set
1)set can b e created using {}
2)the elements inside set are not indexed
3)does not allow duplicate values
4)it unordered
5)heterogenous
6)multable or changable

#eg:1
s1={9,89,7.76,8+7J,(8,7,5),"truck",'e'}
print(s1)


s1="google"
freq=0
for i in s1:
    freq+=1
    print(s1.split())

#eg2
#s2={5,8,98,[9,0]}
#print(s2)--->error
#eg:3
#min(),max(),len()

#eg:4
#to add element inside set
s1={8,78,67,'u'}
s1.add(45)#--->add
print(s1)
#update
s1.update("hello world")
print(s1)


#to delete element inside set
s1={8,78,67,'u'}
#s1.pop()
#print(s1)--->it delete random element

#delete specifc element we use remove()&discard()&clear()

#remove()
s1.remove(8)
print(s1)

#discard()
s1.discard(8767)
print(s1)

#clear()
l1={}
print(type(l1))#-=--->datatype is dict

s1=set()#to create empty set
print(type(s1))


s1={8,9,4,"r"}
s1.clear()
print(s1)


del s1
print(s1)


#join the sets
s1={9,0,8}
s2={9.90,"card",'t',56}
s3=s1.union(s2)#---->union function used for to combine 2 sets
print(s3)


s1={4,5,6}
s2={7,8,5,6}
#print(s1.intersection(s2))

print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s1))


#isdisjoit(),issubset(),issuperset()
s1={1,2,3,4,5}
s2={3,2,7,8,9}
for val in s1:
    if val in s2:
        str1="its joint set"
print("its joint set")

# To print all the keys

d1={1:100, 2:200, 3:300, 4:400}
print(d1.keys())
print(type(d1.keys()))


# To print all the values

d1={1:100, 2:200, 3:300, 4:400}
print(d1.values())


# Iterating dictionary
# To iterate keys alone

d1={1:100, 2:200, 3:300, 4:400}
for val in d1:
    print(val)

# To iterate values alone

d1={1:100, 2:200, 3:300, 4:400}
for val in d1.values():
    print(val)

# to get both key and values

d1={1:100, 2:200, 3:300, 4:400}
for key, val in d1.ite
'''
# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']























