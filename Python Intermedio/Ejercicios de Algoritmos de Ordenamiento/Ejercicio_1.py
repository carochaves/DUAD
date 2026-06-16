def bubble_sort(numbers):

    length = len(numbers)

    for i in range(length):

        for j in range(length - 1):

            if numbers[j] > numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


nums = [5, 3, 8, 4, 2]

print(bubble_sort(nums))