"""Soccer analysis library"""
from __future__ import division
import csv 
import matplotlib.pyplot as plt 

def listH(header,filename,ubound,lbound):
	with open(filename,'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',') # skips the first row
			for row in reader:
				for x in range(ubound,lbound):
					header.append(row[x])
	return header				


def valuesTwo(header, num_two):
	"""Prints the rest of the data minus the header"""
	a = 0
	trueValues = []
	for x in header:
		trueValues.append(x) 

	while (a < num_two):
		del trueValues[:1]
		a = a +1
		
	return trueValues			

def key(header, num_two):
	"""This prints the key header from the csv file"""
	key = []
	x = 1
	if x !=0:
		for x in header:
			for x in range(num_two):
				key.append(header[x])
			break	
		x-=1		
	return key	

def findPlayer(header):
	"""This is used to find the player within the csv file"""
	test_list = []
	string = raw_input("Please input a player name (first letter is capitilized): ")	
	for x in header:
		# place a while loop 
		if x == string:
			y = 1
			adj = header.index(string)
			if y !=0:
				for y in header:
					for y in range(adj, num_two+adj):
						test_list.append(header[y])	
					break
				break		
			y-=1

	return test_list

def getAverage(array,sec):
	"""A function that gets the mean of a column"""
	new_a = array[0]
	size = len(sec)
	if size == 0:
		return 0
	else:	
		total = 0
		for x in sec:
			total+= int(x)
		new_tot = total/size
		print "The average for %s in the season is %5.3f" % (new_a, (new_tot)) 

def playerComparison(first, sec):
	"""A function that compares two players"""
	# The efficency metric will be the sum of 
	# The possession, attack, and goals
	efficency_one = 0
	efficency_two = 0

	for y in range(0, len(first)):
		if y==5:
			efficency_one+=int(first[y]) 
		elif y==6:
			efficency_one+=int(first[y])
		elif y==8:
			efficency_one+=int(first[y])

	for y in range(0, len(sec)):
		if y==5:
			efficency_two+=int(sec[y]) 
		elif y==6:
			efficency_two+=int(sec[y])
		elif y==8:
			efficency_two+=int(sec[y])
 
	# This will compute to see if the players are similar 
	# in terms of efficency
	if (abs(efficency_one - efficency_two) <= 75):
		print "%s is similar to %s in terms of efficency." % (first[0],sec[0])
		print "The efficency"
	else:
		print "The players inputed are not similar in terms of efficency."
		if efficency_one > efficency_two:
			print "%s is more efficent." % (first[0])
		if efficency_one < efficency_two:
			print "%s is more efficent." % (sec[0])	

	# Matplotlib implementation of player comparison		
	plt.title("Efficency of Players")
	plt.ylabel("Efficency Points")
	plt.bar(0, efficency_one, color='r',width=0.5)
	plt.bar(1, efficency_two, color='b',width=0.5)
	plt.text(0, efficency_one+4,s=first[0], fontsize=12)
	plt.text(1, efficency_two+4,s=sec[0], fontsize=12)
	plt.show()		

def playerComparisonShotAverage(first, sec):
	compare_one = first[13]
	compare_two = sec[13] 
	print "The shot accuracy of %s is %s" % (first[0], compare_one)
	print "The shot accuracy of %s is %s" % (sec[0], compare_two)


