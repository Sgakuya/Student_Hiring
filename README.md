Author: Smith Gakuya

# __Middlebury College CS Department Student Hiring__
A simple tool to aid in selecting of student graders and course assistants in the Middlebury College Computer Science department.

The program works by parsing in applications as a csv and utilizing a greedy algorithm to assigned best fits for various positions.

Weights are assigned by considering student experience in the position(s) being applied for, willingness/availability and professor preferences.

Assignment is performed beginning with higher level courses and finishing with lower level courses. To ensure fair distribution of talent a grader and assistant are assigned to a course in each iteration of the algorithm.

Note: This tool doesn't consider other possibly crucial information(e.g., information in the comments section) and should serve only as a tool to come up with initial assignments that can be revised. 