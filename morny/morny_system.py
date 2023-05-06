import os

class Coeur_Def :
	'''Morny Coeur python 程序以及当前的版本的元信息'''
	
	VERSION = "0.1.2+coeur1.0.0-RC3.7"
	CODE = "beiping"
	TIMETAG = "2305062342"
	
	def is_file_logging () -> bool :
		return os.getenv ("MORNY_LOGGING_TO_FILE") == "true"
	