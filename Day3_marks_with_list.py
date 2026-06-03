
#Student Marks Tracker
n = int(input(f"Enter number of students: "))
Marks = [ ]
Names = [ ]
for i in range(n):
    name = input(f"Enter name of student{i+1}: ")
    mark = int(input(f"Enter {name}'s marks: "))
    Names.append(name)
    Marks.append(mark)
average_marks = sum(Marks)/n
print(f"Class average: {average_marks:.2f}")
highest_marks = max(Marks)
for x in range(n):
     if Marks[x]==highest_marks:
         print(f"Topper is {Names[x]} with {Marks[x]} marks.")
