#Test_find_L_over_D.py

#This code sends commands to the UAV to glide in a straight line at varying
#speeds and calculates the lift to drag ratio using the altitude, latitude,
#and longitude values.

#Shogo Minakata, sm34g11@soton.ac.uk, Created 5 Nov 2014

#===============================================================================
#User Inputs--------------------------------------------------------------------

#I've put the definition of these values at the top so that we don't have to go
#looking in the code when we want to change these.

#Starting velocity input
v0 = 10
#Final velocity input
vn = 15
#Velocity intervals (conduct measurement for every --- ms-1)
vint = 1.0
#GPS coordinate check, tolerances
 #For latitude, 0.00001 corresponds to approximately 1 m (1.11 m)
 #For longitude it depends on latitude, but at the latitude of 50.804796
 #(approximately where RAF Beaulieu is), 0.000015 corresponds to
 #approximately 1 m (1.05 m)
lat_tol = 0.00001
lon_tol = 0.000015
alt_tol = 1
#GPS coordinate check done every --- seconds
t_int_gps = 0.5
#Glider settling time (how long to wait after thrust cut to ensure smooth
#                      gliding)
settle_time = 1.0
#Number of datapoints to be collected each flight (be wary of how many can be
#                             collected before reaching dangerous altitude!!!)
datalength = 7
#Measurements during test sampled every --- seconds
t_int = 1.0
#Waypoint file name
WPfilename = '../Pre-flight/long_WP.txt'
#Result file name
resultfilename = 'test.csv'

#How to set up waypoints in MP--------------------------------------------------

#In Mission planner set WPs as following
#First WP: line up WP,
#Second WP: start WP (setting T = 0, start measurement after 'settle_time' sec.)

#FOR ANDY=======================================================================
#I've put the letters *** in places where it needs adding, so when you add the
#code that sends the commands to MP, just search for ***. Thanks!
#(Some of them already have commands on it. I've used the following link to look
# up the syntax...
#http://plane.ardupilot.com/wiki/common-using-python-scripts-in-mission-planner/

#===============================================================================
import numpy as np #Import numerical python module
import time
import matplotlib.pyplot as plt
import csv

#Initilisation, Parameter input-------------------------------------------------

velocity_inputs=np.arange(v0,vn+vint,vint) #List of velocity inputs

execfile('../Pre-flight/coord_WP_dist.py') #Executing Wilhelm's WP file interpretation script

loc_data = get_coords(WPfilename)
"""
lat_start = loc_data[0][0]   #Location of manoeuvre start, from WP file
lon_start = loc_data[0][1]   
alt_start = loc_data[0][2]

lat_lineup = loc_data[1][0]  #Location of line up point, from WP file
lon_lineup = loc_data[1][1]
alt_lineup = loc_data[1][2]"""

lat_start = 80.805000 
lon_start = -1.490000
alt_start = 50

velocity_input_index=0  #Index number for velocity input, used for data storage

datalength = datalength #Length of data that is to be collected
times = np.zeros(shape=(len(velocity_inputs), datalength)) #Creating empty data arrays
latitude = np.zeros(shape=(len(velocity_inputs), datalength))
longitude = np.zeros(shape=(len(velocity_inputs), datalength))
altitude = np.zeros(shape=(len(velocity_inputs), datalength))
airspeed = np.zeros(shape=(len(velocity_inputs), datalength))
gz = np.zeros(shape=(len(velocity_inputs), datalength)) #gyro values for z
winddir = np.zeros(shape=(len(velocity_inputs), datalength))
windvel = np.zeros(shape=(len(velocity_inputs), datalength))
distance = np.zeros(shape=(len(velocity_inputs), datalength))

#Data Collection----------------------------------------------------------------

for velocity_input in velocity_inputs: #Iterating over all elevator angles

    print('Starting data collection sequence for velocity input %4.2f'\
          % (velocity_input))
    
    #Waiting to reach starting WP-----------------------------------------------
    print('Waiting for GPS locations to match')
    for t in np.arange(0, 100000): #Iterating over an undefined time period
        lat = 80.805000 
        lon = -1.490000
        alt = 50
        #lat = cs.lat   #Code importing current coordinate values
        #lon = cs.lng   *** Just need to change from the fixed values above
        #alt = cs.alt
        #Checking coordinates with tolerance values (if coordinates within
        #tolerance, move on)
        if lat >= lat_start-lat_tol and lat <= lat_start+lat_tol:
            if lon >= lon_start-lon_tol and lon <= lon_start+lon_tol:
                if alt >= alt_start-alt_tol and alt <= alt_start+alt_tol:
                    print('GPS coordinates within tolerance with test start location!')
                    break #Exiting for-loop
        time.sleep(t_int_gps)   #How long to wait until next GPS coordinate check

    #Commands to UAV------------------------------------------------------------
    #"Code changing velocity input to UAV" ***
    print('Changing velocity input to %5.2f (Velocity input index: %d)'\
          % (velocity_input, velocity_input_index))
    #"Code changing thrust level to 0" ***
    print('Changing thrust level to 0')
    print('Waiting %d seconds to let glider settle...' % settle_time)
    time.sleep(settle_time) #Delay 5 seconds to let glider settle (e.g. not in stall, etc)

    #Reading off data-----------------------------------------------------------
    #Iterating through time
    print('Data collection start!\n')
    tic = time.clock() #Start of count (t_0)
    for i in np.linspace(0,len(times[0])-1,len(times[0])): 
        toc = time.clock() #Time for each individual datapoint (t_i)
        times[velocity_input_index][i] = toc - tic
        #Code reading values from MP
        latitude[velocity_input_index][i] = 80.805000 
        longitude[velocity_input_index][i] = -1.490000
        altitude[velocity_input_index][i] = 50.
        airspeed[velocity_input_index][i] = 15.
        gz[velocity_input_index][i] = -0.5
        winddir[velocity_input_index][i] = 30
        windvel[velocity_input_index][i] = 1
        #latitude[velocity_input_index][i] = cs.lat
        #longitude[velocity_input_index][i] = cs.lng *** Again, comment out 
        #altitude[velocity_input_index][i] = cs.alt      fixed values please
        #airspeed[velocity_input_index][i] = 15.
        #gz[velocity_input_index][i] = cs.gz
        #winddir[velocity_input_index][i] = cs.wind_dir
        #windvel[velocity_input_index][i] = cs.wind_vel
        print("Time: %6.4f\nLatitude: %6.4f\nLongitude: %6.4f\nAltitude: %6.4f"\
               "\nAirspeed: %6.4f\ngz: %6.4f\nWind Direction: %6.4f\nWind "\
               "Velocity: %6.4f\n"
              % (times[velocity_input_index][i],\
                 latitude[velocity_input_index][i],\
                 longitude[velocity_input_index][i],\
                 altitude[velocity_input_index][i],\
                 airspeed[velocity_input_index][i],\
                 gz[velocity_input_index][i],\
                 winddir[velocity_input_index][i],\
                 windvel[velocity_input_index][i]))
        time.sleep(t_int) #Data reading done "approximately" every t_int seconds
                          #("approximately" because of the time taken to process
                          # the code)
    print('Data collection finished!')
    
    #Commands to UAV (Post data read)-------------------------------------------
    #"Code changing thrust level to 100" ***
    print('Changing thrust level to 100')
    #"Code nullifying velocity input command" *** (or is this unneccesary
                                                  #because flight control is
                                                  #returned when "Thrust != 0" ?
                                                  # +++)
    print('Returning flight authority to Autopilot\n')

    #Miscellaneous--------------------------------------------------------------
    velocity_input_index += 1   #So next iteration does not overwrite data
                                #(Changing position in data array)

#Code setting UAV to loiter at current location ***
#Code returning full flight authority to Autopilot *** (same comment as +++)
print('Test for all velocity input values finished. UAV is set to loiter and '\
      'full control authority returned to Autopilot.')

#Columns into rows--------------------------------------------------------------

#Calculating distance
for n in np.arange(len(velocity_inputs)):
    for m in np.arange(datalength-1):
        d = dist(latitude[n][m],latitude[n][m+1],longitude[n][m],longitude[n][m+1])
        distance[n][m] = d

#Csv export---------------------------------------------------------------------
with open(resultfilename, 'w') as openedcsv:
    csvwriter = csv.writer(openedcsv, delimiter=',')
    data = [times, latitude, longitude, distance, altitude, airspeed, gz, winddir, windvel]
    csvwriter.writerows(data)
