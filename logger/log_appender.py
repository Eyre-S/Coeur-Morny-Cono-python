from datetime import datetime
import threading
from .log import *

def output (message:Log) :
	print(format_message(message))

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
	
