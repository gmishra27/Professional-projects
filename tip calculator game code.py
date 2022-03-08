#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator ")
tot_bill= input("What was the Total bill? $")
tip=input("How much tip would you like to give? 10, 12 or 15? ")
tip_split=input("How many people to split the bill? ")
calc1=float(tot_bill)
calc2=int(tip)
calc3=int(tip_split)
final_bill=(calc1/calc3)*(1+(calc2/100))
round_final_bill=round(final_bill,2)
round_final_bill="{:.2f}".format(final_bill)
print(f"Each person should pay: ${round_final_bill}")

