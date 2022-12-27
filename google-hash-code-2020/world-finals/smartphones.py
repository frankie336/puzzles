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

                hasattr(subclass, 'assembly_points_to_scores') and
                callable(subclass.tasks_ranking) and

                hasattr(subclass, 'globally_optimum_mount_points') and
                callable(subclass.globally_optimum_mount_points) or

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
    def assembly_points_to_scores(self):
        """
        • Ranks task value
        """
        raise NotImplemented




    @abc.abstractmethod
    def globally_optimum_mount_points(self):

        """
        • Calculates globally optimum mount points * available robot arms
        • Mixed-integer programming (MIP)
        • mount points for the given assembly points, based on their distances from the mount points using Euclidean distance


        1. Define the decision variables:
          • For each mount point, create a binary variable x[i] that represents whether a robot arm is placed at the mount point.
          • For each task, create an integer variable y[i] that represents the number of robot arms used for the task.

        2. Define the objective function:
          • The objective is to maximize the total score for all tasks, so the objective function would be:
          maximize sum(score[i] * y[i] for i in tasks)

        3. Define the constraints:
          • For each task, ensure that the number of robot arms used is less than or equal to the maximum number of arms:
            y[i] <= max_arms

        • For each assembly point, ensure that at least one robot arm is placed within 4 cells of the assembly point:
          sum(x[j] for j in mount_points if distance(assembly_point[i], mount_point[j]) <= 4) >= 1

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
        self.optimal_mount_points_list= []
        self.task_assembly_points = []


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

            self.grid[y][x] = "M"

        #print(self.grid)
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
                Checks the constraints here 
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

                self.grid[y][x] = "A"

        arr_reversed = self.grid[::-1]
        #print(arr_reversed)



    def assembly_points_to_scores(self):
        """
        • Maps Task Assembly Points to scores by combing both in a list of tuples
        """


        """
        split score list
        """
        scores_list = [element[0].split()[0] for element in self.tasks_list]


        """
        splitting and converting the assembly list
        to usable coordinates 
        
        Convert the assembly lists to coordinates  
        """
        assemly_list = [[element[1]] for element in self.tasks_list]#1
        assemly_list = [element[0].replace(' ', '') for element in assemly_list]#2
        assemly_list = [re.findall(r'\d{2}', element) for element in assemly_list]#3


        assembly_point_list = []

        for inner_list in assemly_list:
            new_inner_list = []

            for element in inner_list:
                new_inner_list.append([int(x) for x in element])
            assembly_point_list.append(new_inner_list)

        assembly_locations = [[[int(x[1]), int(x[0])] for x in element] for element in assembly_point_list]#NUMBERS REVERSED


        """
        Combine assembly locations and scores to form structure:
        [([[3, 2], [3, 3]], 10), ([[0, 4]], 5), ([[3, 3]], 1)]
        """
        scores = [(x,) for x in scores_list]
        self.task_assembly_points = [(ap, int(score[0])) for ap, score in zip(assembly_locations, scores)]




    def globally_optimum_mount_points(self):
        """
        • Calculates globally optimum mount points * available robot arms
        • Mixed-integer programming (MIP)
        • mount points for the given assembly points, based on their distances from the mount points using Euclidean distance

        1. Define the decision variables:
          • For each mount point, create a binary variable x[i] that represents whether a robot arm is placed at the mount point.
          • For each task, create an integer variable y[i] that represents the number of robot arms used for the task.

        2. Define the objective function:
          • The objective is to maximize the total score for all tasks, so the objective function would be:
          maximize sum(score[i] * y[i] for i in tasks)

        3. Define the constraints:
          • For each task, ensure that the number of robot arms used is less than or equal to the maximum number of arms:
            y[i] <= max_arms

        • For each assembly point, ensure that at least one robot arm is placed within 4 cells of the assembly point:
          sum(x[j] for j in mount_points if distance(assembly_point[i], mount_point[j]) <= 4) >= 1

        """

        tasks = self.task_assembly_points
        print(tasks, '<-----Assembly Points + Scores')

        grid = self.grid
        arr_reversed = self.grid[::-1]#printing the grid in reverse is cosmentic
        print(arr_reversed)

        max_arms = self.factory_dict["arms"]

        mount_points = np.argwhere(grid == 'M')

        scores = []

        optimal_mount_points_list = []

        for task_id, task in enumerate(tasks):
            assembly_points, score = task

            optimal_mount_points = []

            for assembly_point in assembly_points:
                shortest_paths = np.full((len(mount_points), 1), np.inf)

                shortest_paths[:, 0] = np.sqrt(
                    (mount_points[:, 0] - assembly_point[0]) ** 2 + (mount_points[:, 1] - assembly_point[1]) ** 2)

                sorted_indices = np.argsort(shortest_paths, axis=0)
                optimal_mount_points.append(mount_points[sorted_indices])

            optimal_mount_points = np.concatenate(optimal_mount_points)
            num_arms = min(max_arms, len(optimal_mount_points))

            scores.append(score * num_arms)

            optimal_mount_points_list.append(optimal_mount_points[:num_arms])


        optimal_mount_points_list = [x.tolist() for x in optimal_mount_points_list]

        max_opt = len(optimal_mount_points)

        max_arms_range = min(max_arms,max_opt)

        optimal_mount_points_list = optimal_mount_points_list[0]

        self.optimal_mount_points_list = optimal_mount_points_list

        print(scores,'<----Scores')
        print(self.optimal_mount_points_list,'<------Optimal Mounts')
        print(len(self.optimal_mount_points_list),'<----Number of robot arms deployed')

        #return scores, optimal_mount_points_list



































































































