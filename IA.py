cookies = 48
cups_sugar = 1.5
cups_butter = 1
cups_flour = 2.75
num_cookies = int(input("How many cookies do you want to make? "))

sugar_amt = (num_cookies / cookies * cups_sugar)
butter_amt = (num_cookies / cookies * cups_butter)
flour_amt = (num_cookies / cookies * cups_flour)

print("To make " + str(num_cookies) + " cookies, you will need: \n\t" +
      format(sugar_amt, ".2f") + " cups of sugar. \n\t" +
      format(butter_amt, ".2f") + " cups of butter. \n\t" +
      format(flour_amt, ".2f") + " cups of flour. \t")
