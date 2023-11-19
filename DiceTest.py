import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
ROLLING_DURATION = 2  # in seconds

# Rolling phase
rolling_start_time = time.time()
rolling_end_time = rolling_start_time + ROLLING_DURATION

while time.time() < rolling_end_time:
    # Print random numbers during rolling
    random_number = random.randint(1, 20)
    print(f"Rolling... {random_number}")
    time.sleep(0.1)  # Adjust sleep time to control the rolling speed

# Display final result
print(f"Final Result: {random_number}")

# Quit the game
pygame.quit()
sys.exit()
