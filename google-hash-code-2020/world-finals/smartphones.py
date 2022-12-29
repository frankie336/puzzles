from large_lists import error_handles
import abc
import time
import re
import numpy as np
from collections import defaultdict
from math import sqrt


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
                callable(subclass.globally_optimum_mount_points) and


                hasattr(subclass, 'assign_robot_arms') and
                callable(subclass.assign_robot_arms) and

                hasattr(subclass, 'work_scheduler') and
                callable(subclass.work_scheduler) and

                hasattr(subclass, 'robot_worker') and
                callable(subclass.robot_worker) or

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
        • Euclidean distance between the mount point and the first assembly point of each task:
         (x1, y1) and (x2, y2) is calculated as sqrt((x1 - x2)**2 + (y1 – y2)**2)
        • Sets the globally optimum mount point list object
        """
        raise NotImplemented


    @abc.abstractmethod
    def assign_robot_arms(self):
        """
        Assigns robot arms to optimised mount points
        """
        raise NotImplemented



    @abc.abstractmethod
    def work_scheduler(self):
        """
        • Schedules work among robot arms
        • Round robin
        • Initially assigns all tasks
        • Tasks can be later filtered by available steps
        """
        raise NotImplemented


    @abc.abstractmethod
    def robot_worker(self):
        """

        :return:
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
        self.global_mount_point_list = []
        self.task_assembly_points = []
        self.global_schedule_dict = {}


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

        self.grid = [[0 for _ in range(nx)] for _ in range(ny)]

        for row in self.grid:
            print(row,'<--The original grid')
        print('\n')







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

            self.grid[y][x] = 1

        for row in  reversed(self.grid):
            print(row,'<---The lists with 1 for mounts. Row order reversed')
        print("\n")






    def get_tasks(self):
        """
        • Gets the tasks from the input file
        • Checks constraints
        • Gets the assembly points from the input file
        • Assigns the assembly points to the grid
        • S ( 1 ≤ S ≤ 10**6 )  P ( 1 ≤ P ≤ 10  **3)  ← First line
        • x 0 , y 0 , x 1 , y 1 , ..., x P-1 , y P-1  ← Second line
        • Makes a list of tasks
        """
        point_range = 1 + self.factory_dict["mount_points"]

        tasks = self.reads_text(file_name=self.input_file)[point_range:]

        tasks = [x.strip() for x in tasks]
        tasks = [tasks[i:i + 2] for i in range(0, len(tasks), 2)]

        self.tasks_list.extend(tasks)

        print(self.tasks_list,'\n','<---score, # assemblies, assembly references')
        print("\n")


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
                self.grid[y][x] = 2


        for row in reversed(self.grid):
            print(row, '<---The lists with 2 for assembly points. Row order reversed')

        for row in self.grid:
            print(row,'<---None reversed grid')



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
        [(0, [[3, 2], [3, 3]], 10), (1, [[0, 4]], 5), (2, [[3, 3]], 1)]
        """
        scores = [(x,) for x in scores_list]
        self.task_assembly_points = [(ap, int(score[0])) for ap, score in zip(assembly_locations, scores)]

        self.task_assembly_points = [((i,) + task) for i, task in enumerate(self.task_assembly_points)]

        print('\n',self.task_assembly_points,'<----Tasks, assembly points, and scores!')




    def globally_optimum_mount_points(self):
        """
        • Euclidean distance between the mount point and the first assembly point of each task:
         (x1, y1) and (x2, y2) is calculated as sqrt((x1 - x2)**2 + (y1 – y2)**2)
        • Sets the globally optimum mount point list object
        """
        tasks_assembly = sorted(self.task_assembly_points, key=lambda x: x[1], reverse=True)

        print(tasks_assembly, '<-----Assembly Points + Scores')

        mount_points = []

        counter = 0

        # Iterate the tasks
        for task in tasks_assembly:
            counter+=1
            print(counter,'<-----Finding global optimum mounts')
            # Get the assembly points of the task
            assembly_points = task[1]
            # Find the mount point closest to the assembly points
            closest_mount_point = None
            closest_distance = float("inf")
            for assembly_point in assembly_points:
                for i in range(len(self.grid)):
                    for j in range(len(self.grid[0])):
                        if self.grid[i][j] == 1:  # Check if the current cell is a mount point
                            # Calculate the distance between the assembly point and the mount point
                            distance = abs(i - assembly_point[0]) + abs(j - assembly_point[1])
                            if distance < closest_distance:  # Update the closest mount point if the current mount point is closer
                                closest_mount_point = (i, j)
                                closest_distance = distance
            # Add the closest mount point to the list
            mount_points.append(closest_mount_point)

        """
        make a list that removes duplicate entries since mounts can be used once
        
        Further filter this list to the first n number of mounts where n is the number of 
        robot arms   
        """
        arms_number = self.factory_dict["arms"]
        unique_optimal_mounts = [x for i, x in enumerate(mount_points) if x not in mount_points[:i]]
        unique_optimal_mounts = unique_optimal_mounts[:arms_number]

        """
        Set the globally optimal mount points object
        """
        self.global_mount_point_list = unique_optimal_mounts
        print(self.global_mount_point_list,'<------Globally optimum mount points')





    def assign_robot_arms(self):
        """
        Assigns robot arms to optimised mount points
        Candidate mount points are turned to 3
        """
        for mount in self.global_mount_point_list:
            for inner in self.global_mount_point_list:

                x = inner[0]
                y = inner[1]
                self.grid[x][y] = 3

        print('\n')
        for row in reversed(self.grid):
            print(row,'<----Grid with robot arms added')



    def work_scheduler(self):
        """
        • Schedules work among robot arms
        • Round robin
        • Initially assigns all tasks
        • Tasks can be later filtered by available steps
        """

        robot_arms = self.global_mount_point_list

        tasks = self.task_assembly_points

        # Dictionary to store the tasks assigned to each robot arm
        assigned_tasks = {}

        # Sort tasks by their score
        tasks.sort(key=lambda x: x[1], reverse=True)


        #Assign tasks to robot arms using round robin
        for i, task in enumerate(tasks):
            # Get the coordinates of the first assembly point
            assembly_point = task[1][0]

            # Find the robot arm closest to the assembly point
            min_distance = float("inf")
            min_distance_arm = None
            for arm in robot_arms:
                distance = sqrt((arm[0] - assembly_point[0]) ** 2 + (arm[1] - assembly_point[1]) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    min_distance_arm = arm

            # Assign the task to the closest robot arm
            if min_distance_arm in assigned_tasks:
                # If the robot arm is already assigned a task, add the current task to its list of tasks
                assigned_tasks[min_distance_arm].append(task)
            else:
                # If the robot arm is not assigned a task, create a new entry in the dictionary for it
                assigned_tasks[min_distance_arm] = [task]


        for arm, tasks in assigned_tasks.items():
            print(f"Robot arm at {arm} is assigned tasks: {tasks}")

        """
        Reorders the schedule based on highest value tasks first
        """
        self.global_schedule_dict = assigned_tasks
        self.global_schedule_dict = {k: sorted(v, key=lambda x: -x[2]) for k, v in assigned_tasks.items()}
        self.global_schedule_dict = {k: v for k, v in sorted(self.global_schedule_dict.items(), key=lambda item: item[0][-1])}

        print(self.global_schedule_dict,'<---Global Schedule')












    def move(self,pos, direction):
        x, y = pos
        if direction == "up":
            x -= 1
        elif direction == "down":
            x += 1
        elif direction == "left":
            y -= 1
        elif direction == "right":
            y += 1
        # Check if the new position is within the bounds of the room grid
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid[0]):
            return pos  # Return the original position if the new position is outside the room
        # Check if the new position is a wall or a cell containing the number 2
        if self.grid[x][y] in [1, 3]:
            return pos  # Return the original position if the new position is a wall or a cell containing the number 2
        return (x, y)  # Return the new position if it is a valid position within the room




    def automate_movement(self,start, target):
        """
        Function to calculate the shortest
        path from the start position to
        the target position
        """

        # Initialize a queue to store the positions to be explored
        queue = [(start, [])]
        # Initialize a set to store the visited positions
        visited = set()
        # Iterate over the positions in the queue
        while queue:
            pos, moves = queue.pop(0)  # Get the current position and moves made
            # Check if the current position is the target position
            if pos == target:
                return moves  # Return the moves if the current position is the target position
            # Mark the current position as visited
            visited.add(pos)
            # Try moving in each direction
            for direction in ["up", "down", "left", "right"]:
                new_pos = self.move(pos, direction)  # Get the new position after moving in the current direction
                if new_pos not in visited:  # Check if the new position has not been visited
                    queue.append((new_pos, moves + [direction]))  # Add the new position and updated moves to the queue
        return "Error: Target unreachable"  # Return an error message if the target position is not reached








    def robot_worker(self):
        """

        :return:
        """
        room = self.grid
        print("\n")
        for row in reversed(self.grid):
            print(row,'<----Robots working on this grid')

        test_start = self.grid[3][1]

        # Initialize starting and target positions
        start = (3,2)

        target = (3, 3)

        # Calculate the shortest path from the start position to the target position
        moves = self.automate_movement(start, target)
        print(moves)




































































































