# --- Andy Ure, au4g10 ---
# Demo UAV test script

from __main__ import v
import PanicMode
from ArduParam import *
from time import sleep
from MissionTracking import printASG

def F1():
	"""
	A test script for accessing vehicle attributes, changing
	vehicle parameters and running multithreading operations."""
	try:
		printASG("Trying DisplayParams")
		DisplayParams()
		printASG("DisplayParams complete\n\n")
		sleep(5)

		printASG("Trying EditParam")
		EditParam()
		printASG("EditParam complete\n\n")
		sleep(5)

		printASG("Trying CheckThreads")
		CheckThreads()
		printASG("CheckThreads complete\n\n")
		sleep(5)

	except PanicPanic, msg:
		printASG("Entering panic mode due to:\n--- %s ---" %msg)
		PanicMode.Enter()
	except:		# Also catch other exceptions
		printASG("Error: entering panic mode and raising")
		PanicMode.Enter()
		raise

	printASG("Completed F1 okay, exiting")
	sleep(2)

	pass

def DisplayParams():
	printASG("Armed: %s" %v.armed)
	printASG("Airspeed: %.2f" %v.airspeed)
	loc = v.location
	printASG("Altitude: %.2f" %loc.alt)
	printASG("latitude,longitude: %.4f,%.4f" %(loc.lat,loc.lon))
	printASG("Relative alt: %.2f" %RelativeAlt())
	pass

def EditParam():
	THR_MAX_orig = FetchParam(['THR_MAX'])[0]
	printASG("THR_MAX is currently: %.0f" %THR_MAX_orig)
	sleep(2)
	printASG("Changing THR_MAX to 0")
	SetParam(['THR_MAX'],[0])
	sleep(2)
	printASG("Done, THR_MAX is now read as: %.0f"
				%FetchParam(['THR_MAX'])[0])

	sleep(2)
	printASG("Resetting THR_MAX")
	SetParam(['THR_MAX'],[THR_MAX_orig])
	sleep(2)
	printASG("Reset, THR_MAX is now read as: %.0f"
				%FetchParam(['THR_MAX'])[0])
	pass

import threading

class SimpleThread(threading.Thread):
	def __init__(self,name,t):
		threading.Thread.__init__(self)
		self.name = name
		self.t = t
	def run(self):
		printASG("Running %s with interval %ds"
					%(self.name,self.t))
		for i in range(10):
			printASG("%s calling at %ds" %(self.name,self.t*i))
			sleep(self.t)
		printASG("%s now complete, exiting" %self.name)
		pass

def CheckThreads():
	t1 = SimpleThread('Thread 1', 1)
	t2 = SimpleThread('Thread 2', 2)

	t1.start()
	t2.start()

	for t in [t1,t2]:
		t.join()
	printASG("Both threads done, CheckThreads all done too")
	pass
