n = input("Enter the number of prime numbers you want to print: ")
if n.isdigit():
    n = int(n)
    if n <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        x = 0
        y = 2
        primes = []
        while x < n:
            is_prime = True
            for i in range(2, int(y ** 0.5) + 1):
                if y % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(y)
                x += 1
            y += 1
        
        print("First", n, "prime numbers are:", primes)
else:
    print("Invalid input. Please enter a valid integer.")
