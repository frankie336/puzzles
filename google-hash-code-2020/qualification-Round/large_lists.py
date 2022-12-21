
"""
This list contains error messages that will be used to diagnose faults, and issues  with the data input file.
"""
error_handles = ["\nThe first line of the of input file is malformed.\n"
                 "The first line should be three integers separated by a space:\n"
                 "[n1 n2 n3]\n"
                 "Possible causes include:\n"
                 "• Insufficient data\n"
                 "• Incorrect data\n"
                 "Terminating. Resume with a corrected input file!",

                 "\nOne or more of the characters on the first line of the data input file is malformed. Possible causes:\n"
                 "• One or more characters are not numbers.\n"
                 "Terminating. Resume with a corrected input file!",

                 "\nThe number of different books cannot exceed 100,000!\n"
                 "Terminating. Resume with a corrected input file!",

                 "\nThe number of libraries cannot exceed 100,000!\n"
                 "Terminating. Resume with a corrected input file!",

                 "\nThe number of days cannot exceed 100,000!\n"
                 "Terminating. Resume with a corrected input file!",


                 "\nThe second line of the of input file is malformed.\n"
                 "The second line should be series integers equal to the number of books separated by a space:\n"
                 "[s1, s2, s3...]\n"
                 "Possible causes include:\n"
                 "• Insufficient data\n"
                 "• Incorrect data\n"
                 "Terminating. Resume with a corrected input file!",


                 "\nOne or more of the characters on the second line of the data input file is malformed. Possible causes:\n"
                 "• One or more characters are not numbers.\n"
                 "Terminating. Resume with a corrected input file!",

                 " exceeds a score of 1000.\n"
                 "The Score of individual books cannot exceed 1000.\n"
                 "Terminating. Resume with a corrected input file!",
                 " on the input file only contains a new line character with no number sequence present.\n"
                 "This section relates to either the description of an individual library (L) or the\n"
                 "book ID’s within a library.\n"
                 "Terminating. Resume with a corrected input file!",

                 "\nThe sum of  lines 2:n divided by 2 should yield a whole number. Where this is not the case,\n "
                 "further processing of the input data will not work. Possible causes include:\n"
                 "• Insufficient data\n"
                 "• Incorrect data\n"
                 "Terminating. Resume with a corrected input file!",



                 " L1 library description is malformed.\n"
                 "The first line should be three integers separated by a space:\n"
                 "[L1 L2 L3]\n"
                 "Possible causes include:\n"
                 "• Insufficient data\n"
                 "• Incorrect data\n"
                 "Terminating. Resume with a corrected input file!",


                 " L1 library description is malformed:\n"
                 "• One or more characters are not numbers.\n"
                 "Terminating. Resume with a corrected input file!",

                 "The number of books in library ",
                 " cannot exceed ",
                 "\nTerminating. Resume with a corrected input file!",

                 "The number of days it takes to finish sign up of library ",

                 "The number of books that can be shipped from library ",

                 "The total number of books in all libraries does not exceed ",

                 ]



