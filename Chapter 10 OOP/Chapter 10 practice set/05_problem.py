from random import randint 
class Train():
      def __init__(self,train_no):
           self.train_no= train_no
      def book_tickets(self,fro,to):
           print (f"Tickets is booked in train number: {self.train_no} from {fro} to {to}")     
      def train_status(self):
           print(f"Your train {self.train_no} is is running on time")
      def get_fare(self,fro,to):
           print(f"The ticket fare of the train {self.train_no} from {fro} to {to} is {randint(222,555)}") 


a=Train(1247)
a.book_tickets("Dhaka","Rajbari")
a.train_status()
a.get_fare("Dhaka","Rajbari")                   