import os
import sys
import threading
from morny.util.str import strm

from morny.morny_system import Coeur_Def
from morny import log
from morny.log import logger
from morny.morny_hello import morny_hello_text
from morny.morny_config import MornyConfigPrototype


thread_morny_init = "morny-init"
prop_name_token_tg_key = "TELEGRAM_BOT_API_TOKEN"
prop_name_token_morny_key = "MORNY_TG_TOKEN"

def main():
	
	##
	##
	## 启动参数的声明
	_config: MornyConfigPrototype = MornyConfigPrototype()
	_printmode_version: bool = False
	_printmode_hello: bool = False
	_showHello: bool = True
	
	# Todo: set startup time
	
	##
	##
	## 从命令行与环境变量读取启动参数值
	__i = 1;
	_unknownArgs: list[str] = []
	while (__i < len(sys.argv)) :
		
		if (sys.argv[__i].startswith("-")):
			
			match sys.argv[__i] :
				case "-d" | "--dbg", "--debug":
					log.set_debug_mode(True)
					__i+=1;continue
				case "--outdated-block" | "-ob" :
					_config.eventIgnoreOutdated = True
					__i+=1;continue
				case "--no-hello" | "-hf" | "--quiet" | "-q" :
					_showHello = False
					__i+=1;continue
				case "--only-hello" | "-ho" | "-o" | "-hi" :
					_printmode_hello = True
					__i+=1;continue
				case "--version" | "-v" :
					_printmode_version = True
					__i+=1;continue
				case "--token" | "-t" :
					__i+=1; _config.telegram_bot_key = sys.argv[__i]
					__i+=1;continue
				case "--username" | "-u" :
					__i+=1; _config.telegram_bot_username = sys.argv[__i]
					__i+=1;continue
				case "--master" | "-mm" :
					__i+=1; _config.trusted_master = int(sys.argv[__i])
					__i+=1;continue
				case "--trusted-chat" | "-trs" :
					__i+=1; _config.trusted_master = int(sys.argv[__i])
					__i+=1;continue
				case "--trusted-reader-dinner" | "-trsd" :
					__i+=1; _config.trusted_dinnerReaders.add(int(sys.argv[__i]))
					__i+=1;continue
				case "--auto-cmd" | "-cmd" | "-c" :
					_config.commandRefresh_onLogin = True
					_config.commandRefresh_onLogout = True
					__i+=1;continue
				case "--auto-cmd-list" | "-ca" :
					_config.commandRefresh_onLogin = True
					__i+=1;continue
				case "--auto-cmd-remove" | "-cr" :
					_config.commandRefresh_onLogout = True
					__i+=1;continue
				case "--api" | "-a" :
					__i+=1; _config.telegram_botApi_server = sys.argv[__i]
					__i+=1;continue
				case "--api-files" | "files-api" | "-af" :
					__i+=1; _config.telegram_botApi_server4File = sys.argv[__i]
					__i+=1;continue
		
		_unknownArgs.append(sys.argv[__i])
		__i+=1
		
	
	if (_showHello):
		logger.info(morny_hello_text())
	if (_printmode_hello):
		exit(0)
	
	if (_unknownArgs.count != 0):
		logger.warn("Can't understand arg to some meaning :")
		for __arg in _unknownArgs:
			logger.warn(f"  {__arg}")
	
	if (logger.debug_mode):
		logger.warn("Debug log output enabled.\n  It may lower your performance, make sure that you are not in production environment.")
	logger.debug("Debug log output enabled.")
	
	'''从系统环境变量设置的 bot token 值'''
	_propToken:str|None = None
	'''表明 bot token 值的来源是哪个系统环境变量'''
	_propToken_key:str|None = None
	for __key in [prop_name_token_tg_key, prop_name_token_morny_key] :
		if (os.getenv(__key) != None) :
			_propToken = os.getenv(__key)
			_propToken_key = __key
	
	##
	##
	## 启动参数的检查和处理
	
	if _printmode_version :
		logger.info(strm(
			f"Morny Cono Version",
			f"- version :",
			f"    {Coeur_Def.VERSION}  {Coeur_Def.CODE.upper()}",
			f"- md5hash :",
			f"    <unavailable_in_python_implementation>",
			f"- rw.time :",
			f"    {Coeur_Def.TIMETAG} [UTC+8]",
		));
		exit()

	logger.info(strm(
		f"morny/server_main.py Executed >>>",
		f"- version {Coeur_Def.VERSION} [{Coeur_Def.TIMETAG}]",
		f"- Morny {Coeur_Def.CODE.upper()}",
	))
	
	##
	##
	## Coeur 参数检查以及正式呼叫主程序
	
	if (_propToken != None) :
		logger.info(f"Parameter <token> set by EnvVar ${_propToken_key}")
	
	threading.current_thread().name = thread_morny_init
	
	#todo: call coeur main
