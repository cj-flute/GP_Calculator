from Grade import test_grade


class Number_Of_Courses:
    def __init__(self, no_of_courses):
        self.numberOfCourses = list(range(no_of_courses))
        credit_load = [] # empty list to store credit load.
        grades = [] # empty list to store grades.
        credit_load_multiply_by_grade = [] # empty list to store the multiple of credit load and grade points.
        for loop in self.numberOfCourses:
            # ------INPUTS (BOTH CREDIT LOAD AND GRADE)---------
            print('COURSE {0}: '.format(loop + 1)) # The course
            try:
                creditLoad = int(input('INPUT CREDIT LOAD: ')) # The credit load
                pass
            except ValueError:
                print("INVALID INPUT\nTRY AGAIN")
                try:
                    creditLoad = int(input('INPUT CREDIT LOAD: ')) # The credit load after error
                    pass
                except ValueError:
                    print("INVALID INPUT\nLAST TRIAL")
                    creditLoad = int(input('INPUT CREDIT LOAD: '))
                    pass
                pass
            try:
                GRADE = test_grade[str(input('INPUT GRADE: '))] # The grade
                pass
            except KeyError:
                print("INVALID GRADE\nTRY AGAIN")
                try:
                    GRADE = test_grade[str(input('INPUT GRADE: '))]
                except KeyError:
                    print('INVALID GRADE')
                    break
                pass
            credit_load.append(creditLoad) # sending the credit load given into the list credit_load.
            grades.append(GRADE) # sending the grade given into the list grades.
            credit_load_multiply_by_grade.append(creditLoad*GRADE) # doing the multiple of credit load and grade then send to the list credit_load_multiply_by_grade.
        pass
        total_credit_load = int(sum(credit_load))
        print("\nTOTAL CREDIT LOAD: {0}".format(total_credit_load))
        total_credit_load_multiply_by_grade = sum(credit_load_multiply_by_grade)
        try:
            GP = total_credit_load_multiply_by_grade/total_credit_load
        except ZeroDivisionError:
            print("Error computing GP")
            pass
        try:
            print("SEMESTER GP = {0}".format(round(GP, 2)))
        except UnboundLocalError:
            print("RESTART PROGRAM")
            pass
        if GP>3.49:
            print("===========")
            print("DISTINCTION")
            print("===========")
        elif GP>2.99:
            print("============")
            print("UPPER CREDIT")
            print("============")
        elif GP>2.49:
            print("============")
            print("LOWER CREDIT")
            print("============")
        elif GP>1.99:
            print("====")
            print("PASS")
            print("====")
        else:
            print("====")
            print("FAIL")
            print("====")
        pass
    pass
