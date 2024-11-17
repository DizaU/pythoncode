name=input("Enter your name:")
age=int(input("Enter your age:"))
marks=int(input("Enter your marks:"))
if(age>=18):
	if(marks>=65):
		print(name,"is selected")
	else:
		print(name,"is not selected")
else:
	print("You need to wait",18-age,"years more for college")
