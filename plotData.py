#This file reads the numbers from data.txt and plots them

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

#open the data.txt file and read the contents
file = open("data.txt","r")

#Convert data.txt to one long string
dataString = file.read()

#Copy the data from the string into a list
dataList = dataString.split(" ")
dataList.pop()

#initialize a list
myx = []

#Convert the string elements to float elements and add them to our new list
for i in range(0, len(dataList)):
    myx.append(float(dataList[i]))

# create histogram of our data
n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

# plot formating options
ax = plt.subplot()
ax.legend((["Random Distribution"]),loc="upper left",shadow=True)
plt.xlabel('Random Number from 0 to 1',fontweight="bold")
plt.ylabel('Probability',fontweight="bold")
plt.title("Uniform random number",fontweight="bold")
plt.grid(True)

# show figure (program only ends once closed
plt.show()

#Close the file
file.close()
