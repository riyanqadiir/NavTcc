# 1. Customer Spending Distribution
# Scenario: You’re analyzing monthly spending data for customers at an online store.
# Question: Using a univariate plot, explore the distribution of monthly spending. What kind of plot (histogram/boxplot/KDE) would you use, and what does it reveal about customer spending behavior (e.g., skewness, outliers)?
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# file_path = "../class task/vrlvGH.xlsx"
# df = pa.read_excel(file_path)
# print(df)

spending_range = 1000
total_user_spending = np.random.randint(500,5000,spending_range)

# sales = df["Sales"]
# sales = pa.to_numeric(sales,errors="coerce")

# Create a figure with two subplots
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 2, 1)
plt.hist(total_user_spending, bins=10, color='blue', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(total_user_spending, color='green')
plt.title('Box Plot')

plt.tight_layout()
plt.show()