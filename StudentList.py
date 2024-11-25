student={}
n=int(input("enter the no of students:"))
for i in range(n):
	print("Student details ",i+1)
	name=input("Enter the name:")
	age=int(input("Enter the age:"))
	grade=input("Enter the grade:")
	student[name]=(age,grade)
print("Student details are \n",student)
