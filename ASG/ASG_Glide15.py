# this holds the glide scripts
from MissionTracking import printASG
printASG("In ASG_Glide15.py, attempting to import")
from ASG import inflight_run_script_v4
printASG("Import successful")

def F1():
	inflight_run_script_v4.MainRun()

	printASG("hooray we're running ASG_Glide15.py!!!")

	pass
