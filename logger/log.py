import time

class LogLevel:
	def __init__(self, level:float, name:str) :
		self.level = level
		self.name = name
	# def level (self) -> float : return self.level
	# def name (self) -> str : return self.name

class LogLevels:
	trace:LogLevel = LogLevel(-1,  "TRAC")
	debug:LogLevel = LogLevel(0.1, "DBUG")
	info:LogLevel  = LogLevel(0,   "INFO")
	warn:LogLevel  = LogLevel(0.5, "WARN")
	error:LogLevel = LogLevel(1,   "ERRO")
	fatal:LogLevel = LogLevel(10,  "FTAL")
	null:LogLevel  = LogLevel(0,   "NULL")

class Log:
	def __init__ (self, message:str, level:LogLevel) :
		self.timestamp = time.time_ns()
		self.level = level
		self.message = message
	# def timestamp (self) -> int : return self.timestamp
	# def level (self) -> LogLevel : return self.level
	# def message (self) -> str : return self.message
