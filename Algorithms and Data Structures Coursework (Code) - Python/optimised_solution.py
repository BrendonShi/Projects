"""
This program takes an input of binary string and extracting substrings,
checks if a number is prime and then sorting the result.
The final result will be fewer than 6 prime numbers.
Using set() as a data structure.
"""


def is_prime(n):
    """
    prime-checking function using 6k ± 1 method
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:  # eliminating multiples of 2 and 3
        return False
    if n < 9:
        return True
    k, limit = 5, int(n ** 0.5) + 1  # starting to check from 5 up to the square root of n
    while k <= limit:
        if n % k == 0 or n % (k + 2) == 0:  # 6k + 1 method to check divisibility
            return False
        k += 6  # adding 6 to check the pair of divisors
    return True  # if no divisors


def extract_binary_substrings(binary_string):
    """ extracts all possible decimal values from given binary substrings """
    if any(c not in '01' for c in binary_string):  # checks if the string contains only '0' or '1'
        return None

    substrings = set()  # store decimal values
    length = len(binary_string)
    for i in range(length):
        decimal = 0  # Decimal equivalent
        for j in range(i, length):
            # converting binary -> decimal
            decimal = (decimal << 1) | int(binary_string[j])  # binary-to-decimal conversion by moving bits to the left
            substrings.add(decimal)  # adding the decimal value to the set
    return substrings


def main_primes(binary_str, n):
    """ main function to find and format prime numbers in binary substrings """
    binary_substrings = extract_binary_substrings(binary_str)
    if binary_substrings is None:
        return "0: Invalid binary strings"

    # extracting prime numbers that are less than 'n' and are prime.
    prime_numbers = {num for num in binary_substrings if num < n and is_prime(num)}
    if not prime_numbers:
        return "0: No prime numbers found"

    sorted_primes = sorted(prime_numbers)  # sorting the prime numbers
    total_primes = len(sorted_primes)  # counting the total number of prime numbers
    if total_primes < 6:  # if it's less than 6 - return ALL prime numbers
        return f"{total_primes}: {', '.join(map(str, sorted_primes))}"
    else:  # if it's greater than 6, return the first 3 and the last 3
        return f"{total_primes}: {', '.join(map(str, sorted_primes[:3] + sorted_primes[-3:]))}"


def main(binary_string, n):
    import time
    print("Running main function...")
    start = time.time()
    print(main_primes(binary_string, n))
    end = time.time()
    print("Finished!")
    print(f"Time taken: {end - start:.6f} seconds\n")

# Test Cases:
print("Test 1:")  # Time taken: 0.000000 seconds
main("0100001101001111",999999)
print("Test 2:")  # Time taken: 0.000000 seconds
main("01000011010011110100110101010000",999999)
print("Test 3:")  # Time taken: 0.000000 seconds
main("1111111111111111111111111111111111111111",999999)
print("Test 4:")  # Time taken: 0.000915 seconds
main("010000110100111101001101010100000011000100111000",999999999)
print("Test 5:")  # Time taken: 0.004991 seconds
main("01000011010011110100110101010000001100010011100000110001",123456789012)
print("Test 6:")  # Time taken: 0.289093 seconds
main("0100001101001111010011010101000000110001001110000011000100111001",123456789012345)
print("Test 7:")  # Time taken: 5.903836 seconds
main("010000110100111101001101010100000011000100111000001100010011100100100001",123456789012345678)
print("Test 8:")  # Time taken: 8.271338 seconds
main("01000011010011110100110101010000001100010011100000110001001110010010000101000001",1234567890123456789)
print("Test 9:")  # Time taken: 21.014816 seconds
main("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100",1234567890123456789)
print("Test 10:")  # Time taken: 27.014466 seconds
main("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011",12345678901234567890)



# Test 8:
# Running main function...
# 76: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977
# Finished!
# Time taken: 8.223736 seconds
#
# Test 9:
# Running main function...
# 81: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661
# Finished!
# Time taken: 21.437753 seconds
#
# Test 10:
# Running main function...
# 89: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661
# Finished!
# Time taken: 27.733648 seconds