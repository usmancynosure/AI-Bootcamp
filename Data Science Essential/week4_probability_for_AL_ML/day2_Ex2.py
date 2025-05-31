import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import skew, kurtosis

# Load the Iris dataset
url = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(url)

def analyze_distribution(data, title):
    """
    Analyze and visualize the distribution of data including skewness and kurtosis
    """
    # Calculate statistics
    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)
    skewness_val = skew(data)
    kurtosis_val = kurtosis(data)
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot histogram with KDE
    sns.histplot(data, kde=True, ax=ax1)
    ax1.set_title(f'Histogram of {title}')
    ax1.axvline(mean, color='r', linestyle='--', label=f'Mean: {mean:.2f}')
    ax1.axvline(median, color='g', linestyle='--', label=f'Median: {median:.2f}')
    ax1.legend()
    
    # Plot Q-Q plot
    stats.probplot(data, dist="norm", plot=ax2)
    ax2.set_title('Q-Q Plot')
    
    # Print statistics
    print(f"\nAnalysis of {title}:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    print(f"Skewness: {skewness_val:.2f}")
    print(f"Kurtosis: {kurtosis_val:.2f}")
    
    # Interpret skewness
    if abs(skewness_val) < 0.5:
        skew_interpretation = "approximately symmetric"
    elif skewness_val > 0:
        skew_interpretation = "right-skewed (positive skew)"
    else:
        skew_interpretation = "left-skewed (negative skew)"
    
    # Interpret kurtosis
    if abs(kurtosis_val) < 0.5:
        kurt_interpretation = "mesokurtic (similar to normal distribution)"
    elif kurtosis_val > 0:
        kurt_interpretation = "leptokurtic (heavy tails)"
    else:
        kurt_interpretation = "platykurtic (light tails)"
    
    print(f"\nInterpretation:")
    print(f"Distribution is {skew_interpretation}")
    print(f"Distribution is {kurt_interpretation}")
    
    plt.tight_layout()
    plt.show()

# Analyze each numeric column in the dataset
numeric_columns = df.select_dtypes(include=[np.number]).columns

print("Distribution Analysis of Iris Dataset")
print("=" * 50)

for column in numeric_columns:
    analyze_distribution(df[column], column)

# Create a summary table of all distributions
def create_distribution_summary(df):
    summary = []
    for column in numeric_columns:
        summary.append({
            'Feature': column,
            'Mean': np.mean(df[column]),
            'Median': np.median(df[column]),
            'Std Dev': np.std(df[column]),
            'Skewness': skew(df[column]),
            'Kurtosis': kurtosis(df[column])
        })
    return pd.DataFrame(summary)

# Display summary table
summary_df = create_distribution_summary(df)
print("\nSummary of All Features:")
print("=" * 50)
print(summary_df.round(3))

# Additional Analysis: Compare distributions by species
print("\nAnalyzing distributions by species:")
print("=" * 50)

for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='variety', y=column, data=df)
    plt.title(f'{column} Distribution by Species')
    plt.show()
    
    # Calculate statistics by species
    print(f"\nStatistics for {column} by species:")
    print(df.groupby('variety')[column].agg(['mean', 'median', 'std', 
                                           lambda x: skew(x), 
                                           lambda x: kurtosis(x)]).round(3))


