mylist=[1,5,7,9,6]

# traditional way without using list comprehenssion
newlist= []

for item in mylist:
    newlist.append(item*item)

print(newlist)


print("Using new technology")

#Using list comprehension 

newlist=[i*i for i in mylist]

print(newlist)