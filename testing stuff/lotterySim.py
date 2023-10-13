import random
import time
import os

# Clear the console
os.system('cls') # 'cls' for Windows. 'clear' for macOS and Linux

# Define functions
def get_elapsed_time():
   return time.time() - start_time

def runSim(counter):
    while True:
        playerDraw = random.sample(range(start_range,end_range + 1), 5)
        playerDraw = sorted(playerDraw)
        playerRed = random.randint(1, 26)
        playerDraw.append(playerRed)  # the red Powerball

        # for every 100,000 iterations
        if counter % 1000000 == 0:
            print(f"Total random \"tickets\" purchased is {(counter / 1000):,.0f}K. Elapsed time is {get_elapsed_time():,.2f} seconds")

        if counter == 999999999:
            print(f'max iterations reached of {counter:,}')
            break
        elif playerDraw == winning_numbers:
            print(f"There's a winner!")
            print(f"Player's draw was {playerDraw}")
            print(f"The winning numbers were {winning_numbers}")
            print(f"It took {counter:,.0f} tries")
            break
        counter += 1


if __name__ == "__main__":

    # Define the range of numbers from which to draw
    global start_range
    global end_range
    start_range = 1
    end_range = 69

    # Define the winning numbers
    winning_numbers = random.sample(range(start_range, end_range + 1), 5)
    red = random.randint(1, 26)
    winning_numbers = sorted(winning_numbers)
    winning_numbers.append(red)

    ###
    winning_numbers = [1,2,3,4,5,6] # just for curiosity, override winning numbers to chronological sequence
    ###
    
    print(f'The winning numbers to match are {winning_numbers}')
    counter = 1
    start_time = time.time() # start timer for the simulation
    runSim(counter)








'''

can i use parrallel process in python to make a loop run faster?
ChatGPT
Yes, you can use parallel processing in Python to make a loop or any other computational task run faster. Python provides several libraries and modules for parallel programming, with the most commonly used ones being:

multiprocessing: This built-in module allows you to create multiple processes, each of which can execute a loop or a function concurrently. It is useful for CPU-bound tasks, as it takes advantage of multiple CPU cores.

concurrent.futures: This module provides a high-level interface for asynchronously executing functions in separate threads or processes. It is part of the standard library starting from Python 3.2 and is a convenient way to perform parallel processing tasks.

threading: While Python's Global Interpreter Lock (GIL) can limit the effectiveness of multi-threading for CPU-bound tasks, it can still be useful for I/O-bound tasks where threads spend a lot of time waiting for external resources like files or network requests.

Third-party libraries like joblib, ray, or Dask: These libraries offer more advanced parallel processing capabilities and can be used for tasks that require distributed computing or more fine-grained control over parallelism.

Here's a simple example using multiprocessing to parallelize a loop:

python
Copy code
import multiprocessing

def worker_function(start, end):
    for i in range(start, end):
        # Your computation here

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    # Define the range for each process
    ranges = [(0, 1000), (1000, 2000), (2000, 3000)]  # Adjust as needed

    # Use multiprocessing.Pool.map to parallelize the loop
    results = pool.starmap(worker_function, ranges)

    pool.close()
    pool.join()
Keep in mind that parallel processing is most effective for CPU-bound tasks, where the program spends a significant amount of time performing computations. For I/O-bound tasks, you might be better off using asynchronous programming with asyncio or threads, as they can help manage concurrency efficiently. Additionally, you should consider potential synchronization issues and race conditions when working with parallel code.




User
can you convert it to a while loop?
ChatGPT
Certainly! If you want to parallelize a task using a while loop instead of a for loop, you can structure your code accordingly. Here's an example using a while loop with multiprocessing:

python
Copy code
import multiprocessing

def worker_function(start, end):
    while start < end:
        # Your computation here
        start += 1

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    # Define the range for each process
    ranges = [(0, 1000), (1000, 2000), (2000, 3000)]  # Adjust as needed

    # Use multiprocessing.Pool.map to parallelize the while loop
    results = pool.starmap(worker_function, ranges)

    pool.close()
    pool.join()
In this example, the worker_function now uses a while loop with a condition to specify the range of values it should process. The rest of the code remains similar to the previous example, with the multiprocessing.Pool being used to parallelize the execution of the worker_function across multiple processes.

Make sure to adapt the loop condition, range definition, and the actual computation within the worker_function according to your specific use case.




User
can you explain the .starmap method?
ChatGPT
Certainly! In the code examples provided earlier, the .starmap() method is used to parallelize the execution of a function (worker_function) across multiple processes. Let me explain how it works:

.starmap() is a method provided by the multiprocessing.Pool class, which is part of the Python multiprocessing module. It allows you to apply a given function to a sequence of arguments in parallel. Here's how it works:

You create a multiprocessing.Pool object, specifying the number of processes you want to use. This pool of worker processes is responsible for executing your function in parallel.

You define a function (worker_function in this case) that takes arguments. The function should accept multiple arguments as separate parameters, as it will receive the elements of the iterable you pass to .starmap() as separate arguments.

You prepare a list of argument tuples, where each tuple contains the arguments to be passed to worker_function for each parallel execution. In your example, ranges is a list of tuples, where each tuple specifies a range of values for worker_function.

You use .starmap() on the pool object to apply worker_function to the list of argument tuples in parallel. It distributes the work among the available worker processes, passing each tuple as separate arguments to worker_function.

.starmap() returns a list of results, where each element corresponds to the result of applying worker_function to the corresponding argument tuple. These results are collected and returned in the same order as the input tuples.

Finally, you close the pool of worker processes using pool.close() and wait for all processes to complete their work and terminate using pool.join().

In summary, .starmap() is a convenient way to parallelize the execution of a function with multiple sets of arguments. It allows you to take advantage of multiple CPU cores and speed up computations that can be divided into independent tasks.




User
how can I parrallelize the execution of the function without multiple sets of arguments?
ChatGPT
If you want to parallelize the execution of a function without using multiple sets of arguments, you can use the multiprocessing.Pool.map() method instead of multiprocessing.Pool.starmap(). Here's how you can do it:

python
Copy code
import multiprocessing

def worker_function(index):
    # Your computation here
    result = index * 2  # Replace with your actual computation
    return result

if __name__ == "__main__":
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    # Define the range of indices you want to process
    indices = range(0, 1000)  # Adjust as needed

    # Use multiprocessing.Pool.map to parallelize the function execution
    results = pool.map(worker_function, indices)

    pool.close()
    pool.join()
In this example:

The worker_function takes a single argument (index) and performs a computation based on that argument.

Instead of preparing a list of argument tuples, you create a list of indices (indices) that you want to process in parallel. Each index corresponds to a single execution of worker_function.

You use pool.map() to parallelize the execution of worker_function across multiple processes. The indices list is passed as the iterable, and each index is passed as an argument to worker_function in separate parallel executions.

The results of each execution of worker_function are collected in the results list, with each result corresponding to the computation for a specific index.

This approach allows you to parallelize the execution of a function without the need for multiple sets of arguments. Each process in the pool will work on a different index, and you collect the results in the same order as the input indices.


'''
