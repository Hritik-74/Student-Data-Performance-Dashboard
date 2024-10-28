# Student-Data-Performance-Dashboard
This project is a Python-based dashboard for visualizing student performance data. It analyzes student attributes like age, study hours, attendance, grades, and gender to provide insights into academic performance. The project uses data visualization libraries such as Matplotlib and Seaborn.

Features
Basic Data Analysis: Calculates averages for age, study hours, attendance, and grades.
Histograms: Displays the age distribution among students.
Gender Distribution: Shows gender distribution using bar and pie charts.
Scatter Plots:
Study hours vs. grades
Attendance vs. grades
Box Plot: Visualizes grades by gender.
Line Plot: Tracks study hours per student.
Requirements
To run this project, you need:

Python 3.x
NumPy
Pandas
Matplotlib
Seaborn
Install dependencies using:

bash
pip install numpy pandas matplotlib seaborn
Usage
Clone the repository and navigate to the project directory.

Ensure you have a CSV file named student_data.csv in the same directory. This file should include columns for age, study_hours, attendance, grade, and gender.

Run the Python script:

bash
python student_dashboard.py
The script will perform basic data analysis and generate various plots, each displayed in separate windows.

Code Overview
python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('student_data.csv')

# Analysis and Visualization
# Detailed code for histograms, scatter plots, bar plots, box plots, and pie charts
Sample Visualizations
Age Distribution: Histogram of student ages
Gender Distribution: Bar plot and pie chart
Study Hours vs Grades: Scatter plot
Attendance vs Grades: Scatter plot
Grades by Gender: Box plot
Study Hours per Student: Line plot
