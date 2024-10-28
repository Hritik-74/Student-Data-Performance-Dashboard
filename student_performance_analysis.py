import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file with error handling
try:
    data = pd.read_csv('student_data.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: student_data.csv file not found.")
    exit()

# Extract columns for analysis
ages = data['age']
study_hours = data['study_hours']
attendance = data['attendance']
grades = data['grade']
gender = data['gender']

# Perform basic data analysis
print("\nBasic Data Analysis:")
print(f"Average Age: {np.mean(ages):.2f}")
print(f"Average Study Hours: {np.mean(study_hours):.2f}")
print(f"Average Attendance: {np.mean(attendance):.2f}%")
print(f"Average Grade: {np.mean(grades):.2f}")

# Histogram for Student Ages
plt.figure(figsize=(8, 6))
sns.histplot(ages, bins=5, kde=True, color='skyblue')
plt.title('Distribution of Student Ages', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# Bar Plot for Gender Distribution
plt.figure(figsize=(8, 6))
gender_counts = data['gender'].value_counts()
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='pastel')
plt.title('Gender Distribution', fontsize=16)
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, axis='y', alpha=0.3)
plt.show()

# Scatter plot for Study Hours vs Grades
plt.figure(figsize=(8, 6))
sns.scatterplot(x='study_hours', y='grade', data=data, color='green')
plt.title('Study Hours vs Grades', fontsize=16)
plt.xlabel('Study Hours', fontsize=14)
plt.ylabel('Grades', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# Scatter plot for Attendance vs Grades
plt.figure(figsize=(8, 6))
sns.scatterplot(x='attendance', y='grade', data=data, color='orange')
plt.title('Attendance vs Grades', fontsize=16)
plt.xlabel('Attendance (%)', fontsize=14)
plt.ylabel('Grades', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# Pie Chart for Gender Distribution
plt.figure(figsize=(8, 6))
plt.pie(gender_counts, labels=gender_counts.index, colors=['#1f77b4', '#ff7f0e'], autopct='%1.1f%%', startangle=90, explode=(0, 0.1))
plt.title('Gender Distribution Pie Chart', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()

# Box Plot for Grades by Gender
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='grade', data=data, palette='Set2')
plt.title('Box Plot of Grades by Gender', fontsize=16)
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Grades', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# Line plot for Study Hours per Student
plt.figure(figsize=(8, 6))
student_ids = np.arange(1, len(study_hours) + 1)
plt.plot(student_ids, study_hours, marker='o', linestyle='-', color='purple', label='Study Hours', markersize=8)
plt.title('Study Hours per Student', fontsize=16)
plt.xlabel('Student ID', fontsize=14)
plt.ylabel('Study Hours', fontsize=14)
plt.grid(True, alpha=0.3)
plt.xticks(student_ids)
plt.legend()
plt.show()

