#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################
from _ast import Num

def even_odd():
           
# "" Print even or odd:
#    Takes one integer from user
#    accepts only non-word numerals
#    must validate
#    Determines if even or odd
#    Prints determination
#    returns None
#    """
#    pass

    input_str = raw_input("Please enter a numeral : ")
    try:
        input_num = eval(input_str)
    except:
        print "Just enter a non word numeral"
    else:
#         print type(input_num)
         
        if (type(input_num) == type (1)):
              
            if ((input_num % 2) == 0):
                print"even"
      
            else:
                print "odd"
        else:
            print "you dint enter an integer"
    return None
            


def ten_by_ten():
    count = 1
    for i in range(10):
        print str(count) + "  ",
        count += 1
    print

    for i in range(9):
        for j in range(10):
            print str(count) + " ",
            count += 1
        print 


def find_average():
    count = 0
    result = 0
    
    
    while(True):
        val = raw_input("Please enter a Number or 'done' : ")
        if((val == "done") or (val == "Done") or (val == "DONE")) :
            break
        try:
            num = eval(val)
        except:
            print "You didn't enter a number "
        else:
            count += 1
            result = result + num
            
    count = float(count)
    Average = result/count
    print "Average = " + str(Average)
   

##############################################################################
def main():
    print "even odd"
    even_odd()
    print
     
    ten_by_ten()
    print 
    print "find_average"
    find_average()
    

if __name__ == '__main__':
    main()
