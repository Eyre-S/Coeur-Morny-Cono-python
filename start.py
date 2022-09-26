import os
import sys
import threading
from define import Coeur_Def
from logger.logger import *
from morny.morny_hello import morny_hello_text


thread_morny_init = "morny-init"
prop_name_token_tg_key = "TELEGRAM_BOT_API_TOKEN"
prop_name_token_morny_key = "MORNY_TG_TOKEN"

##
##
## 启动参数的声明

versionEchoMode:bool = False
welcomeEchoMode:bool = False
showWelcome:bool = True
key:str = None
username:str = None;
outdatedBlock:bool = False
master:int = 793274677
trustedReadersOfDinner:set = set()
trustedChat:int = -1001541451710
autoCmdList:bool = False
autoCmdRemove:bool = False
api:str = None
api4File:str = None


##
##
## 从命令行与环境变量读取启动参数值

i = 1;
while (i < len(sys.argv)) :
	
	if (sys.argv[i].startswith("-")):
		
		match sys.argv[i] :
			case "--outdated-block" | "-ob" :
				outdatedBlock = True
				i+=1;continue
			case "--no-hello" | "-hf" | "--quiet" | "-q" :
				showWelcome = False
				i+=1;continue
			case "--only-hello" | "-ho" | "-o" | "-hi" :
				welcomeEchoMode = True
				i+=1;continue
			case "--version" | "-v" :
				versionEchoMode = True
				i+=1;continue
			case "--token" | "-t" :
				i+=1; key = sys.argv[i]
				i+=1;continue
			case "--username" | "-u" :
				i+=1; username = sys.argv[i]
				i+=1;continue
			case "--master" | "-mm" :
				i+=1; master = int(sys.argv[i])
				i+=1;continue
			case "--trusted-chat" | "-trs" :
				i+=1; trustedChat = int(sys.argv[i])
				i+=1;continue
			case "--trusted-reader-dinner" | "-trsd" :
				i+=1; trustedReadersOfDinner.add(int(sys.argv[i]))
				i+=1;continue
			case "--auto-cmd" | "-cmd" | "-c" :
				autoCmdList = True
				autoCmdRemove = True
				i+=1;continue
			case "--auto-cmd-list" | "-ca" :
				autoCmdList = True
				i+=1;continue
			case "--auto-cmd-remove" | "-cr" :
				autoCmdRemove = True
				i+=1;continue
			case "--api" | "-a" :
				i+=1; api = sys.argv[i]
				i+=1;continue
			case "--api-files" | "files-api" | "-af" :
				i+=1; api4File = sys.argv[i]
				i+=1;continue
	
	warn(f"Can't understand arg to some meaning :\n  {sys.argv[i]}")
	i+=1
	

propToken:str = None
'''从系统环境变量设置的 bot token 值'''
propTokenKey:str = None
'''表明 bot token 值的来源是哪个系统环境变量'''

for iKey in [prop_name_token_tg_key, prop_name_token_morny_key] :
	if (os.getenv(iKey) != None) :
		propToken = os.getenv(iKey)
		propTokenKey = iKey

##
##
## 启动参数的检查和处理

if versionEchoMode :
	info(f"""Morny Cono Version
- version :
    {Coeur_Def.VERSION}  {Coeur_Def.CODE.upper()}
- md5hash :
    <unavailable_in_python_implementation>
- rw.time :
    {Coeur_Def.TIMETAG} [UTC+8]"""
	); exit()

if showWelcome : info(morny_hello_text())
if welcomeEchoMode : exit()

info(f"""start.py Executed >>>
- version {Coeur_Def.VERSION} [{Coeur_Def.TIMETAG}]
- Morny {Coeur_Def.CODE.upper()}""")

##
##
## Coeur 参数检查以及正式呼叫主程序

if (propToken != None) :
	key = propToken
	info(f"Parameter <token> set by EnvVar ${propTokenKey}")
if (key == None) :
	info("Parameter required has no value:\n --token.")
	exit()
threading.current_thread().name = thread_morny_init
#todo call coeur main
