import time
start_time = time.time()
for i in range(1000000):
    solution(5, (19, 15, 28))

end_time = time.time()
total_time = end_time - start_time
print(f"Total 1 time taken: {total_time:.2f} seconds")

start_time = time.time()
for i in range(1000000):
    solution2(5, (19, 15, 28))

end_time = time.time()
total_time = end_time - start_time
print(f"Total 2 time taken: {total_time:.2f} seconds")


start_time = time.time()
for i in range(1000000):
    solution3(5, (19, 15, 28))

end_time = time.time()
total_time = end_time - start_time
print(f"Total 3 time taken: {total_time:.2f} seconds")