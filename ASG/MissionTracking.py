# --- Andy Ure, au4g10 ---
# Testing of script stdout tedirection shows some issues, so this
#  script appends all printASG() calls to a log file.

from datetime import datetime
import os
loc = os.getcwd()+'/GliderGDP/Tools/Missions/MissionTracker.txt'

def printASG(msg):
	"""
	Output message to stdout and the MissionTracker log file."""
	print(msg)
	f = open(loc,'a')
	f.writelines(str(datetime.now())+':'+str(msg)+'\n')
	f.close()
	pass
