import numpy as np
import pandas as pd


def process_marks():
    """
    Reads a file containing student marks, processes the data using NumPy and Pandas,
    and outputs results. The user is prompted to input the filename.

    The function performs:
    1. Reading the number of students and coursework weighting.
    2. Loading student data into a Pandas DataFrame.
    3. Computing the overall mark.
    4. Assigning grades based on the computed marks.
    5. Creating a structured NumPy array.
    6. Sorting students by overall mark.
    7. Writing sorted records to an output file.
    8. Printing statistical summaries.
    """
    while True:
        filename = input("Enter the filename containing student marks: ").strip()
        try:
            # Read the first line to get the number of students and coursework weighting
            with open(filename, 'r') as file:
                first_line = file.readline().strip().split()
                num_students, coursework_weight = int(first_line[0]), float(first_line[1])

            # Load student data into Pandas DataFrame using recommended separator
            df = pd.read_csv(filename, sep=r'\s+', skiprows=1, engine='python',
                             names=['RegNo', 'ExamMark', 'CourseworkMark'])

            # Compute overall mark based on exam and coursework weightage
            df['OverallMark'] = (df['ExamMark'] * (1 - coursework_weight / 100)) + \
                                (df['CourseworkMark'] * (coursework_weight / 100))
            df['OverallMark'] = df['OverallMark'].round().astype(int)  # Round overall marks to nearest integer

            # Apply grading rules based on exam, coursework, and overall marks
            df['Grade'] = np.where(
                (df['ExamMark'].round() < 33) | (df['CourseworkMark'].round() < 33),  # Automatic Fail Condition
                'F',  # Assign 'F' if either exam or coursework mark is below 33
                np.select(
                    [
                        df['OverallMark'] >= 70,  # First Class
                        df['OverallMark'].between(50, 69),  # Second Class
                        df['OverallMark'].between(40, 49)  # Third Class
                    ],
                    ['1', '2', '3'],  # Grade Categories
                    default='F'  # Default Fail if below 40
                )
            )

            # Define structured NumPy array data type for efficient storage
            dtype = np.dtype([
                ('RegNo', 'i4'), ('ExamMark', 'i4'), ('CourseworkMark', 'i4'),
                ('OverallMark', 'i4'), ('Grade', 'U2')
            ])

            # Convert DataFrame to a structured NumPy array
            structured_array = np.array(
                list(df.itertuples(index=False, name=None)), dtype=dtype
            )

            # Sort students by overall mark in ascending order
            sorted_array = np.sort(structured_array, order='OverallMark')

            # Write sorted student data to an output file with proper alignment
            output_filename = 'output.txt'
            with open(output_filename, 'w') as f:
                f.write(f"{'RegNo':<10}{'ExamMark':<12}{'CourseworkMark':<15}{'OverallMark':<12}{'Grade':<6}\n")
                f.write("=" * 55 + "\n")  # Print a separator line for better readability
                for row in sorted_array:
                    f.write(
                        f"{row['RegNo']:<10}{row['ExamMark']:<12}{row['CourseworkMark']:<15}{row['OverallMark']:<12}{row['Grade']:<6}\n")

            # Count students in each grade category
            grade_counts = df['Grade'].value_counts().to_dict()
            first_class = grade_counts.get('1', 0)  # Count first-class students
            second_class = grade_counts.get('2', 0)  # Count second-class students
            third_class = grade_counts.get('3', 0)  # Count third-class students
            failed = grade_counts.get('F', 0)  # Count failed students

            # Print grade statistics to the console
            print("\n===== Grade Distribution =====")
            print(f"First Class: {first_class}")
            print(f"Second Class: {second_class}")
            print(f"Third Class: {third_class}")
            print(f"Failed: {failed}")

            # List registration numbers of failed students
            failed_students = df[df['Grade'] == 'F']['RegNo'].tolist()
            if failed_students:
                print(f"Failed Students: {failed_students}")

            print(f"\nResults saved in {output_filename}.")
            break  # Exit loop if file processed successfully

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please try again.")
        except Exception as e:
            print(f"Error processing the file: {e}")


# Run the function
process_marks()