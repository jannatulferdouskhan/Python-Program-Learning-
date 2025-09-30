# def rem(n,a):
#      a.remove(f"{n}")
#      return a


# l=["link",12,47,6,5,4]
# a=l
# n=(input("Enter the value of index which you want to remove: "))
# list=rem(n,a)
# print(list)


def rev(l,ward):
     n=[]
     for item in l :
         if not (item==ward):
              n.append(item.strip(ward))
     return n         
l=["fagun","khan","Agun",]  
print(rev(l,"un"))             