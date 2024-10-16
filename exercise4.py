# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get a positive integer from the user
num = int(input("Enter a positive integer: "))

# Store prime numbers less than the integer in a list
prime_numbers = [i for i in range(2, num) if is_prime(i)]

# Print the list of prime numbers
print("Prime numbers less than", num, ":", prime_numbers)