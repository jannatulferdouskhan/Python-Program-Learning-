def gen(n):
     table= ""
     for i in range(1,11):
         table +=f"{i} X {n}={i*n}\n"
     with open(f"tables/table_{n}","w") as f:
         f.write(table)
for n in range(2,32):
     gen(n)

      

          

 


