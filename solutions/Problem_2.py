# Problem 2
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
import time

# input = [1, 2, 3, 4, 5]
input = [3, 2, 1]

def get_result():
    output = []
    product = 1
    for item in input:
        product = product*item
    for item in input:
        output.append(product//item)
    return output

def get_result_without_div():
    output = []
    for idx, item in enumerate(input):
        input_cp = input.copy()
        input_cp.pop(idx)
        product = 1
        for item in input_cp:
            product = product * item
        output.append(product)
    return output


if __name__ == '__main__':
    start = time.time()
    print(get_result()) #with division
    end = time.time()
    print((end - start) * 1000) #~0.039ms
    start = time.time()
    print(get_result_without_div())
    end = time.time()
    print((end - start) * 1000) #~0.014ms