# 3. Product Review Ratings
# Scenario: You are analyzing review ratings (1 to 5 stars) for a product on an e-commerce platform.
# Question: Use a bar plot or histogram to understand the distribution of ratings. What does the plot tell you about customer satisfaction?
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

random_ratings = np.clip(np.random.normal(5,1,100),0,5)

plt.subplot(1,2,1)
plt.hist(random_ratings,bins=6,color="g",alpha=.6)
plt.title("Histogram")


plt.subplot(1,2,2)
sns.boxenplot(random_ratings,color="g",)
plt.title("boxplot")

plt.tight_layout()
plt.show()

