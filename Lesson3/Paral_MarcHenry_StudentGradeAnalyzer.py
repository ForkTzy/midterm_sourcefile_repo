# Store the raw comma-separated records (including Part F test records).
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A & F: Parse and organize the records safely.
for record in raw_records:
    # Split the record into fields.
    fields = record.split(",")

    # Add a guardian condition for an invalid field count (must have name + 3 scores = 4 fields).
    if len(fields) != 4:
        print(f"Skipped invalid record (field count error): {record}")
        continue

    # Store the student's name.
    name = fields[0]

    # Convert the score fields to numbers safely.
    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record (non-numeric score): {record}")
        continue

    # Add the name and scores to student_scores.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("\nORGANIZED STUDENT RECORDS")
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # Guard against an empty score list.
    if not scores:
        continue

    # Calculate total, average, highest, and lowest.
    total = sum(scores)
    num_scores = len(scores)
    average = total / num_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    # Update sum of averages for class summary.
    sum_of_averages += average

    # Append the result tuple to ranking: (average, name, highest, lowest, remark)
    ranking.append((average, name, highest_score, lowest_score, remark))


# PART D: Sort and display the ranking.
# Sort ranking from highest to lowest average.
ranking.sort(reverse=True, key=lambda x: x[0])

print("\nSTUDENT GRADE REPORT")
print(f"{'Rank':<6}{'Name':<7}{'Average':<9}{'Highest':<9}{'Lowest':<8}{'Remark'}")

# Use enumerate() and tuple unpacking to display the ranking.
for rank, (average, name, highest, lowest, remark) in enumerate(ranking, start=1):
    print(f"{rank:<6}{name:<7}{average:<9.2f}{highest:<9}{lowest:<8}{remark}")


# PART E: Display the class summary.
total_valid_students = len(ranking)

# Calculate the class average safely.
class_average = sum_of_averages / total_valid_students if total_valid_students > 0 else 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {total_valid_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")

# Use ranking[0] and ranking[-1] safely to fetch highest and lowest ranked students.
if total_valid_students > 0:
    highest_student = ranking[0]
    lowest_student = ranking[-1]
    print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
    print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")