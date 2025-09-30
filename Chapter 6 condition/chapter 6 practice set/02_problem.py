Bangla=float(input("Enter the mark of Bangla "))
English=float(input("Enter the mark of English: "))
Math=float(input("Enter the mark of Math: "))
total_percentaze=(((Math + Bangla + English)/100)*100)/3
if(Bangla>33):
     if(English>33):
           if(Math>33):
                  if(total_percentaze >= 40):
                         print("The student is passed")
else:
      print("The student is failed")                        
                  
print("Percentaze is:",total_percentaze,"%")