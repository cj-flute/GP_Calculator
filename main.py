from PolyGp import Poly_GP
from UniGp import Uni_GP
from codeTest import* #remove later


def noOFCourses():
    no_of_courses = int(input("Input the number of courses done: "))
    return no_of_courses


print("Welcome to GP Calculator")
try:
    calc_type = int(input("\t\tSelect:\n1. University calculator\n2. Polytechnic calculator\n"))
    if calc_type == 1:
        print("\n \t\tUniversity calculator")
        Uni_GP(noOFCourses())
    elif calc_type == 2:
        print("\n \t\tPolytechnic calculator")
        Poly_GP(noOFCourses())
    elif calc_type == 300: # input 300. use this for any testing
        print("\n \t\t Code test")
        Number_Of_Courses(noOFCourses())
    else:
        print("Wrong input")
        exit()
except ValueError:
    print("Error...\nWrong input")
    exit()