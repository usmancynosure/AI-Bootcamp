
# Bayes theorem
# Prior probabilty P(A)
# how likely the evidence if A is happen/true P(B/A)
# the total probabilty of the evidence P(B)

# def bayes(prior, likelihood, Evidence):
#     bayes_result=(likelihood * prior)/Evidence



#-------------------------------------------- Gausain Distribution
import numpy as np
import matplotlib.pyplot as plt


# mu(Mean (μ): The center of the distribution (where the peak is).)
# Standard Deviation (sigma): Controls the spread. A smaller makes the curve narrower; a larger makes it wider.
mu , sigma = 0, 1

x= np.linspace(-4, 4, 100)
y=(1/(np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5* ((x-mu)/sigma )**2)

plt.plot(x,y)
plt.title("Gausain Distribution")
plt.show()

#-------------------------------------------- Bernoulli Distribution 
# Describr outcomes of a binanry experiment 
    # p(X=1)=p , P(X=0)=1-p
    
p=0.6 
plt.bar([0,1], [1-p, p], color="Silver")
plt.title("Bernualli Distribution")
plt.xticks([0, 1], labels=["0 (Failure)", "1 (Success)"])
plt.show()

# ------------------------------------Binomial Distribution
# Model the number of successes in n independent Bernaulli trail

'''
import scipy.stats as binom
n, p= 10, 0.5
x=np.arange(0,n+1)
y= binom.pmf(x, n, p)
plt.bar(x, y , color="Silver")
plt.title("Binomial Distribution")
plt.show()
'''

# Poisson Distribution 
# Model the number of event in the fixed interval of time and space 
import scipy as poisson

lam =3 
x=np.arange(0,10)
y =poisson.pmf(x,lam)
plt.bar(x, y , color="yellow")
plt.title("Poisson Distribution")
plt.show()