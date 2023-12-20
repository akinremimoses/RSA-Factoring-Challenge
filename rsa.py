import sys

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorize(number):
    for i in range(2, number):
        if number % i == 0 and is_prime(i):
            return i, number // i

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize(n)
            print(f"{n}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
