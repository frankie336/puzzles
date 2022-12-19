import time
from large_lists import  error_handles
import abc
import re
from collections import Counter


class Interface(metaclass=abc.ABCMeta):
    """Formal Interface"""
    @classmethod
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'reads_text') and
                callable(subclass.reads_text) and

                hasattr(subclass, 'checks_first_line') and
                callable(subclass.checks_first_line) and

                hasattr(subclass, 'checks_second_line') and
                callable(subclass.checks_second_line) and

                hasattr(subclass, 'checks_library_desc_vert_struct') and
                callable(subclass.checks_library_desc_vert_struct) and

                hasattr(subclass, 'get_descriptions') and
                callable(subclass.get_descriptions) and

                hasattr(subclass, 'get_list_of_books') and
                callable(subclass.get_list_of_books) and

                hasattr(subclass, 'signup_order') and
                callable(subclass.signup_order) and

                hasattr(subclass, 'book_selection') and
                callable(subclass.book_selection) and

                hasattr(subclass, 'submission_file') and
                callable(subclass.submission_file) or


                NotImplemented)



    @abc.abstractmethod
    def reads_text(self,file_name: str) -> str:
        """
        Reads text files
        Returns a list of elements per line
        """
        raise NotImplemented


    @abc.abstractmethod
    def checks_first_line(self):
        """
        • Checks the structure of the first line integers :
        • Are they within the right spacing structure: n1 n2  n3 ?
        • Is there a complete set of three numbers?
        • Are they each  x( 1 ≤ B ≤ 10 5 )?
        • If any of these is not true, execution will be terminated
        • Returns a dictionary
        """
        raise NotImplemented


    @abc.abstractmethod
    def checks_second_line(self):
        """
        • Checks the structure of the second line integers :
        • Are they within the right spacing structure: S 0 , … , S B-1 , (0 ≤ S i ≤ 10 3 )?
        • Is there a complete set of three numbers?
        • If any of these is not true, execution will be terminated
        """
        raise NotImplemented


    @abc.abstractmethod
    def is_whole_number(self, a, b):
        """
        Checks if the result of division is a whole number
        """
        raise NotImplemented


    @abc.abstractmethod
    def checks_library_desc_vert_struct(self):
        """
        Lines [2:x] contains L sections of two lines per library that describe:

        [L1]=[number of books in each library, the number of days it takes to
        finish the library sign-up,the number of books that can be shipped from library]

        [L2]=[IDs of the books in each library]

        Thus, the vertical structure of becomes non linear from here on.

        Special consideration is needed to parse L1, and L2 for each library.
        Since the numbers of libraries per input file is dynamic, the solution
        here also needs to be dynamic. The first action is to make sure that
        lines [2:x] satisfy mathematical constraints.
        """
        raise NotImplemented


    @abc.abstractmethod
    def get_descriptions(self):
        """
        • Parses lines [2:x] for the L sections of each library.
        • Performs  further checks on the horizontal data structures
        • Returns a dictionary
        """
        raise NotImplemented


    @abc.abstractmethod
    def get_list_of_books(self):
        """
        • Creates a mapping between books per library, and the book scores
        • Returns a nested list of scores per book in library
        • Returns a list of summed scores per library
        """
        raise NotImplemented


    @abc.abstractmethod
    def signup_order(self):
        """
        Calculates which library should be the first to be signed on
        """
        raise NotImplemented



    @abc.abstractmethod
    def book_selection(self):
        """
        Selects books to be scanned per library
        """
        raise NotImplemented

    @abc.abstractmethod
    def submission_file(self):
        """
        Creates the submission file
        """
        raise NotImplemented






class BookScanning(Interface):


    correct_space_pattern = r'([^\s]+)'

    def __init__(self):

        self.total_book_count = 0
        self.days = 0

    def reads_text(self, file_name: str) -> str:

        """
        Reads text files
        Returns a list of elements per line
        """
        with open(file_name, 'r') as file:
            lines = file.readlines()

        return lines



    def checks_first_line(self):
        """
        • Checks the structure of the first line integers :
        • Are they within the right spacing structure: n1 n2  n3 ?
        • Is there a complete set of three numbers?
        • Are they each  B ( 1 ≤ B ≤ 10**5 )?
        • If any of these is not true, execution will be terminated
        • Returns a dictionary
        """
        first_line =   self.reads_text(file_name='input/input.txt')[0]

        first_line = re.findall(self.correct_space_pattern, first_line)

        if len(first_line) !=3:
            print(error_handles[0])
            return
        else:
            pass

        """
        Handles cases where one of the elements on the first line is not an integer.
        """
        try:
            first_line = [int(x) for x in first_line]

        except ValueError:
            print(error_handles[1])
            return

        """
        Checks if numbers are 
        B ( 1 ≤ B ≤ 10**5 )
        L ( 1 ≤ L ≤ 10**5 )
        D ( 1 ≤ D ≤ 10 5 )
        """
        for index, number in enumerate(first_line):
            if number == int(number):
                if number >10**5:
                    if index == 0:
                        print(error_handles[2])
                        return
                    if index==1:
                        print(error_handles[3])
                        return
                    if index==2:
                        print(error_handles[4])
                        return




        first_line_dict = {"Books":first_line[0],"Libraries":first_line[1],"Days":first_line[2]}

        return first_line_dict






    def checks_second_line(self):
        """
        • Checks the structure of the second line integers :
        • Are they within the right spacing structure: S 0 , … , S B-1 , (0 ≤ S i ≤ 10 3 )?
        • Is there a complete set of three numbers?
        • If any of these is not true, execution will be terminated
        • If any of these is not true, execution will be terminated
        """
        sec_line = self.reads_text(file_name='input/input.txt')[1]

        number_of_books = self.checks_first_line()["Books"]

        spaces = re.findall(self.correct_space_pattern, sec_line)


        """
        The size of S is equal to the number of books. 
        Check that the data input has the correct size of S.
        """
        if len(spaces) !=number_of_books:
            print(error_handles[5])
            return
        else:
            pass


        """
        Handles cases where one of the elements on the first line is not an integer.
        """
        try:
            spaces = [int(x) for x in spaces]

        except ValueError:
            print(error_handles[6])
            return


        """
        Checks if numbers are 
        S 0 , … , S B-1 , (0 ≤ S i ≤ 10 3 )
        """
        for index, number in enumerate(spaces):
            if number == int(number):
                if number > 10 ** 3:
                    print("Book "+str(index)+error_handles[7])
                    return


        book_score_dict = {"Book0":spaces[0],
                           "Book1":spaces[1],
                           "Book2":spaces[2],
                           "Book3":spaces[3],
                           "Book4":spaces[4],
                           "Book5":spaces[5],
                           }


        #print(book_score_dict)
        return  book_score_dict




    def is_whole_number(self,a, b):
        """
        Checks if the result of division is a whole number
        """
        quotient, remainder = divmod(a, b)

        return remainder == 0




    def checks_library_desc_vert_struct(self):
        """
        -Checks for empty lines
        Lines [2:x] contains L sections of two lines per library that describe:

        [L1]=[number of books in each library, the number of days it takes to
        finish the library sign-up,the number of books that can be shipped from library]

        [L2]=[IDs of the books in each library]

        Thus, the vertical structure of becomes non linear from here on.

        Special consideration is needed to parse L1, and L2 for each library.
        Since the numbers of libraries per input file is dynamic, the solution
        here also needs to be dynamic. The first action is to make sure that
        lines [2:x] satisfy mathematical constraints.
        """

        vert_lines = self.reads_text(file_name='input/input.txt')[2:]

        """
        checks for empty lines
        """
        for index, line in enumerate(vert_lines):
            if line =="\n":
                print("line "+str(index+2)+error_handles[8])
                return


        """
        If division of the sum of the length of  lines [2:] does not yield a 
        whole number there is something wrong with the structure of the data.
        """
        a = (len(vert_lines))

        if  self.is_whole_number(a, 2) == False:
            print(error_handles[9])
        else:
            pass

        return a




    def get_descriptions(self):

        """
        • Parses lines [2:x] for the L sections of each library.
        • Performs  further checks on the horizontal data structures
        • Returns a dictionary

        Checks that:
        Nj( 1 ≤ N j ≤ 10**5 )
        T j ( 1 ≤ T j ≤ 10**5 )
        M j ( 1 ≤ M j ≤ 10**5 )
        """
        vert_len = self.checks_library_desc_vert_struct()

        vert = self.reads_text(file_name='input/input.txt')[2:]


        """
        Makes a nested list of ever x2 pair of elements
        which results in L1, and L2 fo each library 
        """
        nested_vert = [list(pair) for pair in zip(vert[::2], vert[1::2])]


        library_desc_dict_master = {}

        for index, describe in enumerate(nested_vert):

            lib_desc = re.findall(self.correct_space_pattern, describe[0])
            book_id = re.findall(self.correct_space_pattern, describe[1])


            try:
                lib_desc = [int(x) for x in lib_desc]

                book_id = [int(x) for x in book_id]

            except ValueError:
                print("Library "+str(index)+error_handles[11])
                return


            """
            N j ( 1 ≤ N j ≤ 10**5)
            T j ( 1 ≤ T j ≤ 10**5)
            M j ( 1 ≤ M j ≤ 10**5)
            The total number of books in all libraries does not exceed 10**6 .
            """
            for i, number in enumerate(lib_desc):

                if self.total_book_count >10**6:
                    print(error_handles[17]+str(10**6)+error_handles[14])
                    return

                if i == 0:
                    if number >10**5:
                        print(error_handles[12]+ str(index)+error_handles[13]+str(10**5)+error_handles[14] )
                        return
                    self.total_book_count +=number


                if i == 1:
                    if number >10**5:
                        print(error_handles[15]+" "+str(index)+error_handles[13]+str(10**5)+str(error_handles[14]))
                        return

                if i == 2:
                    if number >10**5:
                        print(error_handles[16]+str(index)+error_handles[13]+str(10**5)+str(error_handles[14]))
                        return

            if len(lib_desc) != 3:
                print("Library "+str(index)+error_handles[10])
                return
            else:
                pass

            library_desc_dict = {"Library"+str(index):[]}
            library_desc_dict["Library"+str(index)].append(lib_desc)
            library_desc_dict["Library" + str(index)].append(book_id)
            library_desc_dict_master.update(library_desc_dict)

        #print(library_desc_dict_master)
        return library_desc_dict_master




    def get_list_of_books(self):
        """
        • Returns nested list of books per library
        """

        b = self.checks_first_line()["Books"]
        print(b,"Books")

        d = self.checks_first_line()["Days"]
        print(d,"Days")

        l =self.checks_first_line()["Libraries"]
        print(l,"Libraries")


        desc = self.get_descriptions()
        t = self.get_descriptions()["Library0"][0][1]

        """
        Gets the books per library
        """
        books_in_library_consol = []

        for i in range(l):
            books_in_library = self.get_descriptions()["Library"+str(i)][1]

            books_in_library_consol.append(books_in_library)


        return  books_in_library_consol




    def signup_order(self):
        """
        The order in which libraries are signed up is determined  by a formula:
        a/b. Where a is the sum total of total book scores on hand, and b is the
        time cost incurred in the sign up process.
        """
        full_list_of_books = self.get_list_of_books()

        l = self.checks_first_line()["Libraries"]
        print(l, "Libraries")

        """
        Creates a list of duplicate entries that can be used to filter the nested lists.
        """
        flattened_list = [i for sublist in full_list_of_books for i in sublist]
        counter = Counter(flattened_list)
        duplicate_entries = [i for i in flattened_list if counter[i] > 1]
        #print(duplicate_entries)

        """
        Filters unique books from each list of books
        """
        unique_books = [[x for x in inner_list if x not in duplicate_entries] for inner_list in full_list_of_books]

        print(full_list_of_books)
        print(unique_books,'<--Unique Books')


        """
        Maps the value of the books per library.
        """
        mapped_scores = []
        for inner_list in full_list_of_books:
            score = []
            for book in inner_list:
                book_score = self.checks_second_line()["Book" + str(book)]
                score.append(book_score)



            mapped_scores.append(score)

        summed_book_scores = [sum(sublist) for sublist in mapped_scores]

        print(mapped_scores,'<---Score per unique book')
        print(summed_book_scores,'<----summed unique book scores')


        values_time = []

        for i, value in enumerate(summed_book_scores):

            sign_on_time = self.get_descriptions()["Library"+str(i)][0][1]

            value = (value,sign_on_time)

            values_time.append(value)


        print(self.get_descriptions())

        value_ratios = [a / b for a, b in values_time]

        sign_up_order_dict = {}

        for i, value in enumerate(value_ratios):

            sign_up_order_dict[str(i)] = value

        sign_up_order_dict = sorted(sign_up_order_dict.items(), key=lambda item: item[1], reverse=True)

        print(sign_up_order_dict)

        return sign_up_order_dict




    def book_selection(self):
        """
        Selects books to be scanned per library
        """
        sign_up = self.signup_order()

        books_per_library = self.get_list_of_books()


        print(books_per_library)



        book_scores = []

        for i, value in enumerate(sign_up):

            libr = value[0]

            cand_books = books_per_library[int(libr)]

            score = []
            for i, book in enumerate(cand_books):

                book_score = self.checks_second_line()["Book" + str(book)]
                score.append(book_score)

            book_scores.append(score)

        print(book_scores)

        list_dicts = []
        """
        Makes a list of dictionaries per library. The keys=book ID’s.
        The values = valuer per book.
        """
        for sublist, keys in zip(book_scores, books_per_library):
            list_dicts.append({key: value for key, value in zip(keys, sublist)})

        print(list_dicts)

        book_order_dicts = [{k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)} for d in list_dicts]

        print(book_order_dicts)

        return book_order_dicts


    def submission_file(self):
        """
        Creates the submission file
        """

        """
        • Calculates the number of available days after the first Library completes the sign up process 
        • All processing must now scale into this remainder number 
        """
        self.days = self.checks_first_line()["Days"]

        first_lib_id = self.signup_order()[0][0]

        first_cost = self.get_descriptions()["Library"+first_lib_id][0][1]

        self.days = self.days-(first_cost+1)
        print(self.days)

        """
        . Calculates scaling of book submissions over given days.
        """
        book_coe = []
        book_scaling = []
        counter = 0
        for value in self.get_descriptions().values():

            a = value[0][2]
            book_coe.append(a)

            b = value[0][0]

            d = b - a

            times_to_multiply = d / a

            rounded_times = round(times_to_multiply)

            result = a * rounded_times

            book_scaling.append(result)



        print(counter,'???')






        print(book_coe,book_scaling)

        print(self.get_descriptions())










        #print(book_coe,book_scaling)
        #number_of_libraries = str(len(self.signup_order()))
        #with open('output/output.txt', 'a') as file:
            #file.write(number_of_libraries)













































def testing():
    run = BookScanning()
    #print(run.checks_first_line())
    #run.checks_second_line()
    #run.checks_library_desc_vert_struct()
    #run.get_descriptions()
    #run.get_list_of_books()
    #run.signup_order()
    run.book_selection()
    run.submission_file()


if __name__ == "__main__":
    testing()