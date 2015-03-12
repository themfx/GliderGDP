from time import time
from __main__ import v

def s(t=2):
	start = time()
	now   = time()
	while (now-start) < t:
		now = time()
		v.flush()
	pass

def ms(t):
	s(t/1000.)
	pass

def minute(t):
	s(t*60)
	pass
