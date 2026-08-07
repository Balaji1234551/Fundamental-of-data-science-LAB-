import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Student data
study_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 50, 55, 60, 65, 70, 72, 80, 85, 90]

# Create DataFrame
data = pd.DataFrame({
    "Study Time": study_time,
    "Exam Score": exam_scores
})

print("Student Data:")
print(data)

# Calculate correlation
correlation = data["Study Time"].corr(data["Exam Score"])

print("\nCorrelation Coefficient:", round(correlation, 2))

# Scatter Plot
plt.figure(figsize=(7, 5))
plt.scatter(study_time, exam_scores)

plt.title("Study Time vs Exam Scores")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)

plt.show()

# Line Plot
plt.figure(figsize=(7, 5))
plt.plot(study_time, exam_scores, marker='o')

plt.title("Study Time vs Exam Scores - Line Plot")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.grid(True)

plt.show()

# Correlation interpretation
if correlation > 0:
    print("\nResult: There is a positive correlation between study time and exam scores.")
elif correlation < 0:
    print("\nResult: There is a negative correlation between study time and exam scores.")
else:
    print("\nResult: There is no correlation between study time and exam scores.")
