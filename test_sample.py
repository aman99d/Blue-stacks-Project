from collections import Counter

#append value in dict via dict[key]=value or using .update
dict = {'key1':'geeks', 'key2':'fill_me'}
dict['key2'] = 'for'
dict['key3'] = 'geeks'
dict.update({'key4':'geeksep'})
print("Updated Dict is: ", dict)

#Find duplicate value in list using counter
MyList = ["a", "b", "a", "c", "c", "a", "c"]
a = Counter(MyList)
print (a)

#Find duplicate value in list using count
list = ["a", "b", "a", "c", "c", "a", "c"]
temp=set(list)
result={}
for i in temp:
    result[i]=list.count(i)
print (result)

#How does set works in python
list_duplicate_values = ["a", "b", "a", "c", "c", "a", "c"]
temp=set(list_duplicate_values)
print(temp)

#Count no of 1 duplicate element in list i.e "a"
MyList = ["b", "a", "a", "c", "b", "a", "c",'a']
count=0
for i in MyList:
    if i == 'a':
        count = count + 1
print ("the number of a in MyList is :", count)

#Remove item from list
myList = ["Bran", 11, 22, 33, "Stark", 44, 55, 11,"Captain"]
myList.remove("Bran") #Pass item name
myList.pop(3)  # pass index
del myList[5]  # pass index
print(myList)

