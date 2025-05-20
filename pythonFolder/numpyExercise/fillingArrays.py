import numpy as np

a = np.full((2, 3, 4), 9) # 2, 3, 4 is the shape of the array, and we fill the dots of the array with 9
# One can see this as a way to instantiate an array with a certain shape
print(a)

b = np.zeros((10, 5, 2)) #  fill with zeros
print(b)

c = np.ones((10, 5, 2)) # fill with ones
print(c)

d = np.empty((10, 5, 2)) # fill with random values, instantiate an array without putting values to be quicker
print(d)

x_values = np.arange(0, 10, 0.5) # I wanna have values from zero to 10 with a step of 0.5 SPECIFY STEPS
print(x_values)

y_values = np.linspace(0, 10, 20) # I wanna have 20 values from zero to 10 SPECIFY AMOUNT
print(y_values)

numbers = np.random.randint(100, size=(2,3,4)) # fill with random integers
print(numbers)

numbs2 = np.random.randint(90, 100, size=(2,3,4)) # fill with random integers between 90 and 100
print(numbs2)

numbs3 = np.random.binomial(100, 0.5, size=(2,3,4)) # fill with binomial distribution
print(numbs3)

numbs4 = np.random.normal(0, 1, size=(2,3,4)) # fill with normal distribution
print(numbs4)

numbs5 = np.random.choice([1, 2, 3, 4, 5], size=(2,3,4)) # fill with random choices
print(numbs5)

np.save("filename", numbs5) # save the array to a file
numbs6 = np.load("filename.npy")
print(numbs6)

np.savetxt("filename.txt", np.random.normal(0, 1, size=(2,3))) # save the array to a text file
txtFile = np.loadtxt("filename.txt")
print(txtFile)