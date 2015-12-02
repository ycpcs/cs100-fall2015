from TurtleWorld import *

####################################################################################################################
# Problem 1: getLetterGrade - Write a function getLetterGrade that accepts a numerical grade (grade) and outputs the
# letter grade for the given numerical grade, based on the following table
#     output 'A'  for 4.0,
#            'B+' for 3.5,
#            'B'  for 3.0,
#            'C+' for 2.5,
#            'C'  for 2.0,
#            'D'  for 1.0,
#            'F'  for 0.0
# Use if-elif-else to determine the letter grade, and the validity of the numerical grade.
# The function should return True if the numerical grade entered was valid (any of the above grades),
# and False otherwise

def getLetterGrade (grade):
    # TODO P1-1: Complete the code for getLetterGrade here
    if (grade == 4.0):
        print('A')
    elif (grade == 3.5):
        print('B+')
    elif (grade == 3.0):
        print('B')
    elif (grade == 2.5):
        print('C+')
    elif (grade == 2.0):
        print('C')
    elif (grade == 1.0):
        print('D')
    elif (grade == 0.0):
        print('F')
    else:
        return False

    return True


####################################################################################################################
# Problem 3: draw_star

def draw_star(t,size):
    pd(t)

    # TODO P3-1: Complete the draw_star function here
    for i in range (5):
        fd(t,size)
        rt(t,144)

def main():
    world = TurtleWorld()
    turtle = Turtle()

    #################################################################################################################
    # Problem 2: Grades
    # TODO: create a for loop that runs until all grades have been entered
    #       The body of the for loop gets a numerical grade from the user, and then passes that numerical grade
    #       to getLetterGrade, which outputs the letter grade, and returns True, if the numerical grade is valid,
    #       and False if the numerical grade was invalid.
    #
    #       The loop should keep separate counts of the valid and invalid grades entered.  Make sure to properly
    #       initialize the two variables that track the counts
    #          If getLetterGrade returns True, update valid_cnt, gpa, and output "Valid grade entered"
    #          If getLetter Grade returns False, update invalid_cnt, and output "Invalid grade entered"
    #       The loop should also accumulate the valid grades in gpa.  make sure to properly initialize gpa, as well.
    #
    # After the for loop terminates, calculate the gpa from the valid grades accumulated in gpa / valid grade count

    # number of grades to enter
    grades = int(input('Enter the number of numerical grades to be converted: '))

    # TODO P2-1: Provide an appropriate initialization value for valid_cnt
    # count of valid grades
    valid_cnt = 0

    # TODO P2-1: Provide an appropriate initialization value for invalid_cnt
    # count of invalid grades
    invalid_cnt = 0

    # TODO P2-1: Provide an appropriate initialization value for gpa
    # accumulate valid grades and then calculate gpa
    gpa = 0

    # TODO P2-2: for loop starts here, embed the following lines in the loop, down to line that says "Loop ends here"
    #            the for loop should process all grades entered by the user
    for i in range(grades):
        grade = float(input('\nEnter next numerical grade: '))

        # TODO P2-3: Pass the grade entered above to getLetterGrade
        # TODO P2-4: Provide an if statement that checks the return value of getLetterGrade,
        #            updates valid_cnt, gpa, invalid_cnt, as necessary, and outputs the appropriate message from below
        if (getLetterGrade(grade)):
            gpa = gpa + grade
            valid_cnt = valid_cnt + 1
            print('Valid grade entered')
        else:
            invalid_cnt = invalid_cnt + 1
            print('Invalid grade entered')
    # TODO P2-2: for loop ends here

    # TODO P2-5: Calculate the gpa for the valid grades
    gpa = gpa / valid_cnt

    # After the loop terminates, output the counts of valid and invalid grades, and the gpa
    print ('\nValid grades:', valid_cnt, ', Invalid grades:', invalid_cnt, ', gpa', gpa, '\n')

    ################################################################################################################
    # Problem 3:

    # TODO P3-2: Validate the user input such that it is greater than 0
    length = 0

    while length <= 0:
        length = int(input('Enter a length value greater than 0: '))


    #TODO P3-3: Call the draw_star function if the user input a value greater than 50
    if length > 50:
        draw_star(turtle, length)
    #        otherwise print an error message
    else:
        print('Length must be greater than 50 to draw a star')

    key = input('Press any key to exit')
    world.destroy()

main()