# Folder Structure
- `qualification-Round/`: This folder contains source files to the qualifying round.

# Qualification Round: /qualification-Round

This is an optimisation problem based on the Google Books Project: https://books.google.co.uk/intl/EN/googlebooks/about.html. The project encounters a logistical challenge: the optimal way to scan millions of books from tens of thousands of libraries in the case where libraries often have the same books in their catalogues. 

The question introduces the real world terms of the challenge, and asks contestants to solve the problem using an input data structure:  input/input.txt. The input file is a data structure  from where candidate libraries with candidate books can be discerned on a points based basis.  

The input file is used to to produce an output file: output/output.txt. The output file is a data structure from where a points based order of libraries and books to be scanned next can be discerned.

- /book_scanning.py: The main class object file. Contains the methods, and algorithms. 
- /large_lists.py: Used to import large lists and collections/
- /main.py: Calls and executes  the code.

- /input/input.txt: The input data structure. See the question constraints.
- /output/output.txt The output data structure. See the question constraints.




## Algorithm 

Step 1: Sort L in descending order of the ratio (Σ_{j=1}^{N_i} S_j) / T_i for each i in L.

Step 2a: Sort B_i in descending order of S_j for each j in B_i.

Step 2b: Set K_i = min(K_i, M_i * D).

Step 2c: If j is in the tracking list of books already scanned, continue to the next book.

2. Otherwise, add book j to the tracking list of books already scanned. This step can be expressed as follows:

Step 2d: Add j to the tracking list of books already scanned.


