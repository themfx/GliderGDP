#	import ASG_Glide15          # contains main glide scripts
import PanicMode       # use to enter panic mode
from MissionTracking import printASG

def Function1():
	# Create exception for entering panic mode
	class PanicPanic(Exception): pass

	# Run the required scripts in a safe way: ensuring any exceptions
	#  put the aircraft back into a safe mode and the pilot is
	#  alerted.
	try:
		# Scripts to be run go here
		printASG("Attempting to import i_r_s_v4")
		from ASG.inflight_run_script_v4 import MainRun
		printASG("Success, running MainRun()")
		MainRun()

	# If panic mode is requested, capture it here
	except PanicPanic, msg:
		printASG("Entering panic mode due to:\n--- %s ---" %msg)
		PanicMode.Enter()

	# Any other exception will also lead to panic mode
	except:
		printASG("Unexcpected error, entering panic mode and raising")
		PanicMode.Enter()
		raise

	# If the scripts complete, we exit nicely here
	printASG("Exiting ASG_TopLevel.py")

	pass
