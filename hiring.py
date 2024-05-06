# 
class Course:
    def __init__(self, course, target_graders, target_assts):
        self.course = course
        self.graders = []
        self.assts = []
        self.target_graders = target_graders
        self.target_assts = target_assts

    def addAsst(self, asst):
        self.assts.append(asst)

    def addGrader(self, grader):
        self.graders.append(grader)


class HiringAlgorithm:
    def __init__(self, students):
        self.unhired = students
