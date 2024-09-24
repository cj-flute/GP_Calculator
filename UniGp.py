from Grade import uni_grade


class Uni_GP:
    def __init__(self, no_of_courses):
        self.numberOfCourses = list(range(no_of_courses))
        credit_load = []
        grades = []
        credit_load_multiply_by_grade = []
        for loop in self.numberOfCourses:
            print('COURSE {0}: '.format(loop + 1))
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
                GRADE = uni_grade[str(input('INPUT GRADE: '))]
                pass
            except KeyError:
                print("INVALID GRADE\nTRY AGAIN")
                try:
                    GRADE = uni_grade[str(input('INPUT GRADE: '))]
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
        if GP>4.49:
            print("===========")
            print("FIRST CLASS")
            print("===========")
        elif GP>3.99:
            print("==================")
            print("SECOND CLASS UPPER")
            print("==================")
        elif GP>3.49:
            print("==================")
            print("SECOND CLASS LOWER")
            print("==================")
        elif GP>2.99:
            print("===========")
            print("THIRD CLASS")
            print("===========")
        elif GP>2.00:
            print("====")
            print("PASS")
            print("====")
        else:
            print("====")
            print("FAIL")
            print("====")
    pass
