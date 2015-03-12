from __main__ import v
import PanicMode
from ArduParam import * # Use FetchParam and ChangeParam
from time import sleep

def F1():
	# Create exception for entering panic mode
	print(v)
	try:
		print("Trying DisplayParams")
		DisplayParams()
		print("DisplayParams complete\n\n")
		sleep(5)

		print("Trying EditParam")
		EditParam()
		print("EditParam complete\n\n")
		sleep(5)

		print("Trying CheckThreads")
		CheckThreads()
		print("CheckThreads complete\n\n")
		sleep(5)

	except PanicPanic, msg:
		print("Entering panic mode due to:\n--- %s ---" %msg)
		PanicMode.Enter()
	# Also catch other exceptions
	except:
		print("Unexcpected error, entering panic mode and raising")
		PanicMode.Enter()
		raise

	print("Completed F1 okay, exiting")
	sleep(2)

	pass

def DisplayParams():
	print("Armed: %s" %v.armed)
	print("Airspeed: %.2f" %v.airspeed)
	loc = v.location
	print("Altitude: %.2f" %loc.alt)
	print("latitude,longitude: %.4f,%.4f" %(loc.lat,loc.lon))
	pass

def EditParam():
	THR_MAX_orig = FetchParam(['THR_MAX'])[0]
	print("THR_MAX is currently: %.0f" %THR_MAX_orig)
	sleep(2)
	print("Changing THR_MAX to 0")
	SetParam(['THR_MAX'],[0])
	sleep(2)
	print("Done, THR_MAX is now read as: %.0f" %FetchParam(['THR_MAX'])[0])

	sleep(2)
	print("Resetting THR_MAX")
	SetParam(['THR_MAX'],[THR_MAX_orig])
	sleep(2)
	print("Reset, THR_MAX is now read as: %.0f" %FetchParam(['THR_MAX'])[0])
	pass

import threading

class SimpleThread(threading.Thread):
	def __init__(self,name,t):
		threading.Thread.__init__(self)
		self.name = name
		self.t = t
	def run(self):
		print("Running %s with interval %ds" %(self.name,self.t))
		for i in range(10):
			print("%s calling at %ds" %(self.name,self.t*i))
			sleep(self.t)
		print("%s now complete, exiting" %self.name)
		pass

def CheckThreads():
	t1 = SimpleThread('Thread 1', 1)
	t2 = SimpleThread('Thread 2', 2)

	t1.start()
	t2.start()

	for t in [t1,t2]:
		t.join()
	print("Both threads done, CheckThreads all done too")
	pass
