'''
	https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
	Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False. Note that the code stub provided 	reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
'''


def is_leap(year):
    leap = False
    
    condition_1 = year%4==0
    condition_2 = year%100==0
    condition_3 = year%400==0
    
    if (condition_1 and condition_2 and condition_3):
        return True
    elif (condition_1 and condition_2 and not condition_3):
        return leap
    elif (condition_1 and not condition_2):
        return True
    
    return leap

year = int(raw_input())
print is_leap(year)
