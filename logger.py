from datetime import datetime
from termcolor import colored

class Logger:
	def __init__(self, tid):
		self.format = '%H:%M:%S'
		self.tid = str(tid)

	def log(self, text, color=None, file=None, debug=None):
		timestamp = '[' + datetime.now().strftime(self.format) + ']'
		timestamp_colour = colored(timestamp, "yellow")
		if color is not None:
			text = self.getColor(text, color)
		elif debug == True:
			text = self.getColor(text, 'debug')

		if file is not None:
			try:
				with open(file, 'a') as txt:
					txt.write('{} : Task [{}] : {}\n'.format(timestamp, self.tid, text))
			except Exception as e:
				print('ERROR: problem writing to file: {}'.format(str(e)))

		if debug is not None:
			if debug == True:
				print('{} : Task [{}] : {}'.format(timestamp_colour, self.tid, text))
			else:
				pass
		else:
			print('{} : Task [{}] : {}'.format(timestamp_colour, self.tid, text))

	def getColor(self, text, color):
		try:
			status = {
				'success': "[{}] ".format(colored('✓', 'green')),
				'error': "[{}] ".format(colored('✗', 'red')),
				'debug': "[{}] ".format(colored('*', 'magenta')),
				'note': "[{}] ".format(colored('#', 'yellow'))
			}
			return status[color.lower()] + text
		except Exception as e:
			try:
				return colored(text, color)
			except Exception as e:
				print("WARNING: Unrecognized Color! {}".format(str(color)))
