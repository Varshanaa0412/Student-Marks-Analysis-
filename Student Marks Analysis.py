marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input(f"Enter marks for student {i+1}: "))
    marks.append(m)

# Calculations
average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

# Grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

# Pass/Fail count
pass_count = 0
fail_count = 0

for m in marks:
    if m >= 50:
        pass_count += 1
    else:
        fail_count += 1

# Output
print("\n--- Result ---")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Overall Grade:", grade)
print("Passed:", pass_count)
print("Failed:", fail_count)