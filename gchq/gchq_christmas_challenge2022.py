"""
This is a response to the GCHQ Crhristmas 2022 Quiz,
Coding question:
https://www.gchq.gov.uk/files/The%20GCHQ%20Christmas%20Challenge%202022.pdf
"""

import time
import os
import enchant
from english_words import english_words_alpha_set




def is_valid_uk_english_word(word):
    """
    Checks if a string is a valid english word
    """
    dictionary = enchant.Dict("en_UK")

    return dictionary.check(word)





def find_possible_words_blue_row_one(word, string):
    """
    Finds possible words
    """
    dictionary = enchant.Dict("en_UK")

    possible_words = []

    for char in string:
        new_word = word[0] + char + word[2:]
        if dictionary.check(new_word):
            possible_words.append(new_word)

            return possible_words




def find_possible_words_blue_row_two(word, string):
    """
    Finds possible words
    """
    dictionary = enchant.Dict("en_UK")

    possible_words = []

    for char in string:
        new_word = char+ word[1:]
        if dictionary.check(new_word):

            possible_words.append(new_word)
            return possible_words





def find_possible_words(word, string):
  # Use the enchant library to create a dictionary object
  dictionary = enchant.Dict("en_UK")

  # Open a list to store the possible words
  possible_words = []

  # Iterate through the characters in the string
  for char in string:
    # Create a new word by replacing the second character of the original word with the current character
    new_word = char+ word[1:]


    # Check if the new word is a valid English word
    if dictionary.check(new_word):
      # If it is, add it to the list of possible words
      possible_words.append(new_word)


  #Return the list of possible words
  print(possible_words)
  return possible_words










def create_formation_grid():
    """

    Output file creation and handling
    """
    file_name = 'output/gchq_christmas_2022.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f'{file_name} deleted.')
    else:
        # If the file does not exist, display a message
        print(f'{file_name} does not exist. Creating')


    with open(file_name, 'a') as f:
        f.write("Step 1 - The Following colours are assigned:\n\n")


    word = "FORMATION"


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



def colours():
    """
    Writes color mappings
    to the output file.
    """
    for color, letters in color_letters.items():
        colors  = (f"{color}: {letters}")
        print(colors)
        with open('output/gchq_christmas_2022.txt', 'a') as f:
            f.write(colors+'\n')

    with open('output/gchq_christmas_2022.txt', 'a') as f:
        f.write('\n')
colours()



"""
A letter from these words
will be used to replace the
corresponding colours. See
The question requirements. 
"""

green_word = "EYES"
gold_word = "UNCURL"


def blue_squares(color):

    """

    The First row
    """

    vowels = 'aeiouAEIOU'
    blue_word = "PART"

    if color in color_letters:
        for letter in color_letters[color]:
            print(f"Doing something with {letter}")

            first_row = "".join(grid[0])

            possible_words = find_possible_words_blue_row_one(first_row, blue_word)


            print(possible_words, '<-------possible words')

            """
            1. If there is one possible alternate word 
            2. Immediately assign that word to row one 
            3. Break from the outer for loop
            """
            if len(possible_words) == 1:
                grid[0] = [letter for letter in possible_words[0]]

                print(grid[0])
                break





            try:
                 letter_position =   grid[0].index(letter)
            except ValueError:
                #print("Letter not present on this row")
                 pass


            counter = 0
            while True:

                 first_row = "".join(grid[0])

                 grid[0][letter_position] = blue_word[counter]

                 if is_valid_uk_english_word(first_row) == True:
                    break

                 counter += 1

                 if counter == 4:
                     break



        """
        Second row
        """
        for letter in color_letters[color][1:]:
            """
            1.look for instances of blue letters on the second row
            2. locate the index of the blue letter on the second row
            """
            print(f"Doing something with {letter}")

            sec_row = "".join(grid[1])

            possible_words = find_possible_words_blue_row_two(sec_row, blue_word)

            print(possible_words,'<---possible words')

            """
            1. If there is one possible alternate word 
            2. Immediately assign that word to row one 
            3. Break from the outer for loop
            """
            if len(possible_words) == 1:
                grid[1] = [letter for letter in possible_words[0]]

                print(grid[0])
                break




            try:
                letter_position =  grid[1].index(letter)
            except ValueError:
                #print("Letter not present on this row")
              pass

            print(letter_position,'<----letter poss')


            counter = 0
            while True:

                grid[1][letter_position] = blue_word[counter]

                sec_row = "".join(grid[1])

                counter += 1

                if is_valid_uk_english_word(sec_row) == True:
                    break


                if counter == 4:
                    break




        """
        Third row
        """
        for letter in color_letters[color][2:]:

            """
            1.look for instances of blue letters on the second row
            2. locate the index of the blue letter on the second row
            """
            print(f"Doing something with {letter}")

            thir_row = "".join(grid[2])

            possible_words = find_possible_words(thir_row,blue_word)

            print(possible_words, '<---possible words THIR')


            """
            1. If there is one possible alternate word 
            2. Immediately assign that word to row one 
            3. Break from the outer for loop
            """
            if len(possible_words) == 1:
                grid[1] = [letter for letter in possible_words[0]]

                print(grid[0])
                break

            """
            If there is more than one possible new word
            perform someo other functions
            """
            if len(possible_words) >1:

                len_poss = len(possible_words)

                print("There are possibly"+str(len_poss)+" new words. Further processing!")

                further_checks = []

                for i in range(len_poss):
                    print(possible_words[i])

                    is_word = (possible_words[i].lower() in english_words_alpha_set)
                    further_checks.append(is_word)


            are_true  = [i for i, bol in enumerate(further_checks) if bol == True]


            if len(are_true) == 1:
                grid[2] = [letter for letter in possible_words[are_true[0]]]
                break
            else:
                pass




            """
            
            Final logic 
            
            """
            letter_position = [i for i, color in enumerate(grid[2]) if color == letter]

            counter = 0
            while True:

                grid[2][letter_position[0]] = blue_word[-1][counter]

                thir_row = "".join(grid[1])

                counter += 1

                if is_valid_uk_english_word(thir_row) == True:
                    break

                if counter == 4:
                    break





            with open('output/gchq_christmas_2022.txt', 'a') as f:
                f.write('Step 2 - The blue squares are assigned their replacement letter:\n\n')


            for row in grid:
                with open('output/gchq_christmas_2022.txt', 'a') as f:
                    f.write(str(row)+'\n')
                    print(row)

            with open('output/gchq_christmas_2022.txt', 'a') as f:
                f.write('\n')






blue_squares('blue')



def green_squares(color):
    """
    Dealing with green squares
    """

    """
    second row
    """
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


            sec_row = "".join(grid[1])


            if is_valid_uk_english_word(sec_row) == True:
                break


            counter += 1

            if counter == 4:
                break


    """
    Third row 
    """
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

          thir_row = "".join(grid[1])

          if is_valid_uk_english_word(thir_row) == True:
              break


          counter += 1

          if counter == 4:
              break


    with open('output/gchq_christmas_2022.txt', 'a') as f:
        f.write('Step 3 - The green squares are assigned their replacement letter:\n\n')


    for row in grid:
        with open('output/gchq_christmas_2022.txt', 'a') as f:
            f.write(str(row)+'\n')
            print(row)

    with open('output/gchq_christmas_2022.txt', 'a') as f:
        f.write('\n')



green_squares('green')

time.sleep(1000)




def gold_squares(color):
    """
    Dealing with gold squares
    """
    if color in color_letters:
        """
        The first row
        """
        for letter in color_letters[color]:
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

                if first_row =='CAR':
                    if is_valid_uk_english_word(first_row) == True:
                        break


                counter += 1

                if counter == 6:
                    break

        """
        second row 
        """
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
        

              sec_row = "".join(grid[1])

              if is_valid_uk_english_word(sec_row) == True:
                  break


              counter += 1
        
              if counter == 6:
                  break
        
        
        """
        Third row
        """
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

                thir_row = "".join(grid[1])

                if is_valid_uk_english_word(thir_row) == True:
                    break


                counter += 1

                if counter == 6:
                    break

        with open('output/gchq_christmas_2022.txt', 'a') as f:
            f.write('Step 4 - The gold squares are assigned their replacement letter:\n\n')

        for row in grid:
            with open('output/gchq_christmas_2022.txt', 'a') as f:
                f.write(str(row)+'\n')


gold_squares('gold')






print('\n')
print("The resulting array is:")
for row in grid:

    print(row)


