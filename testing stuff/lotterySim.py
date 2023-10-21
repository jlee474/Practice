import random
import time
import os
import multiprocessing

# Clear the console
os.system('cls') # 'cls' for Windows. 'clear' for macOS and Linux

# Define functions
def get_elapsed_time(start_time):
   return time.time() - start_time

def runSim(start_time, start_range, end_range, winning_numbers, winnerFound):
    global counter
    while True:
        playerDraw = random.sample(range(start_range,end_range + 1), 5)
        playerDraw = sorted(playerDraw)
        playerRed = random.randint(1, 26)
        playerDraw.append(playerRed)  # the red Powerball

        # for every 1,000,000 iterations
        if counter % 1000000 == 0:
            print(f"Total random \"tickets\" purchased is {(counter / 1000):,.0f}K. Elapsed time is {get_elapsed_time(start_time):,.2f} seconds")

        if counter == 999999999:
            print(f'max iterations reached of {counter:,}')
            break
        elif playerDraw == winning_numbers:
            print(f"There's a winner!")
            print(f"Player's draw was {playerDraw}")
            print(f"The winning numbers were {winning_numbers}")
            print(f"It took {counter:,.0f} tries")
            winnerFound.put(True) # optional 
            break
        counter += 1

counter = 0

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
    
    num_processes = 10 # number of multiple processes
    winnerFound = multiprocessing.Queue() # optional
    processes = [] # this is a container to hold all the individual process in the multiprocessing application

    start_time = time.time() # start timer for the simulation
    for _ in range(num_processes):
        process = multiprocessing.Process(target=runSim, args=(start_time, start_range, end_range, winning_numbers, winnerFound))
        processes.append(process)
        process.start()

    # Wait for one process to find the occurrence
    found = winnerFound.get() #optional 

    # Terminate the other processes
    for process in processes:
        process.terminate()

###
# to do a shared variable, use multipocessing.Value or multiprocessing.Array , the problem is that it introduces slowdown in speed
###