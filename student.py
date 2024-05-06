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

        self.app_weight = 0

    def addWeight(self, weight):
        self.app_weight += weight

    # this method returns the student's name if print()
    # is called on a Student object
    def __str__(self):
        return (self.name + " => " + self.preference)