import math

def isLeapYearCheck(printYearStatement, status):
    if status == 1:
        newStatus = True
        return newStatus

    else:
        newStatus = False
        return newStatus


def mainFunction(year):
    status = 0
    year = int(year)
    printYearStatement = str(year)

    if year < 0:
        newStatus = isLeapYearCheck(printYearStatement, status)
        if newStatus == True:
            return True
                                
        else:
            return False

    else:
        if year > 3:
            if year % 4 == 0:
                status = 1
                if year >= 100:
                    if year % 100 == 0:
                        status = 0
                        if year >= 400:
                            if year % 400 == 0:
                                status = 1
                                newStatus = isLeapYearCheck(printYearStatement, status)
                                if newStatus == True:
                                    return True
                                
                                else:
                                    return False
                            else:
                                status = 0
                                newStatus = isLeapYearCheck(printYearStatement, status)
                                if newStatus == True:
                                    return True
                                
                                else:
                                    return False
                        else:
                            status = 0
                            newStatus = isLeapYearCheck(printYearStatement, status)
                            if newStatus == True:
                                return True
                                
                            else:
                                return False
                    else:
                        status = 1
                        newStatus = isLeapYearCheck(printYearStatement, status)
                        if newStatus == True:
                            return True
                                
                        else:
                            return False
                else:
                    status = 1
                    newStatus = isLeapYearCheck(printYearStatement, status)
                    if newStatus == True:
                        return True
                                
                    else:
                        return False
            else:
                status = 0
                newStatus = isLeapYearCheck(printYearStatement, status)
                if newStatus == True:
                    return True
                                
                else:
                    return False
        else:
            status = 0
            newStatus = isLeapYearCheck(printYearStatement, status)
            if newStatus == True:
                return True
                                
            else:
                return False

