def deposit():
    while True:
     amount = input ("what would you like to deposit?")
     if amount. isdigits():
        amount = int(amount)
        if amount > 0:
            break
        else:
           print("amount must be greater than zero")
    
      
     return amount
     