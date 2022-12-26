from large_lists import error_handles
import abc
import time
import re
import numpy as np
from collections import defaultdict


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
                callable(subclass.get_tasks) and

                hasattr(subclass, 'task_ranking') and
                callable(subclass.tasks_ranking) and

                hasattr(subclass, 'where_robotic_arms_installed') and
                callable(subclass.where_robotic_arms_installed) or

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

        raise NotImplemented


    @abc.abstractmethod
    def mount_points(self):
        """
         • Gets the mount points from the input file
         • Assigns the mount points to the grid
         • Checks constraints
         • x ( 0 ≤ x < W ) and y ( 0 ≤ y < H ) describing the coordinates
        """
        raise NotImplemented


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
        raise NotImplemented

    @abc.abstractmethod
    def task_ranking(self):
        """
        • Ranks task value
        """
        raise NotImplemented




    @abc.abstractmethod
    def where_robotic_arms_installed(self):
        """
        • A modified Dijkstra's algorithm
        • Calculates the most optimal mount points per task+assembly points
        • Optimum mount points = where arms are installed
        • Number of arms  = min(arms,optimums)
        • In effect, ranks mount points
        • returns ordered list
        """
        raise NotImplemented




class SmartPhones(Interface):

    CORRECT_SPACE_PATTERN = r'([^\s]+)'

    def __init__(self,input_file):

        self.width = None
        self.height = None
        self.factory_dict = {}
        self.grid = []
        self.input_file = input_file
        self.tasks_list = []
        self.ranked_assembly_points = []


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
        nx, ny = self.width,self.height

        # Generate the grid of coordinates
        x, y = np.meshgrid(range(nx), range(ny))

        # Create a 2D array with the same dimensions as the grid and fill it with the value "E"
        self.grid = np.full((ny, nx), "E")




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

            self.grid[y][x] = 'M'

        #print(self.grid[2][3],'@@@@')
        #arr_reversed = self.grid[::-1]
        #print(arr_reversed)





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
        self.tasks_list.extend(tasks)

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

                self.grid[y][x] = 'A'

        arr_reversed = self.grid[::-1]
        print(arr_reversed)



    def task_ranking(self):
        """
        • Ranks task value
        """
        task_number = self.factory_dict["tasks"]

        task_scores = []

        print(self.tasks_list)

        scores_list = [element[0].split()[0] for element in self.tasks_list]

        for s in scores_list:

            score = int(s)/task_number
            task_scores.append(score)



        task_ranking_dict = {i: element for i, element in enumerate(task_scores)}
        task_ranking_dict = sorted(task_ranking_dict.items(), key=lambda x: x[1], reverse=True)
        task_ranking_dict = dict(task_ranking_dict)

        print(task_ranking_dict)

        print(self.tasks_list)

        print(self.grid)

        return task_ranking_dict





    def where_robotic_arms_installed(self):
        """
        • A modified Dijkstra's algorithm
        • Calculates the most optimal mount points per task+assembly points
        • Optimum mount points = where arms are installed
        • Number of arms  = min(arms,optimums)
        • In effect, ranks mount points
        • returns ordered list
        """

        assemly_list = [[element[1]] for element in self.tasks_list]
        assemly_list = [element[0].replace(' ', '') for element in assemly_list]
        assemly_list =  [re.findall(r'\d{2}', element) for element in assemly_list]

        """
        Covert the assembly lists to coordinates 
        """
        assembly_point_list = []

        ranked_assembly_points = []

        for inner_list in assemly_list:
            new_inner_list = []
            for element in inner_list:
                new_inner_list.append([int(x) for x in element])
            assembly_point_list.append(new_inner_list)

        assembly_point_list = [[[int(x[1]), int(x[0])] for x in element] for element in assembly_point_list]#NUMBERS REVERSED

        grid = self.grid

        #define the mount points
        mount_points = np.argwhere(grid == 'M')

        for point in assembly_point_list:

            assembly_points = point

            print(f"Assembly points: {assembly_points}")

            # create an array to store the shortest path for each arm
            shortest_paths = np.full((len(mount_points), len(assembly_points)), np.inf)

            # initialize the first column of the shortest_paths array with the distance from each mount point to the first assembly point
            shortest_paths[:, 0] = np.abs(mount_points[:, 0] - assembly_points[0][0]) + np.abs(mount_points[:, 1] - assembly_points[0][1])

            # iterate through the rest of the assembly points and update the shortest_paths array
            for i in range(1, len(assembly_points)):
                for j in range(len(mount_points)):
                    shortest_paths[j, i] = min(
                        shortest_paths[j, i - 1] + np.abs(mount_points[j, 0] - assembly_points[i][0]) + np.abs(
                            mount_points[j, 1] - assembly_points[i][1]),
                        shortest_paths[j, i])



            # get the indices of the sorted shortest paths array
            sorted_indices = np.argsort(shortest_paths, axis=0)

            # get the optimal mount points in order
            optimal_mount_points = mount_points[sorted_indices]

            max_arms = self.factory_dict["arms"]
            optimal_mount_points = optimal_mount_points[:max_arms]

            print(f"Optimal mount points: {optimal_mount_points}")

            print(len(optimal_mount_points), '<-----')

            ranked_assembly_points.append(assembly_points)



        ranked_assembly_points = ranked_assembly_points[:max_arms]
        self.ranked_assembly_points.extend(ranked_assembly_points)

        print(self.ranked_assembly_points,'<----')












































































