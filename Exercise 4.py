import os  # Import OS module for handling file operations


def filter_employees(employee_list, salary1, salary2):
    """
    Filters employees based on a specified salary range and displays the results.

    Args:
        employee_list (list): A list of tuples, where each tuple contains (name, job title, salary).
        salary1 (int): First salary value input by the user (can be lower or higher than salary2).
        salary2 (int): Second salary value input by the user.

    Returns:
        None: Outputs the filtered employees in a formatted table.
    """
    min_salary, max_salary = min(salary1, salary2), max(salary1, salary2)  # Determine correct salary range

    # Filter e mployees whose salary is within the given range
    filtered = [emp for emp in employee_list if min_salary <= emp[2] <= max_salary]

    if not filtered:
        print("\nNo employees found in the specified salary range.")  # Display message if no matches found
        return

    filtered.sort(key=lambda x: x[2], reverse=True)  # Sort results by salary in descending order

    # Print table header for better readability
    print("\nFiltered Employee List:")
    print(f"{'Name':<20} {'Job Title':<15} {'Salary':>10}")
    print("=" * 50)

    # Print employee details with aligned formatting
    for name, job, salary in filtered:
        print(f"{name:<20} {job:<15} {salary:>10}")


def read_employee_data(file_path):
    """
    Reads employee data from a specified file and converts it into a list of tuples.

    Args:
        file_path (str): The file location containing employee data.

    Returns:
        list: A list of tuples in the format (name, job title, salary).
    """
    employee_list = []  # Initialize list to store employee data

    try:
        with open(file_path, "r") as file:  # Open file in read mode
            for line in file:
                name, job, salary = map(str.strip, line.strip().split(','))  # Strip whitespace and split by commas
                employee_list.append((name, job, int(salary)))  # Store as tuple in list
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")  # Handle missing file scenario
    except IOError:
        print(f"Error: Unable to read the file '{file_path}'. Check file permissions.")  # Handle file read errors
    except Exception as e:
        print(f"Unexpected error encountered: {e}")  # Catch any unforeseen errors

    return employee_list  # Return the processed list


def main():
    """
    Main function that prompts the user for a filename and processes employee data accordingly.
    """
    while True:
        file_name = input("Enter the filename containing employee data: ").strip()  # Prompt user for file
        if os.path.exists(file_name):  # Validate file existence
            break
        print("File not found. Please enter a valid filename.")  # Request valid filename

    employees = read_employee_data(file_name)  # Load employee data from file
    if not employees:
        print("No valid data found in the file.")  # Exit if file is empty or incorrect
        return

    # Print loaded employee data in unformatted list form (as per the requirement)
    print("\nLoaded Employee Data:")
    print(employees)

    while True:
        try:
            salary1 = int(input("\nEnter first salary value: "))  # Request first salary range input
            salary2 = int(input("Enter second salary value: "))  # Request second salary range input

            if salary1 < 0 or salary2 < 0:
                print("Salary values must be non-negative. Try again.")  # Validate input
                continue

            filter_employees(employees, salary1, salary2)  # Call function to filter results
        except ValueError:
            print("Invalid input! Please enter numeric salary values.")  # Handle non-numeric input

        choice = input("\nDo you want to filter another range? (yes/no): ").strip().lower()  # User decision
        if choice not in ('yes', 'y'):
            print("Thank you for using the Employee Salary Filter. Exiting now. Goodbye!")  # Exit message
            break


if __name__ == "__main__":
    main()  # Run main function when script is executed directly
