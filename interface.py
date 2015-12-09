"""Interface of program"""
import soccer_analysis as sa 
import soc_learn as learn 
import numpy as py 

# Empty lists for the interface 
header = []

# The bounds and the file name for implementation of the program
iter_num = int(raw_input("Put in lower bounds for categories: "))
iter_num_two = int(raw_input("Put in upper bounds for categories: "))
filename = raw_input("Please input a file name: ") 

# Implementation of functions from soccer analy library
a = sa.listH(header,filename, iter_num, iter_num_two)
list_two = sa.valuesTwo(a,iter_num_two)
independent = sa.key(header, iter_num_two)

# Input of a number so that it will access array
s = int(raw_input("Please input a number for the column: "))
array = py.genfromtxt(filename, delimiter=',', dtype= (str, int))
new_a = array[:,s]
new_a_two = array[1:,s]
avg = sa.getAverage(new_a, new_a_two)

# Player comparision 
player_one = int(raw_input("Please input the row of the first player: "))
player_two = int(raw_input("Please input the row of the second player: "))

player_one_arr = array[player_one]
player_two_arr = array[player_two]

# Calls the soccer analysis library fun for 
# efficency 
sa.playerComparison(player_one_arr, player_two_arr)

# Calls the soccer analysis library methdod for 
# shot accuracy  
sa.playerComparisonShotAverage(player_one_arr, player_two_arr)  

#Calls the soc learn library method for the Random Forest regressor
alg = learn.random_forest(filename)
print "The average number of goals based on the learning algorithm is %f" % (alg)



