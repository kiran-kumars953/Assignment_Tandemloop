a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1
result = [2 * i - 1 for i in range(1, a + 1, 2)]
print(", ".join(map(str, result)))
