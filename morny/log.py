from pyssage.components.restrictions import RestrictionToLog, LevelRestriction
from pyssage.appender import ConsoleAppender
from pyssage.formatter import SimpleFormatter
from pyssage.log.log import levels
from pyssage.logger import Logger


restriction: RestrictionToLog = LevelRestriction(levels.INFO)

logger: Logger = Logger(ConsoleAppender(SimpleFormatter()))
logger.restrictions.append(restriction)


def set_debug_mode(mode: bool):
	if mode:
		restriction.min_level = levels.ALL
	else:
		restriction.min_level = levels.INFO

def is_debug_mode () -> bool:
	return restriction.min_level < levels.INFO
