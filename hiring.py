from student import Student
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

    def __str__(self) -> str:
        out = "Course "+ str(self.course) + "\nGrader Target: " + str(self.target_graders) + "\n"
        count = 1
        for grader in self.graders:
            out += str(count)+". "+ str(grader.name) + "\n"
            count+=1
        out += "\nCA Target: " + str(self.target_assts) + "\n"
        count = 1
        for ca in self.assts:
            out += str(count)+". "+ str(ca.name) + "\n"
            count+=1
        return out

class HiringAlgorithm:
    def __init__(self, students, courses):
        self.unhired = students
        self.courses = courses


    def hire(self):
        numIter = len(self.unhired)
        while(numIter > 0):
            # for each course add a CA and grader with the highest weight above zero if any
            # if hired remove from unhired list
            for crse in self.courses:
                bestFit = max(self.unhired, key=lambda std: std.ca_weights[crse.course])
                if (bestFit.ca_weights[crse.course] > 0) and (crse.target_assts > len(crse.assts)):
                    crse.addAsst(bestFit)
                    self.unhired.remove(bestFit)

                bestFit = max(self.unhired, key=lambda std: std.grade_weights[crse.course])
                if (bestFit.grade_weights[crse.course] > 0) and (crse.target_graders > len(crse.graders)):
                    crse.addGrader(bestFit)
                    self.unhired.remove(bestFit)
            numIter -= 1



