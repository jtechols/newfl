from .base import *

try:
	from .local import *
	live = False
except:
	live = True
	from .production import *