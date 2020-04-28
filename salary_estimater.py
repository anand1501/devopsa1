from sklearn.externals import joblib
salary_model=joblib.load("salary_model.pk1")

print("\t\t\tWelcome to future tools")
print("\t\t\t------------------------")
print()

while True:
	print("""
		press 1:Salary prediction
		press 2:predict new requirement
		press 3:to exit
	""")
	print("Enter your choice:",end='')
	ch = input()

	if int(ch) == 1:
		print("Enter year exp:",end='')
		exp = input()
		exp = float()
		print("predicted salary:", salary_model.predict(exp)[0])

	elif int(ch)==2:
		print("search new requirement")
	elif int(ch)==3:
		exit()

	else:
		print("option not supported")