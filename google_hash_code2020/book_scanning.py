from large_lists import  error_handles
import abc
import re



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
                callable(subclass.checks_library_desc_vert_struct) or

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


    @abc.abstractmethod
    def checks_second_line(self):
        """
        • Checks the structure of the second line integers :
        • Are they within the right spacing structure: S 0 , … , S B-1 , (0 ≤ S i ≤ 10 3 )?
        • Is there a complete set of three numbers?
        • If any of these is not true, execution will be terminated
        """


    def checks_library_desc_vert_struct(self):
        """
        Lines [2:x] contains L sections of two lines per library that describe:

        [L1]=[number of books in each library, the number of days it takes to
        finish the library sign-up,the number of books that can be shipped from library]

        [L2]=[IDs of the books in each library]

        Thus, the the vertical structure of becomes non linear from here on.

        Special consideration is needed to parse L1, and L2 for each library.
        Since the numbers of libraries per input file is dynamic, the solution
        here also needs to be dynamic. The first action is to make sure that
        lines [2:x] satisfy mathematical constraints.
        """





class BookScanning(Interface):


    correct_space_pattern = r'([^\s]+)'


    def __int__(self):
        pass


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

        spaces = result = re.findall(self.correct_space_pattern, first_line)

        if len(spaces) !=3:
            print(error_handles[0])
            return
        else:
            pass

        """
        Handles cases where one of the elements on the first line is not an integer.
        """
        try:
            spaces = [int(x) for x in spaces]

        except ValueError:
            print(error_handles[1])
            return


        """
        Checks if numbers are 
        B ( 1 ≤ B ≤ 10 **5 )
        L ( 1 ≤ L ≤ 10**5 )
        D ( 1 ≤ D ≤ 10 5 )
        """
        for index, number in enumerate(spaces):
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


        first_line_dict = {"Books":spaces[0],"Libraries":spaces[1],"Days":spaces[2]}

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



        print(book_score_dict)
        return  book_score_dict
















def testing():
    run = BookScanning()
    #print(run.checks_first_line())
    run.checks_second_line()


if __name__ == "__main__":
    testing()