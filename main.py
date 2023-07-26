import time
from manage_file import asc, dec, rand, saved
from quick_sort import quick_sort
from upgrade_quick import upgrade_quick

M = 1000000

filename = "num_arr.txt"

# 파일 생성 (순차, 역방향, 랜덤) 

# asc(filename)
# dec(filename)
rand(filename)

with open(filename) as inFile:
    integers = [int(num) for num in inFile]

sorting_arr = integers

# my quick sort
integers = sorting_arr.copy()
start_time = time.time()
quick_sort(integers, 0, M - 1)
end_time = time.time()

total_time = end_time - start_time
print(f"My quick sort time: {total_time} seconds.")
saved("after_my_quick.txt", integers)

# upgrade quick sort
integers = sorting_arr.copy()
start_time = time.time()
upgrade_quick(integers, 0, M - 1)
end_time = time.time()

total_time = end_time - start_time
print(f"Upgrade quick sort time: {total_time} seconds.")
saved("after_upgrade_quick.txt", integers)


# sort method
integers = sorting_arr.copy()
start_time = time.time()
integers.sort()
end_time = time.time()

total_time = end_time - start_time
print(f"sort method time: {total_time} seconds.")
saved("after_sort_method.txt", integers)


# sorted function 
integers = sorting_arr.copy()
start_time = time.time()
integers =sorted(integers)
end_time = time.time()

total_time = end_time - start_time
print(f"sorted function time: {total_time} seconds.")

saved("after_sorted_func.txt", integers)