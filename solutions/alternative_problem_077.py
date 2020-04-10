# Problem 77
#
# This problem was asked by Snapchat.
#
# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
#
# The input list is not necessarily ordered in any way.
#
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

print("Merge Overlapping Intervals")


def get_interval_start(e):
    return e[0]


def merge_intervals(interval_list):
    interval_list.sort(key=get_interval_start)
    merged_intervals = []
    merged_intervals.append(interval_list[0])
    for idx, item in enumerate(interval_list[1:]):
        if merged_intervals[-1][1] < item[0]:
            merged_intervals.append(item)
        elif merged_intervals[-1][1] < item[1]:
            merged_intervals[-1][1] = item[1]
    return merged_intervals


assert merge_intervals([[1, 3], [5, 8], [4, 10], [20, 25]]) == [
    [1, 3], [4, 10], [20, 25]]
assert merge_intervals([[1, 3], [5, 8], [4, 10], [20, 25], [6, 12]]) == [
    [1, 3], [4, 12], [20, 25]]
