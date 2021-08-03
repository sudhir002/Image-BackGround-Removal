class Credential(object):
	'''
		Object that has a word and char count of the word
	'''
	def __init__(self):
		#Creation of new Instance
		self._username = ""
		self._pswd = ""
		self._authsource = "wearesethjiapp"
		self._host = 'localhost'
		self._port = 27017
		self._secret = 'wearesethjiapp'

	def __str__(self):
		return "{}, {}, {}, {}, {}, {}".format(self._username, self._pswd, self._authsource, self._host, self._port, self._secret)

	#Property Getter and Property Setter
	@property
	def username(self):
		return self._username

	@property
	def pswd(self):
		return self._pswd

	@property
	def authsource(self):
		return self._authsource

	@property
	def host(self):
		return self._host

	@property
	def port(self):
		return self._port

	@property
	def secret(self):
		return self._secret
