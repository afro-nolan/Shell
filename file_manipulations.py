#Name: Aifric Nolan

#This is a set of functions to manipulate files and command-line arguments

import os

def input_file_provided(args):
	"""Check if input file provided"""
	if "<" in args:
		input_file = args.split("<")[1].strip()
		if ">" in input_file:
			input_file = input_file.split(">")[0].strip()
		#If input file provided return input file
		return input_file
	else:
		return False

def output_file_provided(args):
	"""Check if output file provided"""
	if ">" in args:
		output_file = args.split(">")[1].strip()
		return output_file
	else:
		return False

def read_input(input_file):
	"""Read Commands from input file"""
	with open(input_file, "r") as f:
		commands = f.readlines()
	return commands

def write_to_file(output_file, content):
	"""Write to file"""
	with open(output_file) as f:
		for line in content:
			f.write(line.strip())

def argument_check(args):
	"""Check for IO Redirection"""
	#Check for input redirection
	if input_file_provided(args):
		function_args = args.split("<")[0].strip()
		if len(function_args) < 1:
			return False
	#Check for output redirection
	elif output_file_provided(args):
		function_args = args.split(">")[0].strip()
		if len(function_args) < 1:
			return False
	else:
		return False
	return function_args

def append_output(args):
	"""Check if output file provided to append output to"""
	if ">>" in args:
		output_file = args.split(">>")[1].strip()
		return output_file
	else:
		return False

def read_in_output_file(file_name):
	"""Reads in content of an output file for the uses of appending more output to it"""
	if os.path.isfile(file_name):
		with open(file_name) as f:
			content = f.readlines()
		content.append("\n") #Newline for readability
	else:
		content = []
	return content

