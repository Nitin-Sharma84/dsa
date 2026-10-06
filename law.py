def associative(a,b,c,op):
    lhs=eval(f"({a} {op} {b}){op} {c}")
    rhs=eval(f"{a} {op} ({b} {op} {c})")

    if rhs==lhs:
        print("True")
    else:
        print("False")

associative(5,2,3,'-')

#a*(b+c)
#(a*b) + (a*c)

def distributive(a,b,c,inop,outop):
    lhs=eval(f'{a} {outop} ({b} {inop} {c})')
    rhs=eval(f'({a} {outop} {b}) {inop} ({a} {outop} {c})')

    if rhs==lhs:
        print("True")
    else:
        print("False")

distributive(3,2,3,'+','*')
