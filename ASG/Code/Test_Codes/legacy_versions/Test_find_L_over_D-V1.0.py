#Test_find_L_over_D.py

#This code sends commands to the UAV to glide in a straight line at varying
#speeds and calculates the lift to drag ratio using the altitude, latitude,
#and longitude values.

#Shogo Minakata, sm34g11@soton.ac.uk, Created 5 Nov 2014

#===============================================================================

import numpy as np #Import numerical python module
import time
import matplotlib.pyplot as plt
import csv

#Initilisation, Parameter input-------------------------------------------------

elevator_angles=np.linspace(-1,1,11) #List of elevator angles 

lat_start = 50.805000   #Location of manoeuvre start, from WP file
lon_start = -1.490000
alt_start = 50 

lat_lineup = 80.804500  #Location of line up point, from WP file
lon_lineup = -1.490000
alt_lineup = 50

elevator_angle_index=0  #Index number for elevator angle, used for data storage

datalength = 3 #Length of data that is to be collected
times = np.zeros(shape=(len(elevator_angles), datalength)) #Creating empty data arrays
latitude = np.zeros(shape=(len(elevator_angles), datalength))
longitude = np.zeros(shape=(len(elevator_angles), datalength))
altitude = np.zeros(shape=(len(elevator_angles), datalength))

#Data Collection----------------------------------------------------------------

for elevator_angle in elevator_angles: #Iterating over all elevator angles

    print('Starting data collection sequence for elevator angle %4.2f'\
          % (elevator_angle))
    
    #Waiting to reach starting WP-----------------------------------------------
    for t in np.arange(0, 10000): #Iterating over an undefined time period
        lat = 80.805000 #Code importing current coordinate values
        lon = -1.490000
        alt = 50
        #lat = cs.lat
        #lon = cs.lng
        #alt = cs.alt

        #Coordinate check, exit while-loop when coordinates match
        while lat != lat_start and lon != lon_start and alt != alt_start: 
            time.sleep(0.5) #Coordinate check done every 0.5 seconds

        print('GPS coordinates match with test start location!')
        break #Stopping for-loop

    #Commands to UAV------------------------------------------------------------
    #"Code changing elevator angle in UAV"
    print('Changing elevator angle to %5.2f (Elevator index: %d)'\
          % (elevator_angle, elevator_angle_index))
    #"Code changing thrust level to 0"
    print('Changing thrust level to 0')

    #Reading off data-----------------------------------------------------------
    #Iterating through time
    print('Data collection start!')
    tic = time.clock() #Start of count (t_0)
    for i in np.linspace(0,len(times[0])-1,len(times[0])): 
        toc = time.clock() #Time for each individual datapoint (t_i)
        times[elevator_angle_index][i] = toc - tic
        #Code reading values from MP
        latitude[elevator_angle_index][i] = 80.805000 
        longitude[elevator_angle_index][i] = -1.490000
        altitude[elevator_angle_index][i] = 50
        #latitude[elevator_angle_index][i] = 80.805000
        #longitude[elevator_angle_index][i] = -1.490000
        #altitude[elevator_angle_index][i] = 50
        print("Time: %6.4f, Latitude: %6.4f, Longitude: %6.4f, Altitude: %6.4f"\
              % (times[elevator_angle_index][i],\
                 latitude[elevator_angle_index][i],\
                 longitude[elevator_angle_index][i],\
                 altitude[elevator_angle_index][i]))
        time.sleep(1) #Data reading done approximately every 0.1 seconds
    print('Data collection finished!')
    
    #Commands to UAV (Post data read)-------------------------------------------
    #"Code changing thrust level to 100"
    print('Changing thrust level to 100')
    #"Code returning elevator authority to Autopilot"
    print('Returning elevator authority to Autopilot\n')

    #Miscellaneous--------------------------------------------------------------
    elevator_angle_index += 1   #So next iteration does not overwrite data
                                #(Changing position in data array)

#Code setting UAV to loiter at current location
#Code returning full flight authority to Autopilot
print('Test for all elevator angles finished. UAV is set to loiter and full'\
      ' control authority returned to Autopilot.')

#Columns into rows--------------------------------------------------------------


#Csv export---------------------------------------------------------------------
