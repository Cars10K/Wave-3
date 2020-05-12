
factor = int(input("Please enter an interger (2 or greater):"))
n = 2

print("The prime factors of", factor, "are:")
while n*n <= factor:
    if factor % n:
        n += 1
    else:
        factor //=n
    print(n)
if n <= 2:
    print("None")