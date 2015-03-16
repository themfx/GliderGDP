from datetime import datetime
import os
loc = os.getcwd()+'/GliderGDP/Tools/Missions/MissionTracker.txt'

def printASG(msg):
	print(msg)
	f = open(loc,'a')
	f.writelines(str(datetime.now())+':'+str(msg)+'\n')
	f.close()
	pass
