# Hello everyone Im henry paral
# First we need to list our scores
scores = [85, 72, 91, 64, 78]

# Then calculate the variables 
total_score = sum(scores)
average_score = total_score / len(scores) if len(scores) > 0 else 0
highest_score = max(scores)
lowest_score = min(scores)

# Print the student scores
print("Student Scores:")
for score in scores:
    print(score)

print()  # Blank line

# Create variables with these 2 
passed_count = 0
failed_count = 0

# Analyze each students score
for index in range(len(scores)):
    x = scores[index]

    # Determine remarks based on the grading scale
    if x >= 75:
        if x >= 90:
            remark = "Excellent"
        elif x >= 80:
            remark = "Very Good"
        else:
            remark = "Good"

        print(f"Student {index + 1}: {x} - {remark} - Passed")
        passed_count += 1
    else:
        print(f"Student {index + 1}: {x} - Failed")
        failed_count += 1

print()  # Empty line for formatting

# Display Summary statistics
print(f"Total Score: {total_score}")
print(f"Average Score: {int(average_score) if average_score.is_integer() else average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

# Now we need to run the code using git bash lets open it