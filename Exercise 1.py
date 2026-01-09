from datetime import date, datetime


# Main function to handle user input, validation, and output

def main():
    """
    Step 1: Gathering User Input
    - Prompts the user to enter their birthdate in the format mm/dd/yyyy.
    - Example: Input "03/25/2022" corresponds to March 25, 2022.
    - The input is taken as a string and converted to a date object.
    """
    dob_str = input("Please enter your birth date (mm/dd/yyyy): ")  # Request user input

    try:
        """
        Step 2: Date Validation
        - Parses the input to confirm it follows mm/dd/yyyy format.
        - Ensures the date is valid (e.g., prevents entries like 02/30/2022).
        - Raises an exception if the format is incorrect or the date does not exist.
        """

        dob = datetime.strptime(dob_str, "%m/%d/%Y").date()  # Convert input string to date

        # Retrieve today's date for age calculation
        today = date.today()

        """
        Step 3: Computing Age
        - Extracts year, month, and day from the entered birthdate and current date.
        - Compares the birth month and day with today's date to determine if the birthday has passed.
        - If the birthday has already occurred this year, the age is (current year - birth year).
        - If the birthday is upcoming, subtracts one from the calculated age.
        """
        age = today.year - dob.year  # Initial age calculation

        # Adjust age if the birthday has not yet occurred this year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1  # Reduce age by one if the birthday has not passed

        # Display the calculated age
        print(f"As of today, you are {age} years old.")

        """
        Step 4: Formatting and Displaying Date
        - Converts the American date format (mm/dd/yyyy) into the European format (dd/mm/yyyy).
        - Ensures day and month are displayed with two digits.
        """
        european_format = f"{dob.day:02}/{dob.month:02}/{dob.year}"  # Reformat date
        print(f"For reference, your birth date in European format is: {european_format}")

    except ValueError:
        """
        Step 5: Error Handling
        - If the input does not follow the correct format or contains an invalid date, an error is raised.
        - Displays an error message asking the user to re-enter a properly formatted date.
        """
        print("Invalid input detected. Please enter your birth date correctly in mm/dd/yyyy format.")  # Error message


# Execute the main function when the script runs
if __name__ == "__main__":
    main()  # Start program execution
