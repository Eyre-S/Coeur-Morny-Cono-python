import os


class Coeur_Def :
	'''Morny Coeur python 程序以及当前的版本的元信息'''
	
	VERSION = "0.1+coeur0.7.2.1"
	CODE = "fuzhou"
	TIMETAG = "2209261500"
	
	def is_file_logging () -> bool :
		return os.getenv ("MORNY_LOGGING_TO_FILE") == "true"
	