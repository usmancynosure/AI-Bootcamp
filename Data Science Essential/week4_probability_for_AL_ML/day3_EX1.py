import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime

class SamplingReport:
    def __init__(self, population_size=10000):
        """
        Initialize the sampling report generator
        
        Parameters:
        -----------
        population_size : int
            Size of the population to generate
        """
        self.population_size = population_size
        self.population = None
        self.samples = {}
        self.report_data = {}
        
    def generate_population(self, mean=100, std=15):
        """Generate a synthetic population"""
        self.population = np.random.normal(mean, std, self.population_size)
        return self.population
    
    def take_samples(self, sample_sizes=[30, 100, 500, 1000], num_samples=100):
        """Take multiple samples of different sizes"""
        for size in sample_sizes:
            samples = []
            for _ in range(num_samples):
                sample = np.random.choice(self.population, size=size, replace=False)
                samples.append(sample)
            self.samples[size] = samples
        return self.samples
    
    def calculate_statistics(self):
        """Calculate statistics for each sample size"""
        for size, samples in self.samples.items():
            means = [np.mean(sample) for sample in samples]
            stds = [np.std(sample) for sample in samples]
            cis = [stats.t.interval(0.95, len(sample)-1, 
                                  loc=np.mean(sample), 
                                  scale=stats.sem(sample)) 
                  for sample in samples]
            
            self.report_data[size] = {
                'means': means,
                'stds': stds,
                'cis': cis,
                'mean_of_means': np.mean(means),
                'std_of_means': np.std(means),
                'ci_coverage': sum(1 for ci in cis if ci[0] <= np.mean(self.population) <= ci[1]) / len(cis)
            }
        return self.report_data
    
    def plot_distributions(self):
        """Plot population and sample distributions"""
        plt.figure(figsize=(15, 10))
        
        # Plot population distribution
        plt.subplot(2, 2, 1)
        sns.histplot(self.population, kde=True)
        plt.title('Population Distribution')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        
        # Plot sample means distribution
        plt.subplot(2, 2, 2)
        for size in self.samples.keys():
            means = [np.mean(sample) for sample in self.samples[size]]
            sns.kdeplot(means, label=f'n={size}')
        plt.axvline(np.mean(self.population), color='red', linestyle='--', 
                   label='Population Mean')
        plt.title('Distribution of Sample Means')
        plt.xlabel('Sample Mean')
        plt.ylabel('Density')
        plt.legend()
        
        # Plot confidence intervals
        plt.subplot(2, 2, 3)
        for i, size in enumerate(self.samples.keys()):
            means = [np.mean(sample) for sample in self.samples[size]]
            cis = self.report_data[size]['cis']
            for j, (ci, mean) in enumerate(zip(cis, means)):
                color = 'green' if ci[0] <= np.mean(self.population) <= ci[1] else 'red'
                plt.plot([i, i], ci, color=color, alpha=0.3)
                plt.plot(i, mean, 'o', color=color, alpha=0.3)
        plt.axhline(np.mean(self.population), color='blue', linestyle='--', 
                   label='Population Mean')
        plt.xticks(range(len(self.samples)), self.samples.keys())
        plt.title('95% Confidence Intervals')
        plt.xlabel('Sample Size')
        plt.ylabel('Value')
        plt.legend()
        
        # Plot coverage rate
        plt.subplot(2, 2, 4)
        sizes = list(self.samples.keys())
        coverages = [self.report_data[size]['ci_coverage'] for size in sizes]
        plt.bar(sizes, coverages)
        plt.axhline(0.95, color='red', linestyle='--', label='Expected Coverage (95%)')
        plt.title('Confidence Interval Coverage Rate')
        plt.xlabel('Sample Size')
        plt.ylabel('Coverage Rate')
        plt.legend()
        
        plt.tight_layout()
        plt.savefig('sampling_report.png')
        plt.close()
    
    def generate_report(self):
        """Generate a comprehensive report"""
        report = []
        report.append("="*50)
        report.append("SAMPLING ANALYSIS REPORT")
        report.append("="*50)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Population Size: {self.population_size}")
        report.append(f"Population Mean: {np.mean(self.population):.2f}")
        report.append(f"Population Std: {np.std(self.population):.2f}")
        report.append("\n" + "="*50)
        
        for size in self.samples.keys():
            report.append(f"\nSample Size: {size}")
            report.append("-"*30)
            report.append(f"Mean of Sample Means: {self.report_data[size]['mean_of_means']:.2f}")
            report.append(f"Std of Sample Means: {self.report_data[size]['std_of_means']:.2f}")
            report.append(f"CI Coverage Rate: {self.report_data[size]['ci_coverage']*100:.1f}%")
            
            # Calculate and report bias
            bias = self.report_data[size]['mean_of_means'] - np.mean(self.population)
            report.append(f"Bias: {bias:.2f}")
            
            # Calculate and report MSE
            mse = np.mean([(np.mean(sample) - np.mean(self.population))**2 
                          for sample in self.samples[size]])
            report.append(f"Mean Squared Error: {mse:.2f}")
        
        report.append("\n" + "="*50)
        report.append("\nKey Findings:")
        report.append("1. As sample size increases:")
        report.append("   - Standard error decreases")
        report.append("   - Confidence intervals become narrower")
        report.append("   - Coverage rate approaches 95%")
        report.append("2. The Central Limit Theorem is demonstrated by:")
        report.append("   - Sample means following normal distribution")
        report.append("   - Mean of sample means approaching population mean")
        report.append("   - Decreasing standard error with larger samples")
        
        # Save report to file
        with open('sampling_report.txt', 'w') as f:
            f.write('\n'.join(report))
        
        return '\n'.join(report)

def main():
    # Create sampling report
    report = SamplingReport(population_size=10000)
    
    # Generate population
    report.generate_population(mean=100, std=15)
    
    # Take samples
    report.take_samples(sample_sizes=[30, 100, 500, 1000], num_samples=100)
    
    # Calculate statistics
    report.calculate_statistics()
    
    # Generate plots
    report.plot_distributions()
    
    # Generate and print report
    print(report.generate_report())
    
    print("\nReport files generated:")
    print("1. sampling_report.txt - Detailed analysis")
    print("2. sampling_report.png - Visualizations")

if __name__ == "__main__":
    main() 