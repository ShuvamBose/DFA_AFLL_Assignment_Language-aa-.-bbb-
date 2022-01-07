'''
language chosen: (aa)*.(bbb)+
'''
def in_put(): #input function
    print("The language is: (aa)*.(bbb)+")
    print("Enter the string to validate: ")
    n=input()
    print("Entered string: ",n)
    return n

def my_valid(str_): #string validator func.
    c_a=0;c_b=0;
    if 'ba' in str_:
            return -1
    
    else:
        for i in str_:
            if i=='a':
                c_a+=1
            elif i=='b':
                c_b+=1
            elif not (i in 'ab'):
                return 0
    
        if c_a % 2==0 and c_b >0 and c_b % 3==0 :
            return 1
        else :
            return 2 

v=my_valid(in_put()) #nested func. call
#the dfa table 
print("DFA Table:") 
print("__________________________")
print("states:| a          |  b ")
print("--------------------------")
print("->Q0   | Q1         |  Q3 ")
print("Q1     | Q2         | DEADSTATE  ")
print("Q2     | Q1         | Q3  ")
print("Q3     | DEADSTATE  | Q4 ")
print("Q4     | DEADSTATE  | Q4  ")
print("*Q5    | DEADSTATE  | Q3  ")
print("__________________________\n")

print("Result:")
if v == -1:
    print("Invalid format of string a's cannot come after b's!")
elif v== 0:
    print("You have entered uwanted characters in string other than a,b !")
elif v==1:
    print("String is accepted according to DFA.")
elif v==2: 
    print("Entered string doesn't match the DFA pattern & criteria !")