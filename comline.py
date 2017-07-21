from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-d", "--directory",
							dest='directory',
							default=os.getcwd().rstrip(),
							help="Provide a path to clumpak output"
		)
		parser.add_argument("-k", "--cluster",
							dest='k',
							required=True,
							help="Provide the best clustering value for clumpak run"
		)
		self.args = parser.parse_args()

		#check if files exist
		#self.exists( self.args.cv )

		#check if directories exist
		self.dirExists(self.args.directory)


	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print( filename, "does not exist" )
			print( "Exiting program..." )
			print( "" )
			raise SystemExit

	def dirExists(self,directory):
		if(os.path.isdir(directory) != True):
			print(repr(directory), "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
