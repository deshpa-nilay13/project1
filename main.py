# This is a program of a Mexican Food Truck menu consisting of burritos, tacos, quesadillas, enchiladas, nachos, fajitas, and churros, as well as margaritas, sodas and water for drinks. It takes the order (item and quantity) and computes the bill and the change that is due.

numBurrito = 0
numTaco = 0
numQuesadilla = 0
numEnchilada = 0
numNachos = 0
numFajita = 0
numChurro = 0
numMargarita = 0
numSoda = 0
numWater = 0

pburrito = 4.00
ptaco = 2.00
pquesadilla = 3.00
penchilada = 3.00
pnachos = 3.00
pfajita = 4.00
pchurro = 2.00
pmargarita = 5.00
psoda = 2.00
pbottledwater = 2.00

# This is a function that prints the price of each food item on the menu.

def PrintMenu():
  print ("***** MEXICAN FOOD TRUCK MENU *****")
  print ("***********************************")
  print ("FOOD ITEM          PRICE ($)")
  print ("Burrito            %.2f"%pburrito)
  print ("Taco               %.2f"%ptaco)
  print ("Quesadilla         %.2f"%pquesadilla)
  print ("Enchilada          %.2f"%penchilada)
  print ("Nachos             %.2f"%pnachos)
  print ("Fajita             %.2f"%pfajita)
  print ("Churro             %.2f"%pchurro)
  print ("Margarita          %.2f"%pmargarita)
  print ("Soda               %.2f"%psoda)
  print ("Water              %.2f"%pbottledwater)
  print 
  print ("***********************************")

# This is a function returning the change.

def computeChange(bill,cash):
  if (cash < bill):
    print("\n***** Not enough cash to pay the bill.****")
  change = cash - bill
  return change


# This is the start of the program.

# First, the menu is printed.

PrintMenu()

# Asking the user to choose their food and drink choices and the quantity of each. When they are done choosing their food and drink items, they can type “done.”

orderDone = 0

# This is a loop that takes the order of one item at a time.

while (orderDone == 0):
  print ("=============================================")
  print ("Enter your next food item/drink or enter done to finish the order and compute the bill.")
    
  item = str(input("** Food Item name or its first letter i.e. \"B\" or \"Burrito\" (or \"Done\"): "))

  # Complex "if statement" that is required in the loop of the program.

  if (item.lower() == "done" or item.lower() == "d"):
    orderDone = 1
    break

  quantity = int(input("** Enter quantity of %s "%item))
  if (item.lower() == "burrito" or item.lower() == "b"):
    numBurrito = numBurrito + quantity
  elif (item.lower()== "taco" or item.lower() == "t"):
    numTaco = numTaco + quantity
  elif (item.lower() == "quesadilla" or item.lower() == "q"):
    numQuesadilla = numQuesadilla + quantity
  elif (item.lower() == "enchilada" or item.lower() == "e"):
    numEnchilada = numEnchilada + quantity
  elif (item.lower() == "nachos" or item.lower() == "n"):
    numNachos = numNachos + quantity
  elif (item.lower() == "fajita" or item.lower() == ".2f"):
    numFajita = numFajita + quantity
  elif (item.lower() == "churro" or item.lower() == "c"):
    numChurro = numChurro + quantity
  elif (item.lower() == "margarita" or item.lower() == "m"):
    numMargarita = numMargarita + quantity
  elif (item.lower() == "soda" or item.lower() == "s"):
    numSoda = numSoda + quantity
  elif (item.lower() == "water" or item.lower() == "w"):
    numWater = numWater + quantity
  else:
    print("Invalid food item name, please enter again.")

# Computing the bill.

bill = (numBurrito * pburrito) + (numTaco * ptaco) + (numQuesadilla * pquesadilla) + (numEnchilada * penchilada) + (numNachos * pnachos) + (numFajita * pfajita) + (numChurro * pchurro) + (numMargarita * pmargarita) + (numSoda * psoda) + (numWater * pbottledwater)
print ("***********************************")
print ("bill is %.2f "%bill)
print ("***********************************")

# Computing the change.

cash = float(input("Enter Cash paid by customer: "))
change = computeChange(bill,cash)

# "if statement."

if (change < 0):
  print("** Customer did not pay enough cash, please don't deliver the order. **")
else:
  print("** Change back to customer is %.2f."%change)

print("*****  Thank You!!!  *****")

# This is the end of the program.
