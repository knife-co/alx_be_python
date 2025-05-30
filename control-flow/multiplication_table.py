number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    new_num = number * i
    print(f"{number} * {i} = {new_num}")
