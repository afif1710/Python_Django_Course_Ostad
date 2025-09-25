
#Base Class
class Person:
    count = 0                        # Class variable to keep track of number of people
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1                       # Increment the count of people

    def introduce(self):                        
        print(f"Hi, I am {self.name}, {self.age} years old.")

    def display_role(self):             # self bcoz it is an instance method
        print("Hi, I am a person.")

    @classmethod
    def get_total_people(cls):          # cls bcoz it is a class method
        print(f"Total {cls.count} person object(s) have been created.")




#Derived Class from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)             # Call the constructor of the parent class
        self.student_id = student_id            # Unique attribute
        self.course_list = []                   # List of Courses
        self.__gpa = 0.0                        # Private attribute / Encapsulation
        
    def enroll_course(self, course):
        self.course_list.append(course)
        print(f"{self.name} has enrolled in {course}.")
    
    def show_courses(self):
        print(f"{self.name} is enrolled in the following courses:")
        for course in self.course_list:
            print(course)

    def display_role(self):             #Polymorphism
        print(f"Hi, I am a student named {self.name} and my ID is {self.student_id}.")


    @property
    def gpa(self):               #getter
        return self.__gpa
    
    @gpa.setter                  #setter
    def gpa(self, value):
        if value >= 0.0 and value <= 4.0:       
            self.__gpa = value   
        else:
            print("GPA must be between 0.0 and 4.0")
    

    @staticmethod                               #Static method / Helper function
    def is_valid_id(student_id):
        student_id = str(student_id)
        if student_id.startswith("S-"):
            print("Student is valid.")
            return True
        else:
            print('Student id must start with "S-".')   
            return False   




#Derived Class from Student
class GraduateStudent(Student):         #Inheritance
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)            # Call the constructor of the parent class which sets up inherited attributes
        self.thesis_title = thesis_title

    def display_role(self):
        print(f"Hi, I am a Graduate student named {self.name} and my ID is {self.student_id}.")



#Derived Class from Person
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)             # Call the constructor of the parent class
        self.employee_id = employee_id          # Unique attribute
        self.subject = subject                  # Subject taught
    

    def introduce(self):
        print(f"I am Professor {self.name}, teaching {self.subject}.")

    def display_role(self):        #Polymorphism
        print(f"Hi, I am a Professor and my name is {self.name} and my ID is {self.employee_id}.")
    





# #create objects

# p1 = Person("John", 46)
# s1 = Student("Gary", 20, "S-1001")
# s2 = GraduateStudent("Saka", 25, "S-2312", "Deep Learning in Farming")
# t1 = Teacher("Walter", 50, "T-5001", "Physics")

