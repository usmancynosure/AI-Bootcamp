# Ex1---->Calculate Probalities Using Bayes Theorem 
# - A disease affected 1% of a population
# - A test 90% accurate for disease individuals and 90% acccuarate for non-disease individual
# - Find the probability of havin the disease given that the positive result 
"""
    Calculates the probability of having a disease given a positive test result
    using Bayes' Theorem.

    Parameters:
    - prior: Prior probability of disease (P(D))
    - sensitivity: True positive rate (P(Pos | D))
    - specificity: True negative rate (P(Neg | ~D))

    Returns:
    - Posterior probability: P(D | Pos)
    """

def bayes_theorem(prior, sensitivity, specificity):
   
    # Complement values
    P_D = prior
    P_not_D = 1 - prior
    P_Pos_given_D = sensitivity
    P_Pos_given_not_D = 1 - specificity  # false positive rate

    # Total probability of testing positive
    P_Pos = (P_Pos_given_D * P_D) + (P_Pos_given_not_D * P_not_D)

    # Bayes' theorem
    P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

    return P_D_given_Pos

# Example use
prior = 0.01        # 1% prevalence
sensitivity = 0.9   # 90% sensitivity
specificity = 0.9   # 90% specificity

result = bayes_theorem(prior, sensitivity, specificity)
print(f"Probability of having the disease given a positive result: {result:.4f} ({result*100:.2f}%)")
