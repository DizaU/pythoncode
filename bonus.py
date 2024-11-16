salary=int(input("Enter your salary:"))
rating=int(input("Enter your rating out of 5:"))
bonus=0
validRating=True
if(rating==5):
	print("Bonus%=20")
	bonus=0.2*salary
elif(rating==4):
	print("Bonus%=15")
	bonus=0.15*salary
elif(rating==3):
	print("Bonus%=10")
	bonus=0.1*salary
elif(rating==2):
	print("Bonus%=5")
	bonus=0.05*salary
elif(rating==1):
	print("Bonus%=2")
	bonus=0.02*salary
elif(rating>5 or rating<0):
	print("invalid rating")
	validRating=False
if (validRating=True):
	print("Bonus in rupees is",bonus)
	print("So your total earnings is rupees",salary+bonus)



