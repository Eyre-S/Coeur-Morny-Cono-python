from logger import logger as logger_impl

class logger:
	
	debug_mode: bool = False
	
	@staticmethod
	def trace (msg: str):
		if (logger.debug_mode):
			logger_impl.trace(msg)
	
	@staticmethod
	def debug (msg: str):
		if (logger.debug_mode):
			logger_impl.debug(msg)
	
	@staticmethod
	def info (msg: str):
		logger_impl.info(msg)
	
	@staticmethod
	def warn (msg: str):
		logger_impl.warn(msg)
	
	@staticmethod
	def error (msg: str):
		logger_impl.error(msg)
	
	@staticmethod
	def fatal (msg: str):
		logger_impl.fatal(msg)
	

def set_debug_mode(mode: bool):
	logger.debug_mode = mode
