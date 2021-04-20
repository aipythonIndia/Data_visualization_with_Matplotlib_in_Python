#!/usr/bin/env python
# coding: utf-8



import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y_data = [1, 4, 9, 16, 25]
plt.plot(x_data, y_data, '--r') # Line formatting
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ### Line formatting example [line][color] - Part 2


import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y_data = [1, 4, 9, 16, 25]
plt.plot(x_data, y_data, '-.g') # Line formatting
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()





