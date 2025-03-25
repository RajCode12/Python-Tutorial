try:
    print(5/0)
except Exception as e:
    print(e)

lst = [1,2,3]
try:
    print(list[3])
except IndexError as e:
    print(e)

numbers = []
while True:
    try:
        num = int(input("Enter an integer (or 0 to stop): "))
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print(numbers)