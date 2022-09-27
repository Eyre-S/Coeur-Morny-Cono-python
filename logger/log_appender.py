from datetime import datetime
import threading

from define import Coeur_Def
from .log import *

if Coeur_Def.is_file_logging() :
	log_file_archive = open(f"./logs/{time.strftime('%Y-%m-%d-%H:%M:%S.log', time.localtime())}", "x")
	log_file = open("./log__latest.log", "a")

def output (message:Log) :
	echo = format_message(message)
	print(echo)
	if Coeur_Def.is_file_logging() :
		log_file.write(echo+"\n")
		log_file_archive.write(echo+"\n")

def format_message (log:Log) -> str :
	
	origins = log.message.split("\n")
	
	message = ""
	message += f"[{datetime.fromtimestamp(log.timestamp/1000/1000/1000).strftime('%Y-%m-%d/%H:%M:%S:%f')}]" + \
		f"[{threading.current_thread().name }]"
	promptNewLine = "'"*len(message)
	message += f"[{log.level.name}]{origins[0]}"
	for i in range(len(origins)-1) :
		message += f"\n{promptNewLine}[{log.level.name}]{origins[i+1]}"
	
	return message
	
