
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
                 "Terminating. Resume with a corrected input file!"



                 ]



