
import re
import math

main_menu = '''\n\tThese Are The Available Operations\n\n\t\t0.) Add\n\t\t1.) Subtract\n\t\t2.) Multiply\n\t\t3.) Divide\n\t\t4.) Raise To A Power (y^x)
\t\t5.) Square-root\n\t\t6.) log\n\t\t7.) ln\n\t\t8.) sin\n\t\t19.) cos\n\t\t10.) tan\n\n'''

op_set =frozenset (["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

def calculation (operation = None):
    
    total_ = operation
    print(f"\t\ttotal = {total_}")

    return input( "\n\tWould You Like To Choose A Different Operation? (y/n): ")
    
def dec_from_frac (operation = None):

    total_ = operation
    print (f"\t\tDecimal: {total_}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def ex_to_the_why (operation = None):

    total_ = operation
    print (f"\t\tX^Y = {total_}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def adding(value_1):
    
    total = float(value_1)

    while True:
        value_next = input ("\t+: ")
        
        if bool(re.findall(r"[a-z]", value_next)) == True:
            print("\t\tError: Not A Number!")
        elif bool(re.findall(r"[0-9]", value_next)) == True:
            total += float(value_next)
            print(f"\t\t{total}")
        else:
            break
    return total

def subtracting (value_1):
    total = float(value_1)
    while True:
        value_next = input("\t-: ")
        
        if bool(re.findall(r"[a-z]", value_next)) == True:
            print ("\t\tError: Not A Number!")
        elif bool(re.findall(r"[0-9]", value_next)) == True:
            total -= float(value_next)
            print (f"\t\t{total}")
        else:
            break
    return total

def multiplying (value_1):
    total = float(value_1)
    while True:
        value_next = input("\t*: ")
        
        if bool(re.findall(r"[a-z]", value_next)) == True:
            print ("\t\tError: Not A Number!")
        elif bool(re.findall(r"[0-9]", value_next)) == True:
            total *= float(value_next)
            print (f"\t\t{total}")
        else:
            break
    return total

def dividing (value_1):

    value_2 = float(1)
    total =float(value_1)/float(value_2)
    while True:
        value_next = input("\t/: ")
        
        if value_next == "0":
            print ("\t\tError: Cannot Divide By 0!")
        elif bool(re.findall(r"[a-z]", value_next)) == True:
            print ("\t\tError: Not A Number!")
        elif bool(re.findall(r"[0-9]", value_next)) == True:
            value_2 = float(value_next)
            total /= value_2
            print (f"\t\tFraction: {value_1}/{value_2}")
            break
        else:
            print (f"\t\tFraction: {value_1}/{value_2}")
            break
    return total

def raise_2_pwr (value_1):

    value_2 = float(1)
    total =float(value_1)**float(value_2)
    while True:
        value_next = input("\tY: ")
        
        if bool(re.findall(r"[a-z]", value_next)) == True:
            print ("\t\tError: Not A Number!")
        elif bool(re.findall(r"[0-9]", value_next)) == True:
            value_2 = float(value_next)
            total **= value_2
            break
        else:
            break
    return total

def square_root (value_1):

    total =math.sqrt(float(value_1))
    print (f"\t\tSQRT ({float(value_1)}) = {total}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def logarithm (value_1):
    
    total =math.log10(float(value_1))
    print (f"\t\tlog ({float(value_1)}) = {total}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def natural_log (value_1):

    total =math.log(float(value_1))
    print (f"\t\tln ({float(value_1)}) = {total}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def trig_sine (value_1):
    
    angle_ = float(value_1)
    total =math.sin(math.radians(angle_))
    print (f"\t\tsin ({float(value_1)} deg.) = {total}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def trig_cosine (value_1):
    
    angle_ = float(value_1)
    total =math.cos(math.radians(angle_))
    print (f"\t\tcos ({float(value_1)} deg.) = {total}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

def trig_tangent (value_1):
    
    angle_ = float(value_1)
    total =math.tan(math.radians(angle_))
    print (f"\t\ttan ({float(value_1)} deg.) = {total}")
    
    return input ("\n\tWould You Like To Choose A Different Operation? (y/n): ")

while True:
    
    print (main_menu)
    
    user_choice = input("\tPlease Choose An Operation From The Menu: ")
    
    if user_choice not in op_set:
        print( "\tError: Not A Valid Choice")
        new_op = input( "\n\tWould You Like To Continue Using The Calculator? (y/n): ")
        if bool(re.match("y", new_op, re.I)) == True:
            continue
        else:
            print( "\n\tThanks For Using This Calculator")
            break
        
    else:
        if user_choice == "0":
            while True:
                init_value = input ("\n\tFirst Number: ")
                if bool(re.findall(r"[0-9]", init_value)) == True:
                    new_op = calculation ( operation = adding(init_value))
                    break
                else:
                    print ("\tError : That Is Not A Valid Number!")
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool(re.match("y", new_op, re.I)) == True:
                continue
            else:
                print( "\n\tThanks For Using This Calculator")
                break
        elif user_choice == "1":
            while True:
                init_value = input ("\n\tFirst Number: ")
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = calculation ( operation = subtracting (init_value))
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "2":
            while True:
                init_value = input ("\n\tFirst Number: ")
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = calculation ( operation = multiplying (init_value))
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "3":
            while True:
                init_value = input ("\n\tTop Number: ")
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = dec_from_frac ( operation = dividing (init_value))
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "4":
            while True:
                init_value = input ("\n\tX: ")
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = ex_to_the_why ( operation = raise_2_pwr (init_value))
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "5":
            while True:
                init_value = input ("\n\tNumber: ")
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = square_root (init_value)
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "6":
            while True:
                init_value = input ("\n\tNumber: ")
                if init_value == "0":
                    print ("\tError: Value Does Not Exist!")
                    continue
                elif bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = logarithm (init_value)
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "7":
            while True:
                init_value = input ("\n\tNumber: ")
                if init_value == "0":
                    print ("\tError: Value Does Not Exist!")
                    continue
                elif bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = natural_log (init_value)
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "8":
            while True:
                init_value = input ("\n\tValue In Degrees: ")
                
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = trig_sine (init_value)
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "9":
            while True:
                init_value = input ("\n\tValue In Degrees: ")
                
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = trig_cosine (init_value)
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        elif user_choice == "10":
            while True:
                init_value = input ("\n\tValue In Degrees: ")
                
                if bool (re.findall(r"[0-9]" , init_value)) == True:
                    new_op = trig_tangent (init_value)
                    break
                else:
                    print ( "\tError: That Is Not A Valid Number!" )
                    new_op = input ("Would You Like To Use A Different Operation? (y/n): ")
                    if bool(re.match("n", new_op, re.I)) == True:
                        continue
                    else:
                        break
            if bool (re.match("y", new_op, re.I)) == True:
                continue
            else:
                print  ("\n\tThanks For Using This Calculator")
                break
        

