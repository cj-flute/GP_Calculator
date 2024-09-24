from Grade import poly_grade


class Poly_GP:
    def __init__(self, no_of_courses):
        self.numberOfCourses = list(range(no_of_courses))
        credit_load = []
        grades = []
        credit_load_multiply_by_grade = []
        for loop in self.numberOfCourses:
            print('COURSE {0}: '.format(loop + 1))
            try:
                creditLoad = int(input('INPUT CREDIT LOAD: '))
                pass
            except ValueError:
                print("INVALID INPUT\nTRY AGAIN")
                try:
                    creditLoad = int(input('INPUT CREDIT LOAD: '))
                    pass
                except ValueError:
                    print("INVALID INPUT\nLAST TRIAL")
                    creditLoad = int(input('INPUT CREDIT LOAD: '))
                    pass
                pass
            try:
                GRADE = poly_grade[str(input('INPUT GRADE: '))] # The grade
                pass
            except KeyError:
                print("INVALID GRADE\nTRY AGAIN")
                try:
                    GRADE = poly_grade[str(input('INPUT GRADE: '))]
                except KeyError:
                    print('INVALID GRADE')
                    break
                pass
            credit_load.append(creditLoad)
            grades.append(GRADE)
            credit_load_multiply_by_grade.append(creditLoad*GRADE)
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
