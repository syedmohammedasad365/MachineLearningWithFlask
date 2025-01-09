# 1. Create a DataFrame from the given data
import pandas as pd
data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000]
}
df = pd.DataFrame(data)
# 2. Perform the specified tasks
# a. Display the first 2 rows of the DataFrame
print("First 2 rows of the DataFrame:")
print(df.head(2))
# b. Add a new column named `Bonus` where the bonus is 10% of the salary
df["Bonus"] = df["Salary"] * 0.10
# c. Calculate the average salary of employees in the DataFrame
average_salary = df["Salary"].mean()
print(f"\nAverage salary of employees: {average_salary}")
# d. Filter and display employees who are older than 25
filtered_employees = df[df["Age"] > 25]
print("\nEmployees who are older than 25:")
print(filtered_employees)