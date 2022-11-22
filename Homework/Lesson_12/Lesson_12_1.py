import concurrent.futures
import time


def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


def compare_thread_process_executors(max_workers=10, fact_range=range(1, 11)):
    start_time1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        nums = [executor.submit(factorial, num) for num in fact_range]
        for future in concurrent.futures.as_completed(nums):
            future.result()
    thread_pool_time = time.time() - start_time1

    start_time2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        nums = [executor.submit(factorial, num) for num in fact_range]
        for future in concurrent.futures.as_completed(nums):
            future.result()
    process_pool_time = time.time() - start_time2

    if thread_pool_time < process_pool_time:
        print(f'The execution time of ThreadPoolExecutor is {thread_pool_time} and ProcessPoolExecutor is {process_pool_time}',
              'ThreadPoolExecutor takes less time', sep='\n')
    else:
        print(f'The execution time of ThreadPoolExecutor is {thread_pool_time} and ProcessPoolExecutor is {process_pool_time}',
              'ProcessPoolExecutor takes less time', sep='\n')


if __name__ == '__main__':
    compare_thread_process_executors()