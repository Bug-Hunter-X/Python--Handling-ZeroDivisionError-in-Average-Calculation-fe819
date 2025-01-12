def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Additional test cases
my_list2 = [10,20,30,40,50]
average2 = calculate_average(my_list2)
print(f"The average is: {average2}")

my_list3 = []
average3 = calculate_average(my_list3)
print(f"The average of an empty list is: {average3}")
