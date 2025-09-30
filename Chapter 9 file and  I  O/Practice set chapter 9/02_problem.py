import random

def game():
     score=random.randint(1,64) 
     print("You are playing the game...")
            # print(f"Your score:{score}")
     with open("high_score.txt") as f:
         high_score=f.read()
         if (high_score!=""):
          high_score=int(high_score)
         else:
             high_score=0
     if (score>high_score):
         with open("high_score.txt","w") as f:
             f.write(str(score))
         print(f"Congratulation {score} is a new high score")
                    
     else:
         print(f"Your score {score} || High score is{high_score}")
     return score 
game()
                                
    

