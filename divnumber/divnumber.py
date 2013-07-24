#/usr/bin/env python

from sys import argv

def check_module (divident, divisor):
    if divident % divisor == 0:
        return True
    
    else:
        return False

def check_by_divisor (number):
    """if check_module (number, 3) and check_module (number, 5):
        print "dgp lug,","""
        
    if check_module (number, 3):
        print "dgp"

    if check_module (number, 5):
        print "lug"

    if not check_module (number, 3) and not check_module (number, 5):
        print "%i" % number

    print ",",

if __name__ == "__main__":
    input_num = int(argv[1])

    for x in range(1,input_num+1):
        check_by_divisor(x)

