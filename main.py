import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import math
import turtle
import seaborn as sns
import pandas as pd

# Changing these values will determine what happens later.
plot_digits = True
digit_count_to_display = 769
digits_to_process = 1000
turtle_count = 800
plot_distribution = False

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
        x = digit_dist[:,1]
        all_digits[count] = x          
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
    s = turtle.getscreen()
    t = turtle.Turtle()
    t.pensize(2)
    t.speed(10)
    s.colormode(255)
    
    for pi_digit in file_contents[:turtle_count]: 
        if pi_digit.isdigit() == True: 
            int_digit = int(pi_digit)
            t.setheading(int_digit * 36)
            t.pencolor(34, 56, 98)
            t.forward(10)
    turtle.exitonclick()

