__name__      = 'gramana'
__author__    = 'Dan Lecocq (dan.lecocq@kaust.edu.sa)'
__license__   = 'Use It!'
__version__   = '0.1'

class gramana:
	def __init__(self, words, base = ""):
		'''Supply a list of words that are valid'''
		# Whether or not this node represents a real word or not
		self.valid = False
		# All the words that share the same beginning
		self.children = {}
		# My parent node, for constructing the string again
		self.parent = None
		self.count = 0
		self.parse(words, base)
	
	def parse(self, words, base):
		# Length of the base string
		base_len = len(base)
		# While words remain...
		while(len(words)):
			word = words[0]
			# If the word is the same as the base itself, it is a valid word
			if (word == base):
				# self.log(base + " is valid.")
				self.valid = True
				# Pop this word off...
				words.pop(0)
				continue
			# Otherwise, if the base still applies to this word,
			elif (base == "" or word[0:base_len] == base):
				# Get the next character, and add it to the base
				char = word[base_len]
				# Spawn a child associated with this letter
				self.children[char] = tree(words, base + char)
			else:
				return

	def search(self, word):
		'''Search for all anagrams for the supplied word'''
		word_hash = {}
		for i in word:
			if i in word_hash:
				word_hash[i] += 1
			else:
				word_hash[i] = 1
		return self.search_hash(word_hash)
	
	def search_hash(self, word, base = ''):
		results = []
		if (self.valid):
			results.append(base)
		# word should be a hash of how many of which letters are remaining
		for i in word:
			if word[i] > 0 and i in self.children:
				word[i] -= 1
				results.extend(self.children[i].search_hash(word, base + i))
				word[i] += 1
		self.count += len(results)
		return results
	
	def log(self, message):
		print message
