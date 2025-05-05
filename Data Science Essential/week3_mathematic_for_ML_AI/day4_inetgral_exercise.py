import sympy as sp


# Define a function
x=sp.Symbol('x')
f=sp.exp(-x)

# lets compute the indefinete integral
indef_integral=sp.integrate(f,x)
print("Indefinete integral \n", indef_integral)

# definiete integral
def_integral=sp.integrate(f, (x,0,sp.oo))
print("Definite integral \n", def_integral)
