from logger.log import Log, LogLevels
from logger.log_appender import output


def trace (msg:str) : output(Log(msg, LogLevels.trace))
def debug (msg:str) : output(Log(msg, LogLevels.debug))
def info (msg:str) : output(Log(msg, LogLevels.info))
def warn(msg:str) : output(Log(msg, LogLevels.warn))
def error (msg:str) : output(Log(msg, LogLevels.error))
def fatal (msg:str) : output(Log(msg, LogLevels.fatal))
