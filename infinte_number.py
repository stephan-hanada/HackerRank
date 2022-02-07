'''
	https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
	The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following:
	"123..."
	Note that "..." represents the consecutive values in between.
'''


from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

str_number = 0
for number in range(n):
    plus_one = number+1
    if (plus_one) > 99:
        str_number = str_number*1000+plus_one
    elif (plus_one) > 9:
        str_number = str_number*100+plus_one
    else: 
        str_number = str_number*10 + plus_one
print(str_number)

