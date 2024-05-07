# Function to update weights corresponding to respective courses for either roles(ca/grader)
# lst => the weight list to be updated
# course => course that specifies location of weight to be updated
def weightUpdate(course, lst, weight):
    match course:
        case "CS 105":
            lst[0] += weight
        case "CS 145 / CS 146":
            lst[1] += weight
        case "CS 200":
            lst[2] += weight
        case "CS 201":
            lst[3] += weight
        case "CS 202":
            lst[4] += weight
        case "CS 301":
            lst[5] += weight
        case "CS 302":
            lst[6] += weight
        case "CS 311":
            lst[7] += weight
        case "CS 312":
            lst[8] += weight
        case "CS 315":
            lst[9] += weight
        case "CS 318":
            lst[10] += weight

    return lst
class Student:

# email, name, nickname, id_num, courses,
#                              upperlevel_courses, grade_courses, grade_experience, ca_courses, ca_experience,
#                              inclass, preference, hours, comments)
    def __init__(self, email, name, nickname, id_num, courses,
                             upperlevel_courses, grade_courses, grade_experience, ca_courses, ca_experience,
                             ca_inclass, preference, hours, comments):

        # store name and email
        self.name = name
        self.email = email

        # store nickname and ID number
        self.nickname = nickname
        self.id = id_num

        # allow students who tested out of CS 101/145/150 to tutor for CS 101/145/150
        if 'CS 101/145' not in courses and 'CS 150' not in courses and ('CS 200' in courses or 'CS 201' in courses):
            courses.append('CS 145')
            courses.append('CS 150')

        # we'll just disregard 101 and convert all instances of 101/145 to 145
        if 'CS 101/145' in courses:
            courses.append('CS 145')
            courses.remove('CS 101/145')

        # add CS 105 to courses in student has taken 101, 145, or 150
        if 'CS 145' in courses or 'CS 150' in courses:
            courses.append('CS 105')

        # for now we are keeping CS 145 and CS 150 tutors separate... but can change this with
        # the following code

        # if the student has taken 101/145, allow them to tutor for 150
        #if ('CS 101' in courses or 'CS 145' in courses) and 'CS 150' not in courses:
        #    courses.append('CS 150')
        #
        # if the student has taken 150, all them to tutor for 101/145
        #elif 'CS 150' in courses and 'CS 101' not in courses and 'CS 145' not in courses:
        #    courses.append('CS 101')
        #    courses.append('CS 145')

        # set list of courses a student has taken
        self.courses = courses

        # set list of upper level courses a student has taken
        self.upperlevel_courses = upperlevel_courses

        # set list of courses student wants to grade for
        self.grade_courses = grade_courses

        # set list of courses student has experience grading for
        if grade_experience != False:
            if 'CS 101' in grade_experience:
                grade_experience.append('CS 145')
        self.grade_experience = grade_experience

        # set list of courses student wants to tutor for
        self.ca_courses = ca_courses

         # set list of courses student has experience tutoring for
        if ca_experience != False:
            if 'CS 101/145' in ca_experience:
                ca_experience.append('CS 145')
                ca_experience.remove('CS 101/145')
        self.ca_experience = ca_experience

        # set list of lab classes student wants to tutor for
        self.ca_inclass = ca_inclass

        # set preference for tutoring or grading
        self.preference = preference

        # num of shifts willing to work
        self.hours = hours

        # set comments
        self.comments = comments

        # add weights depending on preference, availability and experience
        self.grade_weights = [0,0,0,0,0,0,0,0,0,0,0]
        self.ca_weights = [0,0,0,0,0,0,0,0,0,0,0]
        for grd_crse in self.grade_courses:
            self.grade_weights = weightUpdate(grd_crse, self.grade_weights, 1)
        for grd_crse in self.grade_experience:
            self.grade_weights = weightUpdate(grd_crse, self.grade_weights, 1)
        for ca_crse in self.ca_courses:
            self.ca_weights = weightUpdate(ca_crse, self.ca_weights, 1)
        for ca_crse in self.ca_courses:
            self.ca_weights = weightUpdate(ca_crse, self.ca_weights, 1)
        for ca_crse in self.ca_inclass:
            self.ca_weights = weightUpdate(ca_crse, self.ca_weights, 1)


    def addWeight(self, weight, course, role):
        fa_24_classes = ["CS 105", "CS 145 / CS 146", "CS 200", "CS 201", "CS 202", "CS 301", "CS 302", "CS 311", "CS 312", "CS 315", "CS 333"]
        if role == "Grader":
            self.grade_weights[fa_24_classes.index(course)] += weight
        else:   
            self.ca_weights[fa_24_classes.index(course)] += weight

    # this method returns the student's name if print()
    # is called on a Student object
    def __str__(self):
        return (self.name + " => " + str(self.grade_weights[1]))