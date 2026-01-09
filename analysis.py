import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_analysis():
    # 1. DATA ACQUISITION
    if not os.path.exists('data.csv'):
        print("Error: data.csv not found! Please create the file first.")
        return

    df = pd.read_csv('data.csv')
    print("--- Original Data ---")
    print(df.head())

    # 2. DATA CLEANING
    # Filling missing Annual_Income with the mean
    df['Annual_Income'] = df['Annual_Income'].fillna(df['Annual_Income'].mean())
    
    # Ensuring data types are correct
    df['Age'] = df['Age'].astype(int)
    print("\n--- Data Cleaned (Missing values handled) ---")

    # 3. ANALYSIS
    correlation = df.corr()
    print("\n--- Correlation Matrix ---")
    print(correlation)

    # 4. VISUALIZATION
    # Set visual style
    sns.set_theme(style="whitegrid")

    # Figure 1: Income vs Spending
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Annual_Income', y='Spending_Score', hue='Purchases', size='Age', palette='viridis')
    plt.title('Annual Income vs Spending Score')
    plt.savefig('income_vs_spending.png') # Saves the plot as an image
    print("\nPlot 1 saved as 'income_vs_spending.png'")
    plt.show()

    # Figure 2: Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Variable Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    print("Plot 2 saved as 'correlation_heatmap.png'")
    plt.show()

if __name__ == "__main__":
    run_analysis()