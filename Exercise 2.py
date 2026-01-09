def is_prime(n):
    """Determine whether a given number is prime by testing divisibility rules."""
    if n < 2:
        return False  # Any number less than 2 is not a prime number

    if n == 2:
        return True  # 2 is the smallest and only even prime number

    if n % 2 == 0:
        return False  # All other even numbers are not prime since they are divisible by 2

    # Check divisibility for odd numbers only, up to the square root of n
    # This works because any composite number n must have a factor ≤ √n
    for num in range(3, int(n ** 0.5) + 1, 2):  # Start from 3 and check only odd numbers
        if n % num == 0:
            return False  # If divisible by any number in this range, it's not prime

    return True  # If no divisors were found, the number is prime


def find_primes_in_range(start, end):
    """Generate a list of prime numbers between the given start and end values, inclusive."""
    # Ensure the provided range is in ascending order to handle any input sequence
    start, end = min(start, end), max(start, end)

    # Iterate through the range and store prime numbers in a list using list comprehension
    return [num for num in range(start, end + 1) if is_prime(num)]


def get_valid_input():
    """Prompt the user to enter two positive integers and ensure input validation."""
    try:
        numbers = input("Enter two positive integers separated by space: ")  # Request user input

        # Split the input and convert it into integer values
        a, b = map(int, numbers.split())

        # Validate that both numbers are positive integers
        if a < 1 or b < 1:
            print("Error: Both numbers must be positive integers greater than zero.")
            return None, None  # Return None if input is invalid

        return a, b  # Return the valid numbers
    except ValueError:
        print("Error: Invalid input. Please enter two valid positive integers.")
        return None, None  # Handle cases where input is not an integer


def display_primes(prime_numbers):
    """Format and print the list of prime numbers, displaying 10 numbers per line."""
    if not prime_numbers:
        print("No prime numbers found in the given range.")
        return  # Stop execution if no prime numbers are found

    print("Prime numbers in the given range:")

    # Iterate through the prime numbers and print them in batches of 10 for readability
    for i in range(0, len(prime_numbers), 10):
        print(" ".join(map(str, prime_numbers[i:i + 10])))  # Convert numbers to strings and format output


def main():
    """Main function to retrieve input, find prime numbers, and display results."""
    num1, num2 = get_valid_input()  # Prompt user for input and validate it

    # Execute only if valid numbers were entered
    if num1 is not None and num2 is not None:
        primes = find_primes_in_range(num1, num2)  # Compute prime numbers within the given range
        display_primes(primes)  # Output the results in a structured format


# Ensure the script only runs when executed directly
if __name__ == "__main__":
    main()  # Execute the main function to start the program
