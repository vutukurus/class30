import os
import subprocess

def prime_generator(input_list):

	new_list=[]  # Used to hold prime numbers
	for i in input_list:
		if isinstance(i,str):
			return "donotpassstring"
		if i % 2 == 0:
			new_list.append(i)
	return new_list
	














