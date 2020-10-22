import statistics as st
import matplotlib.pyplot as plt
import numpy as np
import math
import turtle
import seaborn as sns
import pandas as pd

plot_digits = False
digit_count_to_display = 149
digits_to_process = 1000000
turtle_count = 800

file_handle = open('Pi-million-places.txt', 'r')   
file_contents = file_handle.read()
digit_dist = np.zeros((10, 2))
all_digits = np.zeros((digits_to_process, 10))

for i in range(10):
    digit_dist[i][0] = i

count = 0     

for pi_digit in file_contents[:digits_to_process]: 
    if pi_digit.isdigit() == True: 
        int_digit = int(pi_digit)

        digit_dist[int_digit][1] = digit_dist[int_digit][1] + 1
        x = digit_dist[:,1]
        all_digits[count] = x          
        count += 1


df_digit_distribution = pd.DataFrame(data=digit_dist, columns=['Digit', 'Count'])
df_history = pd.DataFrame(data=all_digits)
min_count_index = df_digit_distribution[['Count']].idxmin() 
max_count_index = df_digit_distribution[['Count']].idxmax() 
min_count = df_digit_distribution.min() 
max_count = df_digit_distribution.max()

print('Looking at the first 1 million digits of Pi.')
print(f'The standard deviation for digit counts is {df_digit_distribution.std()[1]:.1f}')
print(f'The digit that appears least is {min_count_index[0]} ({min_count[1]:.0f} times).')
print(f'The digit that appears most is {max_count_index[0]} ({max_count[1]:.0f} times).')

#plt.figure(figsize=(15,8))
#sns.barplot(x='Digit', y='Count', data=df_digit_distribution, palette="Blues_d").set_title('Distribution of digits in Pi')
#plt.show()

plt.figure(figsize=(15,8))
ax = sns.lineplot(data=df_history)
ax.set(xlabel='Number of digits processed', ylabel='Times each digit occurs')
ax.set_title(f'Distribution of first {digits_to_process} digits of Pi')
plt.show()




print(f'The first {digit_count_to_display + 1} digits are 3.{file_contents[:digit_count_to_display + 1]}')

if plot_digits:
    s = turtle.getscreen()
    t = turtle.Turtle()
    t.pensize(2)
    t.speed(10)
    
    for pi_digit in file_contents[:turtle_count]: 
        if pi_digit.isdigit() == True: 
            int_digit = int(pi_digit)
            t.setheading(int_digit * 36)
            #t.pencolor(66,66,66)
            t.forward(10)
    turtle.exitonclick()

