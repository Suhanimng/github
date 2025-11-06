"""
NAME: Suhani
DATE: 20 October 2025
PROJECT NAME: Daily Calorie Tracker
"""

# TASK-1
print("Welcome! This is a program to keep track of your calories")

# TASK-2
n = int(input("Enter number of meals: "))
meals = []
calories = []

for i in range(n):
    print("Enter meal name:")
    meals.append(input())
    print("Enter calories:")
    calories.append(int(input()))

# TASK-3
total = sum(calories)
average = total / n
limit = int(input("Enter daily calorie limit: "))

# TASK-4
if total > limit:
    status_message = "Warning: Calorie limit exceeded"
else:
    status_message = "Success: Calories within limit"

print(status_message)

# TASK-5
print("Meal Name\tCalories")
for i in range(n):
    print(meals[i], "\t", calories[i])
print("Total:", total)
print("Average:", average)

# TASK-6
output_filename = "calorie_report.txt"

try:
    with open(output_filename, 'w') as f:
        f.write("Calorie Report\n\n")
        f.write("Status: " + status_message + "\n\n")
        f.write("Meal Name\tCalories\n")
        for i in range(n):
            f.write(meals[i] + "\t" + str(calories[i]) + "\n")
        f.write("Total: " + str(total) + "\n")
        f.write("Average: " + str(average) + "\n")

    print("Report saved as", output_filename)

except IOError as e:
    print("Error saving report:", e)
