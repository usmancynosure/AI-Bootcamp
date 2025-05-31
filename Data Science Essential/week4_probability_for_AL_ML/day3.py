# Statistical inference

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def calculate_confidence_interval(data, confidence=0.95):
    """
    Calculate confidence interval for a dataset
    
    Parameters:
    -----------
    data : array-like
        The data to calculate confidence interval for
    confidence : float, optional
        The confidence level (default is 0.95 for 95% confidence)
    
    Returns:
    --------
    tuple
        (lower_bound, upper_bound) of the confidence interval
    """
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)  # Standard error of the mean
    
    # Calculate confidence interval using t-distribution
    ci = stats.t.interval(confidence, n-1, 
                         loc=mean, 
                         scale=std_err)
    return ci

def plot_confidence_intervals(data, confidence=0.95):
    """
    Plot the data distribution with confidence interval
    
    Parameters:
    -----------
    data : array-like
        The data to plot
    confidence : float, optional
        The confidence level (default is 0.95)
    """
    plt.figure(figsize=(10, 6))
    
    # Plot histogram of data
    sns.histplot(data, kde=True, alpha=0.5)
    
    # Calculate and plot confidence interval
    ci = calculate_confidence_interval(data, confidence)
    mean = np.mean(data)
    
    # Plot mean and confidence interval
    plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.axvline(ci[0], color='green', linestyle=':', label=f'Lower CI: {ci[0]:.2f}')
    plt.axvline(ci[1], color='green', linestyle=':', label=f'Upper CI: {ci[1]:.2f}')
    
    plt.title(f'Data Distribution with {confidence*100}% Confidence Interval')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def compare_confidence_intervals(sample_sizes=[10, 30, 100, 1000], confidence=0.95):
    """
    Compare confidence intervals for different sample sizes
    
    Parameters:
    -----------
    sample_sizes : list
        List of sample sizes to compare
    confidence : float, optional
        The confidence level (default is 0.95)
    """
    plt.figure(figsize=(12, 6))
    
    # Generate data for each sample size
    for i, n in enumerate(sample_sizes):
        # Generate random data from normal distribution
        data = np.random.normal(100, 15, n)
        ci = calculate_confidence_interval(data, confidence)
        mean = np.mean(data)
        
        # Plot confidence interval
        plt.errorbar(i, mean, yerr=[[mean-ci[0]], [ci[1]-mean]], 
                    fmt='o', capsize=5, label=f'n={n}')
    
    plt.axhline(100, color='red', linestyle='--', label='True Mean')
    plt.xticks(range(len(sample_sizes)), sample_sizes)
    plt.title(f'Confidence Intervals for Different Sample Sizes ({confidence*100}% confidence)')
    plt.xlabel('Sample Size')
    plt.ylabel('Mean Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Example 1: Basic confidence interval calculation
    print("Example 1: Basic confidence interval calculation")
    data = np.random.normal(100, 15, 100)  # Generate random data
    ci = calculate_confidence_interval(data)
    print(f"95% Confidence Interval: ({ci[0]:.2f}, {ci[1]:.2f})")
    print(f"Sample Mean: {np.mean(data):.2f}")
    print(f"True Mean: 100.00")
    print("\n" + "="*50 + "\n")
    
    # Example 2: Visualize confidence interval
    print("Example 2: Visualizing confidence interval")
    plot_confidence_intervals(data)
    print("\n" + "="*50 + "\n")
    
    # Example 3: Compare different sample sizes
    print("Example 3: Comparing confidence intervals for different sample sizes")
    compare_confidence_intervals()
    print("\n" + "="*50 + "\n")
    
    # Example 4: Real-world scenario - Website visit duration
    print("Example 4: Real-world scenario - Website visit duration")
    # Simulate website visit durations (in minutes)
    visit_durations = np.random.exponential(5, 1000)  # Mean duration of 5 minutes
    ci = calculate_confidence_interval(visit_durations)
    print(f"Average visit duration: {np.mean(visit_durations):.2f} minutes")
    print(f"95% Confidence Interval: ({ci[0]:.2f}, {ci[1]:.2f}) minutes")
    plot_confidence_intervals(visit_durations)
    print("\n" + "="*50 + "\n")
    
    # Example 5: Different confidence levels
    print("Example 5: Comparing different confidence levels")
    confidence_levels = [0.90, 0.95, 0.99]
    for conf in confidence_levels:
        ci = calculate_confidence_interval(data, conf)
        print(f"{conf*100}% Confidence Interval: ({ci[0]:.2f}, {ci[1]:.2f})")

if __name__ == "__main__":
    main()
