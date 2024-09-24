from Grade import grade


class Number_Of_Courses:
    def __init__(self, no_of_courses):
        self.numberOfCourses = list(range(no_of_courses))
        credit_load = []
        grades = []
        credit_load_multiply_by_grade = []
        for loop in self.numberOfCourses:
            # ------INPUTS (BOTH CREDIT LOAD AND GRADE)---------
            print('COURSE {0}: '.format(loop + 1))
            try:
                creditLoad = int(input('INPUT CREDIT LOAD: '))
                pass
            except ValueError:
                print("INVALID INPUT")
                creditLoad = 0
            GRADE = grade[str(input('INPUT GRADE: '))]
            credit_load.append(creditLoad)
            grades.append(GRADE)
            credit_load_multiply_by_grade.append(creditLoad*GRADE)
        pass
        total_credit_load = int(sum(credit_load))
        print("\nTOTAL CREDIT LOAD: {0}".format(total_credit_load))
        total_credit_load_multiply_by_grade = sum(credit_load_multiply_by_grade)
        GP = total_credit_load_multiply_by_grade/total_credit_load
        print("SEMESTER GP = {0}".format(round(GP, 2)))
    pass
