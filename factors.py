import sys

def factorize(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return i, number // i
    return number, 1

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
