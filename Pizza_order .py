#Pizza Order

#Problem
''' Make a pizza order which will receive order and generate bill accordingly'''

#Solution

print("*** Welcome to Python Pizza Deliveries! ***")

#Taking inputs
size = input("What size pizza do you want? Small, Medium, or Large \n ==>")
add_pepperoni = input("Do you want pepperoni? Yes or No \n ==>")
extra_cheese = input("Do you want extra cheese? Yes or No \n ==> ")

bill =0
if size == "Small":
  bill += 15
  if add_pepperoni == "Yes":
   bill += 2
elif size == "Medium":
  bill += 20
  if add_pepperoni == "Yes":
   bill += 3
elif size == "Large":
  bill += 25
  if add_pepperoni == "Yes":
   bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

print()
print(*** Thank You ***)