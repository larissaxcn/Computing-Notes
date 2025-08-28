'''
# 1
Given two integer variables, a and x (where a is 10 and x is 2), write a single
expression that adds 1 to a, and then multiplies the resulting value by x.
Print out the result of your evaluated expression, with the words
"Question 1 Result:" preceding your result print out.
'''

a = 10
x = 2
expression1 = (1 + a) * x
print("Question 1 Result: " + str(expression1))

'''
# 2
Given three integer variables, x, lb, and ub (where x is 2, lb is 1, and ub is
2), write a single boolean expression that evaluates to True if x is strictly
between lb and ub, and False otherwise.
Print out the result of your evaluated expression, with the words
"Question 2 Result:" preceding your result print out.
'''
x = 2
lb = 1
ub = 2

#expression2 = lb < x < ub
expression2 = (lb < x) and (ub > x)
print("Question 2 Result: " + str(expression2))

'''
# 3
Given three integer parameters a, b, and c (where a is 4, b is 3, and c is 5),
write a single boolean expression that returns True if a2+b2 is equal to c2
(this is called a "Pythagorean Triple"), and False otherwise. For example, given
the a=4, b=3, c=5, the expression evaluate as True. Print out the result of your
evaluated expression, with the words
"Question 3 Result:" preceding your result print out.
'''
a = 4
b = 3
c = 5
expression3 = (a ** 2 + b ** 2 == c ** 2)
print("Question 3 Result: " + str(expression3))

'''
# 4
Suppose that, in order to graduate a (fictional) MA program, students need to
complete at least four Computer Science courses, at least four Social Science
electives, and exactly two workshop classes. Note that students are allowed to
substitute computing classes with courses from the Statistics Department.
Finally, their GPA must be above 3.0 to graduate from the program under normal
conditions. If their GPA is 3.0 or lower, they do have the option, though, to
write a thesis to complete their requirements and graduate.

Write an expression (and any variables that you find useful) to evaluate whether
students with the following characteristics are eligible to graduate from the
program. If they are eligible to graduate, your expression should evaluate as
True, otherwise it should evaluate as False. Print out the results of your
evaluated expressions for each student, with the words "Question 4, Student
NUMBER_HERE Graduation Eligibility:" preceding your result print out.

Student 1: 4 Social Science Electives, 3 Computer Science courses, 1 Statistics
course, 2 workshops, 3.7 GPA, no thesis on file.
Student 2: 5 Social Science Electives, 4 Statistics courses, 2 workshops,
3.0 GPA, wrote a thesis.
'''

# Student 1
ss = 4
cs = 3
stat = 1
ws = 2
gpa = 3.7
thesis = False

grad_elig = (((cs + stat) >= 4) 
             and (ss >= 4) 
             and (ws == 2) 
             and (gpa > 3.0 or thesis))

print("Question 4, Student 1 Graduation Eligibility: " + str(grad_elig))

# Student 2
ss = 5
cs = 0
stat = 4
ws = 2
gpa = 3.0
thesis = True

grad_elig = (((cs + stat) >= 4) 
             and (ss >= 4) 
             and (ws == 2) 
             and (gpa > 3.0 or thesis))

print("Question 4, Student 2 Graduation Eligibility: " + str(grad_elig))