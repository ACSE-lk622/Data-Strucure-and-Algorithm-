class MusicSchool:

	students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                        "Talina": [28, "555-765-452", ["Cello"]],
                        "Eric":   [12, "583-356-223", ["Singing"]]}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	# Add your methods below this line
	def print_student_data(self):
		for student in MusicSchool.students:
			print(f"Students: {student} who is {MusicSchool.students[student][0]} years old and is taking {MusicSchool.students[student][2]} ")
	def print_student(self,name):
		if isinstance(name,str) : 
			print(MusicSchool.students[name])
	def add_student(self,new,data):
		MusicSchool.students[new] = data 


# Create the instance
Students1 = MusicSchool(8,50000)
# Call the methods
Students1.print_student_data()
Students1.print_student("Eric")
Students1.add_student('Losfre',[28,'0910262586',['playing']])
Students1.print_student_data()