"""
Author: francis.neequaye@gmail.com

This program responds to Google Hash Code 2020 conception, world finals :
https://codingcompetitions.withgoogle.com/hashcode/archive.
This is meant for demonstration purposes, and may be freely used, and adapted.
"""

from smartphones import SmartPhones
def main():

    run = SmartPhones(input_file)
    run.header_line()
    run.the_grid()
    run.mount_points()
    run.get_tasks()
    run.assembly_points_to_scores()
    #run.optimum_mount_points_per_task()
    run.globally_optimum_mount_points()


a = "a_example.txt"
b = "b_single_arm.txt"
c = "c_few_arms.txt"
d = "d_tight_schedule.txt"
e = "e_dense_workspace.txt"
f = "f_decentralized.txt"

if __name__ == "__main__":
    input_file = "input/final_round_2020.in/"+a
    main()

