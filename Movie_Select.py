import random
import os


# Open MovieList.txt file from folder
# Filepath should be universal and should be located under the same folder
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = os.path.join(__location__, 'MovieList.txt')

# Create an array to store movie names into a list
mLArray = []

# First, check if file exists and is open
# Then, store file as variable 'movieList' and append each movie's name into mLArray
with open(file) as movieList:
    for line in movieList:
        mLArray.append(line)

""" # Print the array in from the text file for debugging purposes
print(mLArray) """

# Keep count of how many movies are in the list
count = 0
for line in mLArray:
    count += 1

# Print how many movies are in the list
print("Number of movies: " + str(count))

# Randomly Select Movie From List
movieSelect = random.choice(mLArray)

# Print the Movie that has been selected
print("The Movie we are going to watch today is " + movieSelect + ".")