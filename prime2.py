import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

print(f"Prime numbers between {start} and {end} are:")

for i in range(start, end + 1):
    if is_prime(i):
        print(i)