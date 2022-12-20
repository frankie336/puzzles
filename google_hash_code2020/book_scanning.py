import time
import os
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

                hasattr(subclass, 'header_line') and
                callable(subclass.header_line) and

                hasattr(subclass, 'book_scores') and
                callable(subclass.book_scores) and

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

                hasattr(subclass, 'scanning_schedule') and
                callable(subclass.scanning_schedule) and

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
    def header_line(self):
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
    def book_scores(self):
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
        This method selects the order in which libraries are selected for the signup process:
        f(x) = ∑i∈L (Vi * xi)
        Subject to the following constraint:
        ∑i∈L (Ti * xi) <= D
        """
        raise NotImplemented




    @abc.abstractmethod
    def book_selection(self):
        """
        Selects books to be scanned per library
        """
        raise NotImplemented




    @abc.abstractmethod
    def scanning_schedule(self):
        """
        Calculates a scanning schedule that maximises the number
        of books on hand per library scaled each day by the rate
        at which a library can send books.

        num_shipments = ⌊M / R⌋
        final_shipment_size = min(D * R, M - num_shipments * R)
        """
        raise NotImplemented




    @abc.abstractmethod
    def submission_file(self):
        """
        Creates the submission file
        • Must start with a line containing the integer A ( 0 ≤ A ≤ L )
        • Describes which books to ship from which library
        • The order in which libraries are signed up
        • Must describe each library, in the order that you want them to start the signup process
        • The description of each library must contain two lines:
        Y ( 0 ≤ Y ≤ L – 1) – the ID of the library
        K ( 1 ≤ K ≤ N Y )
        """
        raise NotImplemented




class BookScanning(Interface):


    correct_space_pattern = r'([^\s]+)'

    def __init__(self):

        self.total_book_count = 0
        self.days = 0
        self.books_scanned = []#tracks all scanned books




    def reads_text(self, file_name: str) -> str:

        """
        Reads text files
        Returns a list of elements per line
        """
        with open(file_name, 'r') as file:
            lines = file.readlines()

        return lines



    def header_line(self):
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




    def book_scores(self):
        """
        • Checks the structure of the second line integers :
        • Are they within the right spacing structure: S 0 , … , S B-1 , (0 ≤ S i ≤ 10 3 )?
        • Is there a complete set of three numbers?
        • If any of these is not true, execution will be terminated
        • If any of these is not true, execution will be terminated
        """
        sec_line = self.reads_text(file_name='input/input.txt')[1]

        number_of_books = self.header_line()["Books"]

        book_list = re.findall(self.correct_space_pattern, sec_line)


        """
        The size of S is equal to the number of books. 
        Check that the data input has the correct size of S.
        """
        if len(book_list) !=number_of_books:
            print(error_handles[5])
            return
        else:
            pass


        """
        Handles cases where one of the elements on the first line is not an integer.
        """
        try:
            book_list = [int(x) for x in book_list]

        except ValueError:
            print(error_handles[6])
            return

        """
        Checks if numbers are 
        S 0 , … , S B-1 , (0 ≤ S i ≤ 10 3 )
        """
        for index, number in enumerate(book_list):
            if number == int(number):
                if number > 10 ** 3:
                    print("Book "+str(index)+error_handles[7])
                    return

        book_score_dict = {}

        for i, score in enumerate(book_list):
            book_score_dict["Book"+str(i)] = score


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

        return library_desc_dict_master




    def get_list_of_books(self):
        """
        • Returns nested list of books per library
        """

        b = self.header_line()["Books"]
        print(b,"Books")

        d = self.header_line()["Days"]
        print(d,"Days")

        l =self.header_line()["Libraries"]
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
        This method selects the order in which libraries are selected for the signup process:
        f(x) = ∑i∈L (Vi * xi)
        Subject to the following constraint:
        ∑i∈L (Ti * xi) <= D
        """
        header_line = self.header_line()

        self.days = header_line["Days"]

        library_books = self.get_list_of_books()

        book_scores = self.book_scores()

        descriptions = self.get_descriptions()


        """
        Maps the value of the books per library.
        """
        mapped_scores = []

        for inner_list in library_books:
            score = []
            for book in inner_list:
                book_score = book_scores["Book" + str(book)]
                score.append(book_score)

            mapped_scores.append(score)

        """
        Begin by sorting the libraries in decreasing order of value per day, 
        where value per day is calculated as the total value of the books in 
        the library divided by the time it takes to sign up for the library.
        """
        summed_book_scores = [sum(sublist) for sublist in mapped_scores]
        library_values = []

        for i, score in enumerate(summed_book_scores):

            signup_days = descriptions["Library"+str(i)][0][1]

            value = score/signup_days

            library_values.append(value)

        library_values_dict = {i: x for i, x in enumerate(library_values)}
        library_values_dict = dict(sorted(library_values_dict.items(), key=lambda item: item[1], reverse=True))


        """
        • Loops the values dictionary 
        • Libraries will only be selected where the number of days left after their sign on process is >0
        • The key of the ordered dictionary is the library ID and thus preserves the correct ID in selection 
        """
        selected_libraries = []

        for i, (key, value) in enumerate(library_values_dict.items()):

            days = descriptions["Library"+str(key)][0][1]

            self.days = self.days - (days+0)

            """
            If there is at least one day left 
            after the sign up process include 
            the library as a selected library 
            """
            if self.days >1:
                selected_libraries.append(key)

        self.days = header_line["Days"]#resets the tota number of days for later use


        #print(header_line,'<----Header line','\n',
              #self.days,'<---Days','\n',
              #library_books,'<---library books','\n',
              #book_scores,'<----Book Scores','\n',
              #mapped_scores,'<----Mapped Scores','\n',
              #summed_book_scores,'<----Summed book scores','\n',
              #descriptions,'<-----descriptions','\n',
              #library_values,'<---values','\n',
              #library_values_dict,'<-----values dict','\n',
             #selected_libraries,'<-----selected libraries'
              #)

        return selected_libraries




    def book_selection(self):
        """
        Selects books to be scanned per library

        Sorted books:
        B_{iB_{i,1} >= B_{i,2} >= ... >= B_{i,m_i},1} >= B_{i,2} >= ... >= B_{i,m_i}
        Request:
        B_{i,j} = argmax_{b \in U} V_{i,j}

        Sort the books in each library by their assigned value in decreasing order
        For each library, request the highest value book that has not already been scanned and
        can be scanned within the remaining number of days.
        Repeat this process until all books have been scanned or there are no more days left.
        """
        selected_libraries = self.signup_order()

        library_books = self.get_list_of_books()

        book_scores = self.book_scores()

        """
        """
        mapped_scores = []

        for i, library in enumerate(selected_libraries):

            cand_books = library_books[library]

            score = []
            for j, book in enumerate(cand_books):

                book_score = book_scores["Book" + str(book)]

                score.append(book_score)

            mapped_scores.append(score)



        list_of_candbooks = [dict(zip(keys, lst)) for keys, lst in zip(library_books, mapped_scores)]

        master_book_dicts = [{key: dict_} for key, dict_ in zip(selected_libraries, list_of_candbooks)]#dicts,keys from nest



        final_sorted_dicts_list = []

        for i in range(len(master_book_dicts)):

            sortx  = ordered_master_book_dicts1 = [
            {outer_key: {k: v for k, v in sorted(inner_dict.items(), key=lambda x: x[1], reverse=True)}}
            for outer_key, inner_dict in master_book_dicts[i].items()]


            final_sorted_dicts_list.append(sortx[0])


        #print(selected_libraries,'<--Selected_libraries','\n',
              #library_books,'<---library_books','\n',
              #book_scores,'<--Book_scores','\n',
              #mapped_scores,'<-----mapped_scores','\n',
              #list_of_candbooks,'<------cand_books','\n',
              #master_book_dicts,'<----wrapped_dicts','\n',
              #final_sorted_dicts_list ,'<----sorted')

        return final_sorted_dicts_list




    def scanning_schedule(self):
        """
        Calculates a scanning schedule that maximises the number
        of books on hand per library scaled each day by the rate
        at which a library can send books.

        num_shipments = ⌊M / R⌋
        final_shipment_size = min(D * R, M - num_shipments * R)
        """
        header_line = self.header_line()

        candidate_books = self.book_selection()

        descriptions = self.get_descriptions()

        scans_schedule_dict = {}

        for i in range(len(candidate_books)):

            library_id = list(candidate_books[i].keys())[0]

            cand_books = candidate_books[i][library_id]

            days = descriptions["Library" + str(library_id)][0][1]

            self.days = self.days - (days + 0)#TBC

            """
            Initializing the variables of:
            num_shipments = M // R
            final_shipment_size = min(D * R, M - num_shipments * R, B)
            """
            D = self.days
            R = descriptions["Library" + str(library_id)][0][2]
            B = descriptions["Library" + str(library_id)][0][0]
            M=B

            num_shipments = M // R    ###need solution
            final_shipment_size = min(D * R, M - num_shipments * R, B)


            for i in range(num_shipments):

                B = B - R

                scans_range =R*num_shipments+final_shipment_size


            book_list = list(cand_books.keys())

            book_list = [x for x in book_list if x not in self.books_scanned]#Filters books that have been scanned

            schedule = book_list[:scans_range]


            scans_schedule_dict[library_id] = schedule

            self.days = self.days-scans_range

            self.books_scanned.extend(schedule)#Adds books just scanned to the tracker








        #print(self.days,'<----Initial days available','\n',
              #candidate_books,'<-----candidate books','\n',
              #scans_schedule_dict,'<----Schedule dict','\n',
              #self.days,'<----Days left','\n',
              #self.books_scanned,'<---All books scanned')

        return scans_schedule_dict




    def submission_file(self):
        """
        • Must start with a line containing the integer A ( 0 ≤ A ≤ L )
        • Describes which books to ship from which library
        • The order in which libraries are signed up
        • Must describe each library, in the order that you want them to start the signup process
        • The description of each library must contain two lines:
        Y ( 0 ≤ Y ≤ L – 1) – the ID of the library
        K ( 1 ≤ K ≤ N Y )
        """
        file_name = 'output/output.txt'

        selected_libraries = self.signup_order()#Ordered list of selected libraries

        libraries = str(len(selected_libraries))

        scan_secdule = self.scanning_schedule()

        print(len(scan_secdule))




        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'{file_name} deleted.')


        with open(file_name, "w") as file:
            file.write(libraries+'\n')



        for i, library in enumerate(selected_libraries):


            schedule = scan_secdule[library]
            schedule = list(map(str, schedule))
            books_no = str(len(schedule))
            schedule_string = " ".join(schedule)

            ord = str(library) + ' ' +books_no+ '\n'+schedule_string+'\n'

            with open(file_name, "a") as file:
                file.write(ord)



        print(selected_libraries,'<----Selected libraries','\n',
              scan_secdule,'<------Scan Schedule per library')









def testing():
    run = BookScanning()
    #print(run.header_line())
    #run.book_scores()
    #run.checks_library_desc_vert_struct()
    #run.get_descriptions()
    #run.get_list_of_books()
    #run.signup_order()
    #run.book_selection()
    #run.scanning_schedule()
    run.submission_file()
    #print(run.signup_order())


if __name__ == "__main__":
    testing()