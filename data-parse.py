import csv, random, json
from student import Student
from hiring import HiringAlgorithm, Course
# /Users/sgakuya@middlebury.edu/Downloads/f24.csv

class DataParser:
    def __init__(self, filename):
        # create an empty list of students
        self.students = []

        # open the file from Google forms
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            # go through each row in file
            for row in csv_reader:
                # skip first row
                if line_count > 0:
                    # get email, name, id number, and employment status from sheet
                    email = row[1]
                    name = row[2]
                    nickname = row[3]
                    id_num = row[4]
                    
                    # set courses and upper level courses
                    courses = row[5].split(', ')
                    upperlevel_courses = row[6]

                    # add grading/ca experience and preferences for all courses 
                    fa_24_classes = ["CS 105", "CS 145 / CS 146", "CS 200", "CS 201", "CS 202", "CS 301", "CS 302", "CS 311", "CS 312", "CS 315", "CS 333"]
                    # h-r(7-17) => grader , s-ac(18-28) => ca
                    grade_courses = []
                    grade_experience = []
                    ca_courses = []
                    ca_experience = []
                    for i in range(7,29):
                        if(i<18):
                            if "experience" in row[i]:
                                grade_experience.append(fa_24_classes[i-7])
                            if "willing" in row[i] or "preferred" in row[i]:
                                grade_courses.append(fa_24_classes[i-7])
                        else:
                            if "experience" in row[i]:
                                ca_experience.append(fa_24_classes[i-18])
                            if "willing" in row[i] or "preferred" in row[i]:
                                ca_courses.append(fa_24_classes[i-18])

                    # set courses they can be inclass CAs for
                    temp_inclass = row[29].split(',')
                    inclass = []
                    for i in range(0,len(temp_inclass), 3):
                        if len(temp_inclass) > 1:
                            inclass.append(temp_inclass[i]+temp_inclass[i+1]+temp_inclass[i+2])
                    
                    # set preference for grader vs CA
                    preference = row[30]

                    # set # of CA hours
                    hours = 0
                    match row[31]:
                        case "I don't want to work as a course assistant":
                            hours = 0
                        case "2-3":
                            hours = 2
                        case "4-5":
                            hours = 4
                        case "6+":
                            hours =6

                    # set CTLR preference
                    ctlr = row[32]
                    ctlr_courses = row[33]

                    # set interest in being the social CA
                    social_ca = row[34]

                    # comments
                    comments = row[35]

                    # create student object
                    student = Student(email, name, nickname, id_num, courses,
                             upperlevel_courses, grade_courses, grade_experience, ca_courses, ca_experience,
                             inclass, preference, hours, comments)

                    # add student object to list
                    self.students.append(student)

                line_count += 1

        

    # this method sorts the students by last name, then by first name
    def sort_students(self):

        # sort students by last name
        self.students.sort(key = lambda x: x.name.split()[-1], reverse = False)

        # now sort by first name if last names are the same
        sort = False
        while sort == False:
            sort = True
            for i in range(1, len(self.students)):
                student = self.students[i]
                prev_student = self.students[i-1]

                if student.name.split()[-1] == prev_student.name.split()[-1]: # last names
                    if student.name.split()[0] < prev_student.name.split()[0]: # first names
                        self.students[i-1] = student
                        self.students[i] = prev_student
                        sort = False
        count = 1
        # for std in self.students:
        #     print(count, std)
        #     count += 1

if __name__ == "__main__":
    parser = DataParser("/Users/sgakuya@middlebury.edu/Downloads/f24.csv")
    # print(parser.students)
    # parser.sort_students()

    # Minimal Tests
    # test_students = parser.students[0:10]
    # for std in test_students:
    #     std.grade_weights[1] = random.randint(0,5)
    #     print(std)
    # test_courses = [Course(1, 2, 3)]
    # alg = HiringAlgorithm(test_students, test_courses)
    # alg.hire()
    # for crse in test_courses:
    #     print(crse)


    # Courses
    course_list = []
    # cs105
    course_list.append(Course(0, 1, 1))
    # cs145/cs146
    course_list.append(Course(1, 5, 8))
    # cs200
    course_list.append(Course(2, 3, 4))
    # cs201
    course_list.append(Course(3, 3, 8))
    # cs202
    course_list.append(Course(4, 3, 3))
    # cs301
    course_list.append(Course(5, 3, 3))
    # cs302
    course_list.append(Course(6, 3, 2))
    # cs311
    course_list.append(Course(7, 0, 1))
    # cs312
    course_list.append(Course(8, 3, 3))
    # cs315
    course_list.append(Course(9, 0, 2))
    # cs333
    course_list.append(Course(10, 0, 1))

    students = parser.students

    for std in students:
        print(json.dumps(std.__dict__) + "\n")
    alg = HiringAlgorithm(students, course_list)
    alg.hire()

    for course in course_list:
        print(course)

