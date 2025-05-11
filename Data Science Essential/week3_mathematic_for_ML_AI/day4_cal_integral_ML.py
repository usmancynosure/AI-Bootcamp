import numpy as np
import sympy as sp


# What is integral
    # -compute the Area under the curve, representing the accumulation

    # In Machine Learning, integrals can be used in various ways:
    # 1. To compute the area under the ROC curve (AUC) for evaluating classification models.
    # 2. To calculate expectations in probabilistic models.
    # 3. To solve optimization problems involving continuous functions.


    # Example: Compute the integral of a function
    
    
x= sp.Symbol('x')
f = x**2
definite_integral=sp.integrate(f, (x,0,2))
indefinite_integral= sp.integrate(f,x)
print("Definite integral\n", definite_integral)
print("indefinite integral\n", indefinite_integral)



# -------------------------------Optimization Technique-----------------------------------------
'''
In optimization (like in gradient descent), we're usually trying to minimize a cost/loss function.

A minimum is a point where the function value is lower than nearby values.

Global Minimum---->The lowest possible value of the function over the entire domain.

When training models:
The loss function might have many local minima.
We want the global minimum (i.e., lowest error).

convex function is ---->one global minima 
non convex function ---->multiple local minima 
'''
'''
What is SGD (Stochastic Gradient Descent)?
Stochastic Gradient Descent is a variant of gradient descent that 
updates model parameters using a single training example (or a small batch),
instead of the entire dataset.

'''
'''
Variant of SDG
    -Mini-Bactch SDG (update parameter using small batches)
    -momemtum (which add the fraction of prevoius update to the current update to accelerate the convertion)
    -Adam Optimizer (use quite alot it combine momemtum with adaption learning rates with faster conversion )
'''



