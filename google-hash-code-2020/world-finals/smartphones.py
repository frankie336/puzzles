from large_lists import error_handles
import abc
import time
import re
import numpy as np



class Interface(metaclass=abc.ABCMeta):
    """Formal Interface"""

    @classmethod
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'reads_text') and
                callable(subclass.reads_text) and

                hasattr(subclass, 'the_grid') and
                callable(subclass.the_grid) and

                hasattr(subclass, 'mount_points') and
                callable(subclass.mount_points) and

                hasattr(subclass, 'get_tasks') and
                callable(subclass.get_tasks) or

                NotImplemented)

    @abc.abstractmethod
    def reads_text(self, file_name: str) -> str:
        """
        Reads text files
        Returns a list of elements per line
        """
        raise NotImplemented

    @abc.abstractmethod
    def header_line(self):
        """
        Checks that :
        • W ( 1 ≤ W ≤ 10**3 ) – the width of the assembly workspace (columns)
        • H ( 1 ≤ H ≤ 10 **3) - the height of the assembly workspace(rows)
        • R ( 1 ≤ R ≤ 10 **2) -  R ( 1 ≤ R ≤ 10 2 ) – the number of robotic arms available
        • M ( R ≤ M ≤ 10**3) - the number of mount point
        • T ( 1 ≤ T ≤ 10**3 ) - the number of tasks available
        • L ( 1 ≤ L ≤ 10**4 ) -  the number of total steps for the assembly process
        """
        raise NotImplemented

    @abc.abstractmethod
    def the_grid(self):
        """
        Initialises a w * h grid
        """


    @abc.abstractmethod
    def mount_points(self):
        """
         • Gets the mount points from the input file
         • Assigns the mount points to the grid
         • Checks constraints
         • x ( 0 ≤ x < W ) and y ( 0 ≤ y < H ) describing the coordinates
        """


    @abc.abstractmethod
    def get_tasks(self):
        """
        • Gets the tasks from the input file
        • Checks constraints
        • Gets the assembly points from the input file
        • Assigns the assembly points to the grid
        • S ( 1 ≤ S ≤ 10**6 )  P ( 1 ≤ P ≤ 10  **3)  ← First line
        • x 0 , y 0 , x 1 , y 1 , ..., x P-1 , y P-1  ← Second line
        """




class SmartPhones(Interface):

    CORRECT_SPACE_PATTERN = r'([^\s]+)'

    def __init__(self,input_file):

        self.width = None
        self.height = None
        self.factory_dict = {}
        self.grid = []
        self.input_file = input_file


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
        Checks that :
        • W ( 1 ≤ W ≤ 10**3 ) – the width of the assembly workspace (columns)
        • H ( 1 ≤ H ≤ 10 **3) - the height of the assembly workspace(rows)
        • R ( 1 ≤ R ≤ 10 **2) -  R ( 1 ≤ R ≤ 10 2 ) – the number of robotic arms available
        • M ( R ≤ M ≤ 10**3) - the number of mount point
        • T ( 1 ≤ T ≤ 10**3 ) - the number of tasks available
        • L ( 1 ≤ L ≤ 10**4 ) -  the number of total steps for the assembly process
        """

        first_line = self.reads_text(file_name=self.input_file)[0]

        first_line = re.findall(self.CORRECT_SPACE_PATTERN, first_line)

        digits = len(first_line)

        if digits != 6 or digits > 6:
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
        • W ( 1 ≤ W ≤ 10**3 ) 
        • H ( 1 ≤ H ≤ 10 **3) 
        • R ( 1 ≤ R ≤ 10 **2) 
        • M ( R ≤ M ≤ 10**3) 
        • T ( 1 ≤ T ≤ 10**3 ) 
        • L ( 1 ≤ L ≤ 10**4 ) 
        """
        for index, number in enumerate(first_line):

            number = int(number)

            if number > 10**3:
                if index == 0:
                    print(error_handles[2])
                    return
                if index == 1:
                    print(error_handles[2])
                    return
                if index == 3:
                    print(error_handles[3])
                    return
                if index == 4:
                    print(error_handles[4])
                    return

            if number > 10**2:
                if index == 2:
                    print(error_handles[5])
                    return

            if number > 10**4:
                if index == 5:
                    print(error_handles[6])
                    return

        factory_dict = {}

        factory_dict["width"] = first_line[0]
        factory_dict["height"] = first_line[1]
        factory_dict["arms"] = first_line[2]
        factory_dict["mount_points"] = first_line[3]
        factory_dict["tasks"] = first_line[4]
        factory_dict["steps"] = first_line[5]

        self.width = first_line[0]
        self.height = first_line[1]

        self.factory_dict.update(factory_dict)

        print(self.factory_dict)




    def the_grid(self):
        """
        Initialises a w * h grid
        """
        w = self.width
        h = self.height

        #the_grid = np.full((h, w), "E", dtype=object)
        the_grid= [['E' for _ in range(w)] for _ in range(h)]

        the_grid[1][1] = 'M'
        the_grid[1][3] = 'M'


        self.grid = the_grid

        print(self.grid)

        for row in self.grid:
            print(row)

        time.sleep(1000)




    def mount_points(self):
        """
         • Gets the mount points from the input file
         • Assigns the mount points to the grid
         • Checks constraints
         • x ( 0 ≤ x < W ) and y ( 0 ≤ y < H ) describing the coordinates
        """
        print(self.factory_dict)

        point_range = 1+self.factory_dict["mount_points"]

        mount_points = self.reads_text(file_name=self.input_file)[1:point_range]

        mount_points = [x.strip() for x in mount_points]

        for mount in mount_points:

            x = int(mount.split(' ')[0])
            y = int(mount.split(' ')[-1])

            self.grid[x][y] = 'M'

        print(self.grid[3][2],'@@@@')

        print(self.grid)

        #for x in self.grid:
            #print(x)

        #for row in reversed(self.grid):
            #print(row)








        #print(self.grid)

        indices = np.where(self.grid == 'M')
        print(indices,'<--Found in np' )
        print(mount_points,'<--Should be =M')











    def get_tasks(self):
        """
        • Gets the tasks from the input file
        • Checks constraints
        • Gets the assembly points from the input file
        • Assigns the assembly points to the grid
        • S ( 1 ≤ S ≤ 10**6 )  P ( 1 ≤ P ≤ 10  **3)  ← First line
        • x 0 , y 0 , x 1 , y 1 , ..., x P-1 , y P-1  ← Second line
        """
        point_range = 1 + self.factory_dict["mount_points"]

        tasks = self.reads_text(file_name=self.input_file)[point_range:]

        tasks = [x.strip() for x in tasks]
        tasks = [tasks[i:i + 2] for i in range(0, len(tasks), 2)]

        for i, inner_list in enumerate(tasks):

            for j, element in enumerate(inner_list):

                score = int(element.split(' ')[0])


                """
                Checks he constraints here 
                """
                if score >10**6:
                    print(error_handles[7])
                    return

                assembly_points = int(element.split(' ')[-1])

                if assembly_points > 10 ** 3:
                    print(error_handles[8])
                    return

            """
            Assembly coordinates
            """
            for x in inner_list:
                second_element = inner_list[1]
                numbers = second_element.split(' ')
                grouped_numbers = [numbers[i:i + 2] for i in range(0, len(numbers), 2)]


            assembly_coordinates = [''.join(sublist) for sublist in grouped_numbers]

            for assembly in assembly_coordinates:

                x = int(assembly[0])
                y = int(assembly[1])

                #self.grid[y][x] = 'A'



        #for lst in reversed(self.grid):
            #print(lst)





















































