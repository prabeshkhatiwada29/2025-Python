marks=int(input("Enter student marks:"))
grade=["A","B"]
if(marks >=90):
    grade:"A"
elif(marks >=80 and marks <90):
    grade:"B"
elif(marks >=70):
    grade:"C"
else:
    grade="D"

print("grade of the student ->",grade)
