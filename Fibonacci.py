def fibonacci_sequence(n):
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result

try:
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(fibonacci_sequence(n))
except ValueError:
    print("Please enter a valid integer.")

# Display the results with addition information
for i, num in enumerate(fibonacci_sequence(n)):
    if i == 0:
        print("(0 + 0): {:>8} ".format(num))
    elif i == 1:
        print("(0 + 1): {:>8} ".format(num))
    else:
        print("({} + {}): {:>8}".format(fibonacci_sequence(n)[i-1], fibonacci_sequence(n)[i-2], num))
