import page

class page_stats(object):
	"""
	parse a page objects data to get basic stats on the data.
	"""
	def __init__(self,t_page):
		"""t_page = page object generated with page.py"""
		if isinstance(t_page, page.page):
			# TODO: make sure you are consistent with how data is represented in this software.
			# currently all data is saved in 1 long string. Ex. data = "this\nis\na\nfile\nwith\nmultiple\nlines\n!!!"
			self.data_stats = self.get_data_stats(t_page)
		else:
			print "you passed an incorrect data type. make sure it is a `page` object!!!"

	def get_data_stats(self,t_page,max_words=None,skip_words=None):
		"""
		iterate through a file and return the top occuring words given max size of words
		to return and omitting any strings
		"""
		# TODO: create a class that handles all of these characters and how they effect the data with regards to what language you are using
		punc_tokens = [".",",","?","!",":","\"","\'","(",")","[","]","{","}","<",">","@","#","$","%","^","&","*","_","=","+","`","~"]
		# TODO: do error checking to make sure that skip_words is either a `None` value or a list of strings. also check that max_words is a number
		if isinstance(t_page.data, str):
			l = t_page.data.split("\n")
			l = [curr.split(" ") for curr in l]
			print l #<@>
			all_words = {}
			for i in l:
				for j in i:
# -----------------------------------------------------------------------
# TODO: split this into a seperate function. also come up with a more elegant solution this function stinks!
					curr_j = ""
					for k in j: #check each char in the string
						if k not in punc_tokens:
							curr_j += k
# -----------------------------------------------------------------------
					if curr_j in all_words:
						all_words[curr_j] = all_words[curr_j]+1
					else:
						all_words[curr_j] = 1
			print all_words #<@>
			return all_words
