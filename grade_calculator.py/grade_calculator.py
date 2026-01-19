"""
Grade Calculator Program
------------------------
This program:
- Takes marks input from the user
- Validates input
- Uses if-elif-else with logical operators
- Applies nested conditions (business rules)
- Displays proper grade messages
"""

def calculate_grade(marks):
    """
    Determines grade based on marks.
    Business rules are simulated using nested conditions.
    """

    # Validate marks range
    if marks < 0 or marks > 100:
        return "❌ Invalid marks! Enter a value between 0 and 100."

    # Business rule: Pass or Fail
    if marks >= 40:
        # Nested grading rules
        if marks >= 90:
            return "🏆 Grade A+ : Outstanding performance"
        elif marks >= 75 and marks < 90:
            return "🎯 Grade A : Excellent work"
        elif marks >= 60 and marks < 75:
            return "👍 Grade B : Good performance"
        else:
            return "✅ Grade C : Passed"
    else:
        # Fail conditions
        if marks >= 35 and marks < 40:
            return "⚠️ Grade D : Borderline fail – improvement needed"
        else:
            return "❌ Grade F : Failed"


def main():
    """
    Main function to take input and display results.
    Handles invalid input using error handling.
    """
    try:
        marks = float(input("Enter student marks (0–100): "))
        result = calculate_grade(marks)
        print(result)
    except ValueError:
        print("❌ Invalid input! Please enter numeric marks only.")


# Program execution starts here
if __name__ == "__main__":
    main()
