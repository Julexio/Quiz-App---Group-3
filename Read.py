import random

quiz_bank = {
    "What is the captial of the Philippines?"
}

def check_ans(user_ans, correct_ans): 
  if user_ans == correct_ans:
    print ("Correct")
  
  else:
    print ("Wrong")


def question (): 
    print(quiz_bank)
    print("A")
    print("B")
    print("C")
    print("D")

question()

user_ans = input ("Your answer: ").lower()
print(check_ans(user_ans, A))
