import time

'''Start time'''
start_time = time.time()


'''Read file into list -> list_digits'''


# Request name
# Response list
# Use standard read method
def read_file(name_file: str) -> list:
    # list comprehension
    return [int(i.rstrip()) for i in open(name_file, 'r')]


# Name file for function -> read_file
# File in currently directory
list_digits = read_file(r'10m.txt')


# Max and min digits into list (Use max and min functions)
print(f'Max digits: {max(list_digits)}\nMin digits: {min(list_digits)}')


'''Determining the median (double and odd numbers) of the current list'''


# Request list
# Response int
def median(elements: list) -> int:
    len_list_digits = len(elements)
    middle_digit = len_list_digits // 2

    if len_list_digits % 2 == 0:
        elements.sort()
        return 0.5 * (elements[middle_digit-1] + elements[middle_digit])

    elif len_list_digits % 2 == 1:
        return elements[middle_digit]


print(f'Median: {median(list_digits)}')


'''Determining the arithmetic mean of the current list'''


# Request list
# Response float
# Use loop while
# Determining counter for while and round result
def arithmetic(elements: list) -> float:
    len_list_digits = len(elements)
    sum_digit = 0
    counter = 0

    while counter < len_list_digits:
        sum_digit += elements[counter]
        counter += 1

    return round(sum_digit / len_list_digits, 2)


print(f'Arithmetic: {arithmetic(list_digits)}')


'''Determining the Digits sequence (increasing and decreasing)'''


# Request list and bool
# Response list
# Use loop while
# Determining counter for while and two lists (sequence - current iteration sequence,
# finish - finale iteration sequence (Keep first max sequence into list))
def digits_sequence(elements: list, increasing: bool) -> list:
    counter = 0
    sequence = []
    finish = []

    while counter < len(elements):

        # For increasing
        if increasing:
            if len(sequence) == 0 or elements[counter] > sequence[-1]:
                sequence.append(elements[counter])

            else:
                if len(sequence) > len(finish):
                    finish = sequence.copy()
                sequence = list()
                sequence.append(elements[counter])

        # For decreasing
        else:
            if len(sequence) == 0 or elements[counter] < sequence[-1]:
                sequence.append(elements[counter])

            else:
                if len(sequence) > len(finish):
                    finish = sequence.copy()
                sequence = list()
                sequence.append(elements[counter])

        counter += 1

    return finish


# Result
result_increasing = digits_sequence(list_digits, increasing=True)
result_decreasing = digits_sequence(list_digits, increasing=False)

print('Digits sequence (increasing):', *result_increasing)
print('Digits sequence (decreasing):', *result_decreasing)

'''Finish time'''
end_time = time.time()

'''Total time'''
execution_time = round(end_time - start_time, 2)

print(f'\nTotal time: {execution_time}')