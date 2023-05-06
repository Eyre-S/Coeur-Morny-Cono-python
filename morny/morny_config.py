PROP_TOKEN_KEY_DEFAULT: str = "TELEGRAM_BOT_API_TOKEN"
PROP_MORNY_TOKEN_KEY: str = "MORNY_TG_TOKEN"

PROP_TOKEN_KEYS: list[str] = [PROP_TOKEN_KEY_DEFAULT, PROP_MORNY_TOKEN_KEY]

class MornyConfigPrototype:
	def __init__(self):
		
		self.telegram_botApi_server: str|None = None
		self.telegram_botApi_server4File: str|None = None
		self.telegram_bot_key: str|None = None
		self.telegram_bot_username: str|None = None
		
		self.eventIgnoreOutdated: bool = False
		self.eventOutdatedTimestamp: int = -1
		
		self.commandRefresh_onLogin: bool = False
		self.commandRefresh_onLogout: bool = False
		
		self.trusted_master: int = 793274677
		self.trusted_chat: int = -1001541451710
		
		self.trusted_dinnerReaders: set[int] = set[int]()
		self.dinner_chatId: int = -1001707106392
		
		self.reportTo_chatId: int = -1001650050443
		
		self.medicationNotify_toChat_id: int = -1001729016815
		self.medicationNotify_useTimezone = 0 #todo: type
		self.medicationNotify_atHour: set[int] = set[int]()
		

class MornyConfig:
	
	class CheckError(Exception):
		def __init__(self, failure_at: str, request: str):
			self.failure_at = failure_at
	
	def __init__(self, prototype: MornyConfigPrototype):
		
		if (prototype.telegram_bot_key == None): raise MornyConfig.CheckError("telegram_bot_key", "not None.")
		self.telegram_botApi_server:      str|None = prototype.telegram_botApi_server
		self.telegram_botApi_server4File: str|None = prototype.telegram_botApi_server4File
		self.telegram_bot_key:            str      = prototype.telegram_bot_key
		self.telegram_bot_username:       str|None = prototype.telegram_bot_username
		
		if (prototype.eventOutdatedTimestamp < 1): raise MornyConfig.CheckError("eventOutdatedTimestamp", "bigger than 1")
		self.eventIgnoreOutdated:         bool     = prototype.eventIgnoreOutdated
		self.eventOutdatedTimestamp:      int      = prototype.eventOutdatedTimestamp
		
		self.commandRefresh_onLogin:      bool     = prototype.commandRefresh_onLogin
		self.commandRefresh_onLogout:     bool     = prototype.commandRefresh_onLogout
		
		self.trusted_master:              int      = prototype.trusted_master
		self.trusted_chat:                int      = prototype.trusted_chat
		
		self.trusted_dinnerReaders:       set[int] = prototype.trusted_dinnerReaders
		self.dinner_chatId:               int      = prototype.dinner_chatId
		
		self.reportTo_chatId:             int      = prototype.reportTo_chatId
		
		for i in prototype.medicationNotify_atHour:
			if (i > 23 or i < 0):
				raise MornyConfig.CheckError(f"medicationNotify_atHour value {i}", "must a vaild hour number(0-23)")
		self.medicationNotify_toChat_id:  int      = prototype.medicationNotify_toChat_id
		self.medicationNotify_useTimezone          = prototype.medicationNotify_useTimezone
		self.medicationNotify_atHour:     set[int] = prototype.medicationNotify_atHour
		
	
