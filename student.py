import re

"""
 Function to update weights corresponding to respective courses for either roles(ca/grader)
 lst(int list) => the CA/grader weight list of a particular student. Each index represents a course
 course(string) => course that specifies location of weight to be updated in lst
 weight(int) => how much to increment the current weight in the specific class by 

 Note: would need updates to contain different set of courses for different semesters
"""
def weightUpdate(course, lst, weight):
    if re.search("^CS 105.*", course):
        lst[0] += weight
    elif re.search("^CS 145.* | CS 146.*", course):
            lst[1] += weight
    elif re.search("^CS 200.*", course):
        lst[2] += weight
    elif re.search("^CS 201.*", course):
        lst[3] += weight
    elif re.search("^CS 202.*", course):
        lst[4] += weight
    elif re.search("^CS 301.*", course):
        lst[5] += weight
    elif re.search("^CS 302.*", course):
        lst[6] += weight
    elif re.search("^CS 311.*", course):
        lst[7] += weight
    elif re.search("^CS 312.*", course):
        lst[8] += weight
    elif re.search("^CS 315.*", course):
        lst[9] += weight
    elif re.search("^CS 333.*", course):
        lst[10] += weight

    return lst
"""
    Student class keeps track of each students info 
    i.e., email, name, nickname/preferred name, id, courses taken 
    and extra data about the courses they have assisted with and 
    those they would like to be considered for

"""
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
        # updating weights by 1 if they have experience, willingness, and availability for labs
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

    # this method returns the student's name if print()
    # is called on a Student object
    def __str__(self):
        return (self.name + " => " + str(self.grade_weights[1]))