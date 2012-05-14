import cmd
import readline
import credentials.ui

class Credentials(cmd.Cmd):
	"""The main credentials program implemented as a subclass of Cmd."""

	prompt = '\033[4mcredentials\033[0m > '
	intro =  "Manages usernames and passwords for pentesting.\n"
	intro += "Use exit, quit, or ctrl-d to exit.\n"
	doc_header = 'Accepted Commands (use help <command> )'
	msg = credentials.ui.Messages()

	##
	# When an unrecognized command is used, print an error and print the help
	def default(self, line):
		self.msg.print_error("Invalid command: " + line)
		self.do_help('')

	##
	# Exit the Credentials program
	def do_EOF(self, line):
		"""Exit Credentials"""
		self.msg.print_status("\nExiting Credentials")
		return True
	##
	# Exit the Credentials program
	def do_quit(self, line):
		"""Exit Credentials"""
		self.msg.print_status("Exiting Credentials")
		return True

	##
	# Exit the Credentials program
	def do_exit(self, line):
		"""Exit Credentials"""
		self.msg.print_status("Exiting Credentials")
		return True

	##
	# Print help information for the help command
	def help_help(self):
		print "Print help information"

	##
	# Methods for dealing with usernames
	def do_load_users(self, line):
		"""Takes a list of usernames and loads them into the db."""
		#self.db.add_users(users)
		self.msg.print_status("Adding users to DB")

	##
	# Methods for dealing with passwords
	def do_load_passwords(self, line):
		"""Takes a list of passwords and loads them into the db."""
		#self.db.add_passwords(passwords)
		self.msg.print_status("Adding passwords to DB")

if __name__ == '__main__':
	Credentials().cmdloop()
