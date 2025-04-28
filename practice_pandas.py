import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1.	You have two DataFrames: students (with student IDs and names) and grades (with student IDs and exam scores). How would you combine them so that only students with recorded grades are included?

table1 = pd.DataFrame({
    "id": list(range(1, 11)),
    "name": ["riyan", "bilal", "khan", "ashbal", "sami", "faisal", "ayman", "hamza", "usman", "zayan"]
})

grades = np.random.choice(["A", "B", "C", "D", "F"], size=6, p=[0.3, 0.3, 0.2, 0.1, 0.1]) 

table2 = pd.DataFrame({
    "id": list(range(5, 11)),
    "grade": grades
})

result = pd.merge(table1,table2,on="id",how="inner")

print(result)

# 2.	You need to merge employee and department DataFrames, ensuring all departments are shown even if no employees belong to them. What kind of join will you use?


department = pd.DataFrame({
    "dept_id": [101, 102, 103, 104],
    "dept_name": ["HR", "Engineering", "Marketing", "Finance"]
})

employee = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "emp_name": ["Alice", "Bob", "Charlie", "David"],
    "dept_id": [101, 102, 101, 103]
})

result2 = pd.merge(department,employee,on="dept_id",how="left")

print(result2)

# 3.	A university has separate DataFrames for Spring, Summer, and Fall admissions. How would you combine them vertically into a single DataFrame?

spring = pd.DataFrame({
    "id": [101, 102, 103]
})

summer = pd.DataFrame({
    "id": [201, 202]
})

fall = pd.DataFrame({
    "id": [301, 302, 303, 304]
})

result3= pd.concat([spring,summer,fall],axis=1)

print(result3)

# 4.	You’re merging two DataFrames but lose some rows from the first one. Which type of join might be causing this?

# it is the right join

#  5. Total sales per product category (use groupby and sum)

sales = pd.DataFrame({
    "category": ["Electronics", "Clothing", "Electronics", "Groceries", "Clothing"],
    "amount": [200, 150, 300, 120, 180]
})

result4 = sales.groupby("category")["amount"].sum().reset_index()
print(result4)

# 6. Average rating per customer (use groupby and mean)

reviews = pd.DataFrame({
    "customer_id": [1, 2, 1, 3, 2, 3],
    "rating": [4, 5, 3, 4, 2, 5]
})

result5 = reviews.groupby("customer_id")["rating"].mean().reset_index()
print(result5)

# 7. Count students per grade (use value_counts() or groupby)
grades_df = pd.DataFrame({
    "grade": ["A", "B", "A", "C", "B", "A", "C", "B", "A"]
})

result6 = grades_df["grade"].value_counts().reset_index(name="count").rename(columns={"index": "grade"})
print(result6)

# 8. Group age into brackets (use pd.cut)
people = pd.DataFrame({
    "age": [5, 17, 23, 36, 45, 67, 29, 15]
})

bins = [0, 18, 35, 60, 100]
labels = ["0-18", "19-35", "36-60", "61+"]
people["age_group"] = pd.cut(people["age"], bins=bins, labels=labels)

result7 = people
print(result7)

# 9. Categorize temperatures (use apply() or pd.cut)
temps = pd.DataFrame({
    "celsius": [5, 15, 22, 28, 35, 40]
})

def label_temp(temp):
    if temp < 15:
        return "Cold"
    elif temp < 30:
        return "Warm"
    else:
        return "Hot"

temps["category"] = temps["celsius"].apply(label_temp)

result8 = temps
print(result8)

# 10. Apply 10% discount to prices
products = pd.DataFrame({
    "price": [100, 200, 300, 400]
})

products["discounted_price"] = products["price"] * 0.9

result9 = products
print(result9)

# 11. Rename all columns to lowercase
data = pd.DataFrame({
    "Name": ["Ali", "Sara"],
    "Age": [23, 30],
    "Country": ["Pakistan", "Morocco"]
})

data.columns = data.columns.str.lower()

result10 = data
print(result10)

# 12. Save DataFrame to CSV without index
df_to_save = pd.DataFrame({
    "name": ["Zain", "Areeba"],
    "score": [88, 92]
})

# Save to CSV without index
df_to_save.to_csv("students.csv", index=False)

result11 = df_to_save
print(result11)

# 13. Visualize distribution of "Income" (use .plot(kind='hist'))


incomes = pd.DataFrame({
    "income": [30000, 45000, 50000, 52000, 70000, 32000, 60000, 48000, 39000]
})

result12 = incomes

# Plot (optional to show in script)
incomes["income"].plot(kind="hist", bins=5, title="Income Distribution")
plt.xlabel("Income")
plt.show()

#  14. Compare monthly sales of two products (use line plot)
monthly_sales = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "product_A": [200, 220, 250, 270, 300],
    "product_B": [180, 210, 230, 260, 290]
})

result13 = monthly_sales

# 15. Relationship between math and science scores (use scatter plot)
# Example data: Math and Science scores of students
student_scores = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "math_score": [88, 92, 79, 85, 91],
    "science_score": [84, 90, 78, 80, 87]
})

# Scatter plot to show relationship between math and science scores
plt.scatter(student_scores["math_score"], student_scores["science_score"])
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.title("Relationship between Math and Science Scores")
plt.show()

result14 = student_scores

# 16. Histogram and KDE curve for customers' ages (use seaborn.histplot)

ages = pd.DataFrame({
    "age": [22, 34, 23, 25, 33, 31, 26, 28, 32, 29, 24, 35, 30]
})

# Plot histogram and KDE curve together
sns.histplot(ages["age"], kde=True)
plt.title("Age Distribution with Histogram and KDE Curve")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

result15 = ages

# 17. Visualize relationship and distribution of two numerical variables (use seaborn.jointplot)

data = pd.DataFrame({
    "weight": [55, 65, 70, 80, 60, 75, 85, 90, 95, 88],
    "height": [160, 162, 165, 170, 168, 172, 175, 180, 185, 177]
})

# Jointplot combining scatter and histograms
sns.jointplot(x="weight", y="height", data=data, kind="scatter")
plt.suptitle("Weight and Height Relationship", y=1.02)
plt.show()

result16 = data


# 18. Compare median income across three job categories (use seaborn.boxplot)
# Example data: Job category and income
job_data = pd.DataFrame({
    "job_category": ["Engineer", "Artist", "Engineer", "Artist", "Manager", "Manager", "Artist", "Engineer", "Manager"],
    "income": [70000, 45000, 75000, 42000, 65000, 62000, 46000, 74000, 63000]
})

# Boxplot to compare the distribution and median income across job categories
sns.boxplot(x="job_category", y="income", data=job_data)
plt.title("Income Distribution by Job Category")
plt.show()

result17 = job_data


#  19. Survey responses by gender (use seaborn.countplot)

survey_data = pd.DataFrame({
    "gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "preference": ["Product A", "Product B", "Product A", "Product C", "Product B", "Product A", "Product C", "Product B"]
})

# Count plot to show responses by gender
sns.countplot(x="preference", hue="gender", data=survey_data)
plt.title("Survey Responses by Gender")
plt.show()

result18 = survey_data

# 20. Visualize correlation matrix of features (use seaborn.heatmap)

# Example data: Features and their correlations
features = pd.DataFrame({
    "feature_1": [1, 2, 3, 4, 5],
    "feature_2": [5, 4, 3, 2, 1],
    "feature_3": [2, 3, 4, 5, 6],
    "feature_4": [6, 5, 4, 3, 2]
})

# Calculate correlation matrix
corr_matrix = features.corr()

# Heatmap to visualize correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

result19 = corr_matrix
