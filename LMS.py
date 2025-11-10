def process_list(numbers):
    numbers.append(100)
    print("Inside function:", numbers)

data = [1, 2, 3]
process_list(data)
print("Outside function:", data)
