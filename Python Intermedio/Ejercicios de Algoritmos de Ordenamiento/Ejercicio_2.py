def bubble_sort(numbers):

    length = len(numbers)

    for i in range(length):

        for j in range(length - 1, 0, -1):

            if numbers[j] < numbers[j - 1]:

                temp = numbers[j]
                numbers[j] = numbers[j - 1]
                numbers[j - 1] = temp

    return numbers


nums = [1, 2, 3, 4, 5, 9, 6, 8, 7]

print(bubble_sort(nums))