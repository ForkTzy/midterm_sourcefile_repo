def classify_grade(grade):
    """Return the classification and status of a grade based on grading criteria."""
    # Check if the grade falls in the Excellent range (90 to 100)
    if 90 <= grade <= 100:
        return ("Excellent", "Passed")  # Return tuple with category and status
    # Check if the grade falls in the Very Good range (85 to 89)
    elif 85 <= grade <= 89:
        return ("Very Good", "Passed")
    # Check if the grade falls in the Good range (80 to 84)
    elif 80 <= grade <= 84:
        return ("Good", "Passed")
    # Check if the grade falls in the Satisfactory range (75 to 79)
    elif 75 <= grade <= 79:
        return ("Satisfactory", "Passed")
    # Any valid grade below 75 falls under Needs Improvement
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list of dictionaries."""
    students = []  # Initialize an empty list to store valid student dictionaries

    try:
        # Open the file in read mode safely using context manager
        with open(filename, "r") as file:
            # Iterate through each line in the text file
            for line in file:
                # Remove leading and trailing whitespace/newlines
                cleaned_line = line.strip()

                # Skip empty lines or comment lines starting with '#'
                if not cleaned_line or cleaned_line.startswith("#"):
                    continue  # Move to the next line in loop

                # Split the line by comma delimiter into individual fields
                parts = cleaned_line.split(",")

                # Ensure line contains exactly 3 fields (ID, Name, Grade)
                if len(parts) != 3:
                    continue  # Skip invalid lines with missing or extra fields

                # Clean up individual field values
                student_id = parts[0].strip()
                name = parts[1].strip()

                # Try converting the grade string to a floating point number
                try:
                    grade = float(parts[2].strip())
                except ValueError:
                    continue  # Skip records where grade is not numeric (e.g., 'one hundred')

                # Validate that the numeric grade is within the range [0, 100]
                if 0 <= grade <= 100:
                    # Append valid record as a dictionary to the list
                    students.append(
                        {
                            "student_id": student_id,
                            "name": name,
                            "grade": grade,
                        }
                    )

    # Handle missing file error gracefully
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    # Handle general file system errors
    except OSError as e:
        print(f"Error reading file: {e}")

    # Return list containing all valid student records
    return students


def calculate_statistics(students):
    """Calculate class statistics without using sum(), max(), or min()."""
    # Guard clause: return None if list is empty to prevent division by zero
    if not students:
        return None

    # Initialize accumulation and counter variables
    total_grade = 0
    passed_count = 0
    failed_count = 0

    # Set initial highest and lowest records to the first student in list
    highest_student = students[0]
    lowest_student = students[0]

    # Process each student record in the list
    for student in students:
        grade = student["grade"]  # Extract numeric grade
        total_grade += grade  # Accumulate total sum of grades

        # Get status using the classify_grade helper function
        _, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1  # Increment passed counter
        else:
            failed_count += 1  # Increment failed counter

        # Check if current student has a higher grade than current highest
        if grade > highest_student["grade"]:
            highest_student = student  # Update highest student reference

        # Check if current student has a lower grade than current lowest
        if grade < lowest_student["grade"]:
            lowest_student = student  # Update lowest student reference

    num_students = len(students)  # Get total number of valid students
    average = (
        total_grade / num_students
    )  # Calculate mean grade for the class

    # Return computed statistics organized in a dictionary
    return {
        "num_students": num_students,
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student,
    }


def display_students(students):
    """Display all student records in a formatted table layout."""
    # Check if student list has records
    if not students:
        print("No student records available.")
        return

    # Print top divider line
    print("\n" + "=" * 65)
    # Print formatted table header columns
    print(
        f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<8}"
    )
    print("=" * 65)

    # Loop through and display each student row
    for student in students:
        # Unpack tuple into classification and status strings
        classification, status = classify_grade(student["grade"])

        # Truncate long names to 18 chars to keep table aligned properly
        name = student["name"][:18]

        # Print record formatted with left alignment and two decimal places for grade
        print(
            f"{student['student_id']:<12} {name:<20} {student['grade']:<8.2f} {classification:<18} {status:<8}"
        )

    # Print bottom divider line
    print("=" * 65)


def display_statistics(statistics):
    """Display computed class statistics to stdout."""
    # Return if statistics dictionary is empty/None
    if not statistics:
        print("No statistics available.")
        return

    # Print formatted summary output
    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['num_students']}")
    print(
        f"Class average: {statistics['average']:.2f}"
    )  # Formatted to 2 decimals
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(
        f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}"
    )
    print(
        f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}"
    )


def search_student(students, keyword):
    """Return records whose student number or name matches keyword (case-insensitive)."""
    matches = []  # List to accumulate matching records
    clean_keyword = (
        keyword.strip().lower()
    )  # Clean search string and make lowercase

    # Return empty list if user input was empty
    if not clean_keyword:
        return matches

    # Loop through each student to check match condition
    for student in students:
        # Check if keyword exists inside ID or Name (case-insensitive)
        if (
            clean_keyword in student["student_id"].lower()
            or clean_keyword in student["name"].lower()
        ):
            matches.append(student)  # Add matching student to list

    return matches  # Return list of matching student dictionaries


def save_report(students, statistics, filename="grade_report.txt"):
    """Write student records and summary statistics to a text report file."""
    # Ensure there is valid data before attempting to write
    if not students or not statistics:
        print("Cannot save report: No student data available.")
        return

    try:
        # Open file in write mode ("w") which creates or overwrites the file
        with open(filename, "w") as file:
            # Write main title header
            file.write("=========================================\n")
            file.write("       STUDENT GRADE ANALYZER REPORT     \n")
            file.write("=========================================\n\n")

            # Write student details header
            file.write("STUDENT RECORDS:\n")
            file.write("-" * 65 + "\n")
            file.write(
                f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<8}\n"
            )
            file.write("-" * 65 + "\n")

            # Iterate and write each student record to the file
            for student in students:
                classification, status = classify_grade(student["grade"])
                name = student["name"][:18]
                file.write(
                    f"{student['student_id']:<12} {name:<20} {student['grade']:<8.2f} {classification:<18} {status:<8}\n"
                )

            file.write("-" * 65 + "\n\n")

            # Write summary statistics section
            file.write("CLASS STATISTICS:\n")
            file.write("-" * 30 + "\n")
            file.write(
                f"Total Students : {statistics['num_students']}\n"
            )
            file.write(f"Class Average  : {statistics['average']:.2f}\n")
            file.write(f"Passed         : {statistics['passed']}\n")
            file.write(f"Failed         : {statistics['failed']}\n")
            file.write(
                f"Highest Student: {statistics['highest']['name']} ({statistics['highest']['grade']:.2f})\n"
            )
            file.write(
                f"Lowest Student : {statistics['lowest']['name']} ({statistics['lowest']['grade']:.2f})\n"
            )

        print(f"Report successfully saved to '{filename}'.")

    # Handle write permission or IO errors
    except OSError as e:
        print(f"Error saving report file: {e}")


def main():
    """Main program loop controlling menu interaction."""
    # Load valid student records from file at startup
    students = load_students("grades.txt")

    # Exit program early if file is missing or has no valid records
    if not students:
        print("No valid student records were loaded.")
        return

    # Pre-calculate statistics for menu options
    statistics = calculate_statistics(students)

    # Main menu loop
    while True:
        # Print menu options
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        # Get user menu selection and strip whitespace
        choice = input("Enter your choice: ").strip()

        # Route choice 1: Display all student records
        if choice == "1":
            display_students(students)

        # Route choice 2: Display calculated class statistics
        elif choice == "2":
            display_statistics(statistics)

        # Route choice 3: Perform search by keyword
        elif choice == "3":
            keyword = input("Enter student ID or name to search: ")
            matches = search_student(students, keyword)
            if matches:
                print(f"\nFound {len(matches)} matching record(s):")
                display_students(matches)
            else:
                print(f"\nNo records found matching '{keyword}'.")

        # Route choice 4: Save report to text file
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")

        # Route choice 5: Terminate program loop
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break  # Exit the while loop

        # Handle invalid inputs outside 1-5
        else:
            print("Invalid choice. Please select options 1 to 5.")
            continue  # Re-prompt menu display


# Python entry point check
if __name__ == "__main__":
    main()  # Run main function when script is executed directly