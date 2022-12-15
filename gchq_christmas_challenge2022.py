"""
This is a response to the GCHQ Crhristmas 2022 Quiz,
Coding question:
https://www.gchq.gov.uk/files/The%20GCHQ%20Christmas%20Challenge%202022.pdf
"""

import time
import nltk

# Download the NLTK word corpus
nltk.download('words')
# Create a set of English words
english_words = set(nltk.corpus.words.words())

english_words = [s.upper() for s in english_words]

def is_valid_word(word):
  # Check if the word is in the set of English words
  return word in english_words




def create_formation_grid():
  # Define the word "FORMATION"
  word = "FORMATION"

  # Create a 3x3 grid as a list of lists
  grid = [
    [word[0], word[1], word[2]],
    [word[3], word[4], word[5]],
    [word[6], word[7], word[8]],
  ]

  # Define a dictionary mapping each grid position to a color
  colors = {
    (0, 0): "gold",
    (0, 1): "blue",
    (0, 2): "white",
    (1, 0): "blue",
    (1, 1): "green",
    (1, 2): "gold",
    (2, 0): "blue",
    (2, 1): "gold",
    (2, 2): "green",
  }

  # Create a dictionary mapping each color to a list of letters with that color
  color_letters = {}
  for i, row in enumerate(grid):
    for j, item in enumerate(row):
      color = colors[(i, j)]
      if color not in color_letters:
        color_letters[color] = []
      color_letters[color].append(item)

  # Return the grid and the color_letters
  return grid, color_letters

# Create the grid and the color_letters
grid, color_letters = create_formation_grid()

# Print the color_letters
for color, letters in color_letters.items():
  print(f"{color}: {letters}")



# Define the replacement words
blue_word = "PART"
green_word = "EYES"
gold_word = "UNCURL"

"""
row strings
"""


# Perform some action on the letters with a specific color
color = "blue"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter

    #print(f"Doing something with {letter}")



    try:
        letter_position =   grid[0].index(letter)
    except ValueError:
        #print("Letter not present on this row")
        pass


    counter = 0
    while True:

        grid[0][letter_position] = blue_word[counter]



        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])


        counter += 1


        if is_valid_word(first_row) == True:
            if is_valid_word(sec_row) == True:
                if is_valid_word(thir_row) == True:
                    break


        if counter == 4:
            break






color = "blue"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter

    #print(f"Doing something with {letter}")


    try:
        letter_position =  grid[1].index(letter)
    except ValueError:
        #print("Letter not present on this row")
        pass


    counter = 0
    while True:

        grid[1][letter_position] = blue_word[counter]


        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])


        counter += 1


        if is_valid_word(first_row) == True:
            if is_valid_word(sec_row) == True:
                if is_valid_word(thir_row) == True:
                    break


        if counter == 4:
            break








"""
For I special solution needs cleaning up
"""

color = "blue"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter

    #print(f"Doing something with {letter}")

    if letter == 'I':
        try:
            letter_position =  grid[2].index(letter)
        except ValueError:
            #print("Letter not present on this row")
            pass


    counter = 0
    while True:

        grid[2][0] = blue_word[-1][counter]


        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])


        counter += 1


        if is_valid_word(first_row) == True:
            if is_valid_word(sec_row) == True:
                if is_valid_word(thir_row) == True:
                    break


        if counter == 4:
            break





"""
Green 
"""
color = "green"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter

    #print(f"Doing something with {letter}")


    try:
        letter_position =  grid[1].index(letter)
    except ValueError:
        #print("Letter not present on this row")
        pass


    counter = 0
    while True:
        grid[1][letter_position] = green_word[counter]


        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])


        counter += 1


        if is_valid_word(first_row) == True:
            if is_valid_word(sec_row) == True:
                if is_valid_word(thir_row) == True:
                    break


        if counter == 4:
            break




"""
Green 
"""
color = "green"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter

    #print(f"Doing something with {letter}")


    try:
        letter_position =  grid[2].index(letter)
    except ValueError:
        #print("Letter not present on this row")
        pass


    counter = 0
    while True:
        grid[2][2] = green_word[1]



        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])


        counter += 1


        if is_valid_word(first_row) == True:
            if is_valid_word(sec_row) == True:
                if is_valid_word(thir_row) == True:
                    break


        if counter == 4:
            break









"""
Gold 
"""
color = "gold"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter
    #print(f"Doing something with {letter}")



    try:
        letter_position =  grid[0].index(letter)
    except ValueError:
        #print("Letter not present on this row")
        pass


    counter = 0
    while True:
        grid[0][letter_position] = gold_word[counter]



        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])




        if first_row =='CAR':
            if is_valid_word(first_row) == True:
                if is_valid_word(sec_row) == True:
                    if is_valid_word(thir_row) == True:
                        break

        counter += 1


        if counter == 6:
            break







"""
Gold 
"""
color = "gold"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter

    #print(f"Doing something with {letter}")



    try:
        if letter=='T':
            letter_position =  grid[1].index(letter)
    except ValueError:
        #print("Letter not present on this row")
        pass




    counter = 0
    while True:

        grid[1][2] = gold_word[counter]

        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])


        if first_row =='CAR':
            if is_valid_word(first_row) == True:
                if is_valid_word(sec_row) == True:
                    if is_valid_word(thir_row) == True:
                        break


        counter += 1

        if counter == 6:
            break








"""
Gold 
"""
color = "gold"
if color in color_letters:
  for letter in color_letters[color]:
    # Do something with the letter



    try:
        letter_position =  grid[2].index(letter)

    except ValueError:
        #print("Letter not present on this row")
        pass




    counter = 0
    while True:

        grid[2][1] = gold_word[4]

        first_row = "".join(grid[0])
        sec_row = "".join(grid[1])
        thir_row = "".join(grid[1])



        if is_valid_word(first_row) == True:
            if is_valid_word(sec_row) == True:
                if is_valid_word(thir_row) == True:
                    break


        counter += 1

        if counter == 6:
            break



print('\n')
print("The resulting array is:")
for row in grid:

    print(row)


