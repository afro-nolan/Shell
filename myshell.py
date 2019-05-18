#Name: Aifric Nolan

import cmd
import os
import time
import curses_functions as cf
import sys
import subprocess
import file_manipulations as fm
import curses
import threading

class myShell(cmd.Cmd):

	#Prompt displayed in terminal. 
	prompt = "shell=" + os.getcwd() + " >"

	def do_quit(self, args):
		"""Quits shell"""
		print("Quitting...")
		raise SystemExit

	def update_prompt(self):
		"""Function to update prompt when directory changed."""
		self.prompt = "shell=" + os.getcwd() + " >"

	def do_clr(self, args):
		"""Clears Screen"""
		clear = lambda: os.system('clear')
		clear()

	def do_commands(self, args):
		"""Provides a list of commands and supports IO re direction"""
		#Read user manual
		with open("readme") as f:
			content = f.read().split("\n")
		#Check if output file provided for io redirection
		output_file_check = fm.output_file_provided(args)
		#If you don't need to append output to a file
		if fm.append_output(args) is False:
			#If you need to write output to file
			if output_file_check is not False:
				#Open output file
				with open(output_file_check, "w") as f:
					f.write("List of commands: \n")
					i = 0
					while i < len(content) and i+1 < len(content):
						#Parse manual for commands 
						if content[i].split(":")[0] == "Command":
							f.write(content[i] + "\n")
							i += 2
						i += 1
				
			#Don't need to write output to file
			else:
				print("List of commands: \n")
				i = 0
				while i < len(content) and i+1 < len(content):
					#Search for commands in manual
					if content[i].split(":")[0] == "Command":
						print(content[i])
						i += 2
					i += 1
		#If you need to append output to file
		else:
			#Content to be outputted to file
			output_content = []
			output_content.append("List of commands: \n")
			i = 0
			#Parse manual for commands and append
			while i < len(content) and i+1 < len(content):
						if content[i].split(":")[0] == "Command":
							output_content.append(content[i] + "\n")
							i += 2
						i += 1
			#Write all back to output file
			with open(fm.append_output(args), "a") as f:
				f.write("".join(output_content))

	def do_concepts(self, args):
		"""Provides a list of concepts and supports IO re-direction"""
		#Read user manual
		with open("readme") as f:
			content = f.read().split("\n")
		#Check if output file provided for io redirection
		output_file_check = fm.output_file_provided(args)
		#If you don't need to append output to a file
		if fm.append_output(args) is False:
			#If you need to write output to file
			if output_file_check is not False:
				#Open output file
				with open(output_file_check, "w") as f:
					f.write("List of Concepts: \n")
					i = 0
					while i < len(content) and i+1 < len(content):
						#Parse manual for commands 
						if content[i].split(":")[0] == "Concept":
							f.write(content[i] + "\n")
							i += 2
						i += 1
				
			#Don't need to write output to file
			else:
				print("List of Concepts: \n")
				i = 0
				while i < len(content) and i+1 < len(content):
					#Search for commands in manual
					if content[i].split(":")[0] == "Concept":
						print(content[i])
						i += 2
					i += 1
		#If you need to append output to file
		else:
			#Content to be outputted to file
			output_content = []
			output_content.append("List of Concepts: \n")
			i = 0
			#Parse manual for commands and append
			while i < len(content) and i+1 < len(content):
						if content[i].split(":")[0] == "Concept":
							output_content.append(content[i] + "\n")
							i += 2
						i += 1
			#Write all back to output file
			with open(fm.append_output(args), "a") as f:
				f.write("".join(output_content))


	def do_dir(self, args):
		"""Lists contents of a directory"""
		path = "."
		if fm.append_output(args) is False: #Check if we need to append output to file
			output_file_check = fm.output_file_provided(args) #Check if there is an output file
			if output_file_check is not False: #If we do need to write results to file
				with open(output_file_check, "w") as f: #Open file to write
					args = args.strip().split(">")[0].split() #Get data after '>' which should be dir name if any
					#If more than one directory name given, joins them into a path.
					if len(args) > 1:
						path = "/".join(args)
					elif len(args) == 1: #If only one dir given, make that the path
						path = args[0]
					#If it is not a directory, notify user.
					if not os.path.isdir(path):
						f.write("{} is not a directory.".format(path))
						return
					files = os.listdir(path)
					#Display details of contents of directory in readable format.
					f.write("{:{:d}s} {:{:d}s}".format("\nPath:", 16, path, 15))
					for name in files:
						f.write("{}{:{:d}s} {:{:d}s}".format(" ", "Name:", 15, name, 15))
						full_path = os.path.join(path, name)
						f.write("{}{:{:d}s} {:{:d}s}".format(" ", "Full path:", 15, str(full_path), 15))
						inode = os.stat(full_path)
						f.write("{}{:{:d}s} {:{:d}s}".format(" ", "Size: ", 15, str(inode.st_size), 15))
						f.write("{}{:{:d}s} {:{:d}s}".format(" ","Mode: ", 15, str(inode.st_mode), 15))
						if os.path.isdir(full_path):
							f.write("{}{:{:d}s} {:{:d}s}\n".format(" ", "Type:", 15, "dir", 15))
						elif os.path.isfile(full_path):
							f.write("{}{:{:d}s} {:{:d}s}\n".format(" ","Type:", 15, "file", 15))
			#Don't need to write output to file
			else:
				args = args.strip().split()
				#If more than one directory name given, joins them into a path.
				if len(args) > 1:
					path = "/".join(args)
				elif len(args) == 1:
					path = args[0]
				#If it is not a directory, notify user.
				if not os.path.isdir(path):
					print("{} is not a directory.".format(path))
					return
				files = os.listdir(path)
				#Display details of contents of directory in readable format.
				print("{:{:d}s} {:{:d}s}".format("Path:", 16, path, 15))
				for name in files:
					print("{}{:{:d}s} {:{:d}s}".format(" ", "Name:", 15, name, 15))
					full_path = os.path.join(path, name)
					print("{}{:{:d}s} {:{:d}s}".format(" ", "Full path:", 15, str(full_path), 15))
					inode = os.stat(full_path)
					print("{}{:{:d}s} {:{:d}s}".format(" ", "Size: ", 15, str(inode.st_size), 15))
					print("{}{:{:d}s} {:{:d}s}".format(" ","Mode: ", 15, str(inode.st_mode), 15))
					if os.path.isdir(full_path):
						print("{}{:{:d}s} {:{:d}s}\n".format(" ", "Type:", 15, "dir", 15))
					elif os.path.isfile(full_path):
						print("{}{:{:d}s} {:{:d}s}\n".format(" ","Type:", 15, "file", 15))
		#Need to append output to a file
		else:
			#output_content = fm.read_in_output_file(fm.append_output(args)) #Get file name and read its content if it exists
			output_content = []
			output_file = fm.append_output(args)
			args = args.strip().split(">>")[0].split() #Get args which should be dir names
			if len(args) > 1: #If there are more than one, join them to make path
					path = "/".join(args)
			elif len(args) == 1: #If one, put that as path
					path = args[0]
			#If it is not a directory, notify user.
			if not os.path.isdir(path):
				output_content.append("{} is not a directory.".format(path))
				return
			files = os.listdir(path) 
			#Directory details
			output_content.append("{:{:d}s} {:{:d}s}".format("Path:", 16, path, 15))
			for name in files:
				output_content.append("{}{:{:d}s} {:{:d}s}".format(" ", "Name:", 15, name, 15))
				full_path = os.path.join(path, name)
				output_content.append("{}{:{:d}s} {:{:d}s}".format(" ", "Full path:", 15, str(full_path), 15))
				inode = os.stat(full_path)
				output_content.append("{}{:{:d}s} {:{:d}s}".format(" ", "Size: ", 15, str(inode.st_size), 15))
				output_content.append("{}{:{:d}s} {:{:d}s}".format(" ","Mode: ", 15, str(inode.st_mode), 15))
				if os.path.isdir(full_path):
					output_content.append("{}{:{:d}s} {:{:d}s}\n".format(" ", "Type:", 15, "dir", 15))
				elif os.path.isfile(full_path):
					output_content.append("{}{:{:d}s} {:{:d}s}\n".format(" ","Type:", 15, "file", 15))
			with open(output_file, "a") as f_out: #Write all back into output file
				f_out.write("".join(output_content))

	def do_echo(self, args):
		"""Displays comment on newline."""
		if fm.append_output(args) is False: #Check if we need to append output to file
			output_file_check = fm.output_file_provided(args) #Get output file if one, else False
			if output_file_check is not False: #If there is an output file
				with open(output_file_check, "w") as f: #Write args to file
					f.write(" ".join(args.strip().split(">")[0].split()))
			else: #No output file, print to screen on newline
				print(" ".join(args.strip().split())) 
		#Need to append to file
		else:
			output_content = []
			output_content.append("\n ".join(args.strip().split(">>")[0].split())) #Append echo comment to file content
			with open(fm.append_output(args), "a") as f: #Write all back into file.
				f.write("".join(output_content))

	def do_cd(self, args):
		"""Changes current directory to <directory>"""
		#If no directory name given, display current working directory.
		if len(args.strip()) < 1:
			print(os.getcwd())
		else:
			#Check if directory_name is a directory.
			if os.path.isdir(args):
				os.chdir(args) # Change directory
				self.update_prompt() #Update prompt to reflect change
			#Notify user of file type.
			elif os.path.isfile(args):
				print("{} is a file, not a directory...".format(args))
			else:
				print("No such directory.")
		self.update_prompt()

	def do_pwd(self, args):
		"""Prints current working directory"""
		output_file_check = fm.output_file_provided(args) #Check if output file given
		if fm.append_output(args) is False: #If we don't need to append output to file
			if output_file_check is not False: #If we need to write output to file
				with open(output_file_check, "w") as f:
					f.write(os.getcwd()) #Write working directory to file
			#No output file; print to screen
			else:
				print(os.getcwd())
		#Need to append to file
		else:
			output_content = []
			output_content.append("\n") #Append newline for readablility
			output_content.append(os.getcwd()) #Current working directory
			with open(fm.append_output(args), "a") as f: #Write all content back to file
				f.write("".join(output_content))

	def do_help(self, args):
		"""Displays user manual, used by typing 'help <command> or '? <command>', if command ommitted shows whole
		user manual"""

		#Open readme manual
		with open("readme") as f:
			content = f.readlines()
		if fm.append_output(args) is False: #If we don't need to append output to file
			output_file_check = fm.output_file_provided(args) #If output file given
			if output_file_check is not False:  #Output file given
				with open(output_file_check, "w") as f: #Check if there are any arguments for command
					arguments = fm.argument_check(args)
					if arguments is False: #If not, write complete readme manual to file
						f.write("\n".join(content))
					#Arguments are given
					else:
						i = 0
						while i < len(content):
							line = content[i].strip().split()
							#Parse manual to find command user wants
							if len(line) > 0 and (line[0] == "Command:" or line[0] == "Concept:") and line[1] == arguments:
								f.write("{:s}\n".format(" ".join(line)))
								f.write("{:s}\n".format(" ".join(content[i+1].strip().split())))
								return
							i +=  1
						#If it exits loop without exiting function, item is not in readme manual
						f.write("Sorry, Cannot find what you are looking for...")
			#If no output file
			else:
				args = args.split()
				#If searching for a specific command
				if len(args) > 0:
					i = 0
					while i < len(content):
						line = content[i].strip().split() 
						#Parse manual to find command
						if len(line) > 0 and (line[0] == "Command:" or line[0] == "Concept:") and line[1] == args[0]:
							print("{:s}\n".format(" ".join(line)))
							print("{:s}\n".format(" ".join(content[i+1].strip().split())))
							return
						i +=  1
					
					#If it exits loop without exiting function, means item not in readme manual
					print("Sorry, Cannot find what you are looking for...")
				else:
					#Display full manual, (view 20 lines when space pressed)
					slices = len(content) % 20
					sections = ["".join(content[0:20])]
					for i in range(1,slices+1): #Append each 20 lines to list
						sections.append("".join(content[(i*20): (i*20) + 20]))
					print("{:>s}\n".format(sections[0].strip())) #print first 20 automatically
					j = 1 #index for next section
					sections = [paragraph for paragraph in sections if len(paragraph) >= 1]
					std = curses.initscr() #Intialise curses to get keyboard input
					c = cf.enable_curses(std) #Character of key press
					while j < len(sections):
						if c == 32: #If character is 'SpaceBar'
							cf.disable_curses(std) #Turn off curses
							print("{:>s}\n".format(sections[j].strip()))
							j += 1
						#stdscr = curses.initscr()
						c = cf.enable_curses(std) #Enable curses again
					cf.disable_curses(std) #Disable
					return
		#Append output to file
		else:
			filename = fm.append_output(args)
			output_content = []
			output_content.append("\n") #Append newline for readability
			args = args.split(">>")[0].strip().split() #Get arguments
			#If searching for a specific command
			if len(args) > 0:
				i = 0
				while i < len(content):
					line = content[i].strip().split()
					#Parse manual for command
					if len(line) > 0 and line[0] == "Command:" and line[1] == args[0]:
						output_content.append("{:s}\n".format(" ".join(line)))
						output_content.append("{:s}\n".format(" ".join(content[i+1].strip().split())))
						with open(filename, "a") as f_out: #Write all back to file
			  				f_out.write("".join(output_content))
			  				return
					i += 1

					
				#If it exits loop without exiting function, means item not in readme manual
				output_content.append("Sorry, Cannot find what you are looking for...")
				with open(filename, "a") as f:
							f.write("".join(output_content))
			else:
				#Writes full manual to file
				for lines in content:
					output_content.append(lines.strip() + "\n")
				with open(filename, "a") as f_out:
					f_out.write("\n".join(output_content))
				return

	def do_pause(self, args):
		"""Pauses program until Enter Pressed"""
		std = curses.initscr() #Initialise curses
		c = cf.enable_curses(std) #Character of key press
		while c != 10: #If keypress is not 'Enter'
			cf.disable_curses(std) #Turn off curses
			c = cf.enable_curses(std) #Character of key press
		cf.disable_curses(std) #Disable
		return

	def do_environ(self, args):
		"""Lists all environment strings """
		strings = os.environ #Is dictionary of all environment strings
		output_file_check = fm.output_file_provided(args) #Check for output file
		if fm.append_output(args) is False: #Don't need to append output to file
			if output_file_check is not False: #Write output to file
				with open(output_file_check, "w") as f:
					for k in strings:
						#Display in readable format.
						f.write(("{} : {}\n".format(k, strings[k])))
					f.write("\n") #Print new line
			else: #Print to screen
				for k in strings:
					#Display in readable format.
					print("{} : {}".format(k, strings[k]))
				print() #Print new line
		#Need to append to file
		else:
			filename = fm.append_output(args)
			output_content = []
			output_content.append("\n")
			for k in strings: #Append strings
				output_content.append(("{} : {}\n".format(k, strings[k])))
			output_content.append("\n")
			with open(filename, "a") as f_out: #Write all back to file
				f_out.write("".join(output_content))

	def do_EOF(self, args):
		"""Exits program, ctrl + d will allow you to exit"""
		print("Quitting...")
		return True

	def do_shell(self, args):
		"""Runs shell commands, can be run with "!" command, allows for program invocation"""
		if fm.append_output(args) is False: #If we don't need to append output to file
			input_file_check, output_file_check = fm.input_file_provided(args), fm.output_file_provided(args) #input and output file check
			if input_file_check is not False: #Given an input file
				instructions = fm.read_input(input_file_check) #Read in input from input file
			if output_file_check is not False and input_file_check is not False: #Given both input and output file
				#Run each command in instructions and write output to output file
				with open(output_file_check, "w") as f:
					for command in instructions:
						subprocess.run(command.strip(), stdout=f, shell=True)
			#Run each command in instructions and output to screen
			elif output_file_check is False and input_file_check is not False:
				for command in instructions:
						subprocess.run(command.strip(), shell=True)
			#Run instructions from prompt and write output to output file
			elif input_file_check is False and output_file_check is True:
				with open(output_file_check, "w") as f:
					subprocess.run(args.strip(), stdout=f, shell=True)
			#Run instruction from prompt and output to screen
			else:
				#Background Program Execution
				if args[-1].strip() == "&":
					subprocess.Popen(args, close_fds=True, shell=True)
				else:
					print("Running command: {}".format(args))
					output = os.popen(args).read()
					print(output)
		#Need to append result of command to file.
		else:
			filename = fm.append_output(args) #Output File
			input_file = fm.input_file_provided(args) #Input File or False
			log = open(filename, "a") #Open File for appending
			log.flush() #Stops it from writing before ready
			#If we are receiving input from text file
			if input_file is not False:
				instructions = fm.read_input(input_file)
				for command in instructions:
					subprocess.run(command.strip(), stdout=log, shell=True)
			#Receiving input from prompt
			else:
				subprocess.run(args.strip().split(">>")[0], stdout=log, shell=True)

if __name__ == "__main__":
	shell = myShell()
	output_file = fm.output_file_provided(sys.argv) #Check if output file
	if len(sys.argv) > 1: #If there are arguments
		if output_file is False: #No output file so must be input file
			batchfile = sys.argv[1].strip()
			with open(batchfile, "r") as f: #Read in instructions
				instructions = f.readlines()
			for command in instructions:  #Execute each instruction one at a time
				command = command.strip()
				shell.onecmd(command)
		else:
			append_output_file = fm.append_output(sys.argv) #Is there and output file to append to?
			if append_output_file is False: #No appending 
				if len(sys.argv.split(">")[0]) > 0:
					batchfile = sys.argv[1].strip() #Must be input file
					with open(batchfile, "r") as f: #Read in instructions
						instructions = f.readlines()
					for command in instructions: #Execute instructions on at a time and output to output file
						command = command.strip()
						shell.onecmd(command, stdout=output_file)
				else:
					#Run shell and write output to file.
					shell.cmdloop("Starting shell...\nType 'commands' to receive a list of commands.\nType 'concepts' to receive a list of concepts.\n", stdout=output_file)
			#Append output to output file
			else:
				log = open(append_output_file, "a") #Open file for appending
				log.flush() #Prevent writing to file too early
				#If it has an input file
				if len(sys.argv.split(">>")[0]) > 0:
					batchfile = sys.argv[1].strip()
					with open(batchfile, "r") as f:
						instructions = f.readlines()
					for command in instructions:
						command = command.strip()
						shell.onecmd(command, stdout=log)
				#If it doesn't have an input file
				else:
					shell.cmdloop("Starting shell...\nType 'commands' to receive a list of commands.\nType 'concepts' to receive a list of concepts.\n", stdout=log)
	else:
		shell.cmdloop("Starting shell...\nType 'commands' to receive a list of commands.\nType 'concepts' to receive a list of concepts.\n")
	