# 2. Exam Scores Analysis
# Scenario: A university professor collected the final exam scores of 100 students.
# Question: Visualize the score distribution using an appropriate univariate plot. Identify if the data is normally distributed and check for any unusually low or high scores.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

total_students = 100
student_score = np.random.randint(0,101,total_students)

plt.subplot(1,2,1)
plt.hist(student_score,bins=6,color="g",alpha=.6)
plt.title("Histogram")
plt.ylabel("strength")
plt.xlabel("Score")


plt.subplot(1,2,2)
sns.boxenplot(student_score,color="g",)
plt.title("boxplot")

plt.tight_layout()
plt.show()
