class Student:
	def __init__(self, name, roll_no):
		self.name = name
		self.roll_no = roll_no
		self.__marks = {}
	
	def add_marks(self, subject, mark):
		if mark>=0 and mark<=100:
			self.__marks[subject] = mark
	
	def get_marks(self):
		return self.__marks
	
	def percentage(self):
		if len(self.__marks)==0:
			return 0
		else:
			percentage= sum(self.__marks.values())/len(self.__marks)
		return percentage
		
	
	def check_pass_status(self):
		has_passed = all(mark>=40 for mark in self.__marks.values())
		if has_passed:
			print(f"{self.name} has passed")
		else:
			print(f"{self.name} has failed")

class Report:
	@staticmethod
	def generate(student : Student):
		print("–––Student Marks Report–––")
		print(f"Roll.No: {student.roll_no}\nStudent name: {student.name}")
		print("–––––––––––––––")
		for subject, marks in student.get_marks().items():
			print(f"{subject} : {marks}")
		print("–––––––––––––––")
		print(f"Percentage: {student.percentage()}%")
		student.check_pass_status()
		print("\n\n")

a = Student("Anu", 3)
a.add_marks("Chemistry", 98)
a.add_marks("Electronics", 80)
a.add_marks("Python", 90)
a.add_marks("Maths", 88)
Report.generate(a)

b = Student("Sneha", 6)
b.add_marks("Chemistry", 77)
b.add_marks("Electronics", 66)
b.add_marks("Python", 22)
b.add_marks("Maths", 40)
Report.generate(b)
