import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
import pandas as pd
import pygame

# Changing these values will determine what happens later.
plot_digits = False
digit_count_to_display = 769
digits_to_process = 1000
turtle_count = 20000
plot_distribution = False
pi_is_running = False
screen_width = 1600
screen_height = 1200
line_length = 4

file_handle = open('Pi-million-places.txt', 'r')   
file_contents = file_handle.read()
digit_dist = np.zeros((10, 2))  # Holds the number of times each digit occurs.
all_digits = np.zeros((digits_to_process, 10))  # Holds the full history of each digit's occurence.

for i in range(10):
    digit_dist[i][0] = i

count = 0     

# Iterate through the first digits_to_process digits of Pi.
for pi_digit in file_contents[:digits_to_process]: 
    if pi_digit.isdigit() == True: 
        int_digit = int(pi_digit)

        # Update the distribution of each digit.
        digit_dist[int_digit][1] = digit_dist[int_digit][1] + 1
        # And record the history of each digit.
        totals_column = digit_dist[:,1]
        all_digits[count] = totals_column          
        count += 1

df_digit_distribution = pd.DataFrame(data=digit_dist, columns=['Digit', 'Count'])
df_history = pd.DataFrame(data=all_digits)

print('Looking at the first 1 million digits of Pi.')
print(f'The digit zero appears {digit_dist[0][1]:.0f} times.')
print(f'The digit 1 appears {digit_dist[1][1]:.0f} times.')
print(f'The digit 2 appears {digit_dist[2][1]:.0f} times.')
print(f'The digit 3 appears {digit_dist[3][1]:.0f} times.')
print(f'The digit 4 appears {digit_dist[4][1]:.0f} times.')
print(f'The digit 5 appears {digit_dist[5][1]:.0f} times.')
print(f'The digit 6 appears {digit_dist[6][1]:.0f} times.')
print(f'The digit 7 appears {digit_dist[7][1]:.0f} times.')
print(f'The digit 8 appears {digit_dist[8][1]:.0f} times.')
print(f'The digit 9 appears {digit_dist[9][1]:.0f} times.')
print(f'The standard deviation for digit counts is {df_digit_distribution.std()[1]:.1f}')
print(f'The first {digit_count_to_display + 1} digits are 3.{file_contents[:digit_count_to_display + 1]}')

if plot_distribution:
    plt.figure(figsize=(15,8))
    ax = sns.lineplot(data=df_history)
    ax.set(xlabel='Number of digits processed', ylabel='Times each digit occurs')
    ax.set_title(f'Distribution of first {digits_to_process} digits of Pi')
    plt.show()

# Visualise the digits of Pi as a turtle drawing.
if plot_digits:
    pen_colours = [[255, 241, 0],[255, 140, 0],[232, 17, 35],[236, 0, 140],
                  [104, 33, 122],[0, 24, 143],[0, 188, 242],[0, 178, 148],
                  [0, 158, 73],[186, 216, 10]]
    
    for pi_digit in file_contents[:turtle_count]: 
        if pi_digit.isdigit() == True: 
            int_digit = int(pi_digit)
            t.setheading(int_digit * 36)
            t.pencolor(pen_colours[int_digit])
            t.forward(3)
    turtle.exitonclick()

# Get a screen context and create the initial setup.
grid_display = pygame.display.set_mode((screen_width, screen_height))
mid_point = ()
digit_pos = 0
previous_point = (screen_width//2, screen_height-400)

pen_colours = [[255, 241, 0],[255, 140, 0],[232, 17, 35],[236, 0, 140],
              [104, 33, 122],[0, 24, 143],[0, 188, 242],[0, 178, 148],
              [0, 158, 73],[186, 216, 10]]

while True:
    # Handle application interrupts - effectively mouse and keyboard input.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            key_pressed = pygame.key.name(event.key).upper()
 
            # React to specified keys.
            if key_pressed == 'P':
                pi_is_running = not pi_is_running

    if pi_is_running:
        
        int_digit = int(file_contents[digit_pos])
        
        # Calculate the destination for the line.
        angle = 36 * int_digit
        angle = math.radians(angle)
        new_x = line_length * math.sin(angle) + previous_point[0]
        new_y = line_length * math.cos(angle) + previous_point[1]
        new_point = (new_x, new_y)
        pen = pen_colours[int_digit]
        
        # print(digit_pos)

        # Draw the line.
        pygame.draw.line(grid_display, pen, previous_point, new_point, 1)
        digit_pos += 1
        previous_point = new_point

    pygame.display.update()

