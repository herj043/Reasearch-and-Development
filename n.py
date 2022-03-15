def test():
  print("text")

  
date.dope()
def guess():
  win = input("Type Something: ")
  
  if "OP".lower() in win.lower():
    print("yes")
  else:
    guess()

guess()
cont = "zero"
while "no".lower() not in cont.lower():
  cont = input("Would you like to play again? (Yes/No) ")
  if "yes" in cont.lower():
    guess()
  if "no" in cont.lower():
    print("Thanks for testing!")
  else:
    print("unaccepted statement")