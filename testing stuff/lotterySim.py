import random
import time
import os

# Clear the console
os.system('cls') # 'cls' for Windows. 'clear' for macOS and Linux

# Define functions
def get_elapsed_time():
   return time.time() - start_time

# Define the range of numbers from which to draw
start_range = 1
end_range = 69

# Define the winning numbers
winning_numbers = random.sample(range(start_range, end_range + 1), 5)
red = random.randint(1, 26)
winning_numbers = sorted(winning_numbers)
winning_numbers.append(red)
print(f'The winning numbers to match are {winning_numbers}')

# Now for the player draws 
counter = 1
start_time = time.time() # start timer for the simulation


while True:
   playerDraw = random.sample(range(start_range,end_range + 1), 5)
   playerDraw = sorted(playerDraw)
   playerRed = random.randint(1, 26)
   playerDraw.append(playerRed)  # the red Powerball

   # for every 100,000 iterations
   if counter % 100000 == 0:
      print(f"counter is {(counter / 1000):,.0f}K. Elapsed time is {get_elapsed_time():,.2f} seconds")

   if counter == 1000000000:
      print(f'max iterations reached of {counter:,}')
      break
   elif playerDraw == winning_numbers:
      print(f"There's a winner!")
      print(f"Player's draw was {playerDraw}")
      print(f"The winning numbers were {winning_numbers}")
      print(f"It took {counter} tries")
      break
   counter += 1

