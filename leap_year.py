year = int(input("What is your year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
         print("Not lap year")
    else:
       print("Not leap year")
else:
   print("Not leap year")
