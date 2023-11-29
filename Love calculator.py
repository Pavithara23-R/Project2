print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_word = name1 + name2
lower_names = combined_word.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l+o+v+e
total = int(str(first_digit)+ str(second_digit))
if (total <10) or (total>90):
  print(f"Your score is {total}, you go together like coke and mentos.")
elif (total>=40) and (total<=50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")



