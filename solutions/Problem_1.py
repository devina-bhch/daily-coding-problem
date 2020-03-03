"""
Problem 1

Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import time

num_list = [11, 15, 3, 6, 7]
k = 17

def check_sum(num_list, k):
    for i, num in enumerate(num_list[:-1]):
        complementary = k - num
        if complementary in num_list[i + 1:]:
            print(f"complimentary numbers: {num} and {complementary}")
            return True
    return False

#github solution
def check_sum_github(array, k):
    potential_solutions = set()
    for num in array:
        if num in potential_solutions:
            return True
        potential_solutions.add(k - num)

    return False

if __name__ == '__main__':
    start = time.time()
    print(check_sum(num_list, k))
    end = time.time()
    print((end - start) * 1000) #~0.039ms
    start = time.time()
    print(check_sum_github(num_list, k))
    end = time.time()
    print((end - start)*1000) #~.006ms
