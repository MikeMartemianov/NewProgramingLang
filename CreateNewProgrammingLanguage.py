try:

	class CreateProgramingLang:		
		
		def __init__(self):

			pass

		class tokens:

			def __init__(self):

				self.tokens1 = []

			def append_token(self, name:str, program:any):

				self.tokens1.append([name, program])

			def return_tokens(self):

				return self.tokens1

		class program:

			def __init__(self, tokens):

				self.tokens = tokens

			def out(self, num:int):

				return self.co[num]

			def run(self, code:str, lines:str, words:str):

				code = code.split(line)

				for cod1 in code:

					cod = cod1.split(words)

					n = 0

					for self.co in cod:

						for hng in self.tokens:

							if self.co == hng[0]:

								hng[1](cod, n)

						n += 1

except Exception:

	pass
