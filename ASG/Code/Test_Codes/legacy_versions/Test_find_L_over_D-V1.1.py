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
#GPS coordinate check done every --- seconds
t_int_gps = 0.5
#Number of datapoints to be collected each flight (be wary of how many can be
#                             collected before reaching dangerous altitude!!!)
datalength = 3
#Measurements during test sampled every --- seconds
t_int = 1.0
#Waypoint file name
WPfilename = 'long_WP.txt'
#Result file name
resultfilename = 'test.csv'

#How to set up waypoints in MP--------------------------------------------------

#In Mission planner set WPs as following
#First WP: line up WP,
#Second WP: start WP (setting T = 0, start measurement after 5 s)

#FOR ANDY=======================================================================
#I've put the letters *** in places where it needs adding, so when you add the
#code that sends the commands to MP, just search for ***. Thanks!
#(also just ignore the part where the coordinate has to be pulled out using
# Wilhelm's file)

#===============================================================================
import numpy as np #Import numerical python module
import time
import matplotlib.pyplot as plt
import csv

#Initilisation, Parameter input-------------------------------------------------

velocity_inputs=np.arange(v0,vn+vint,vint) #List of velocity inputs

execfile('coord_WP_dist.py') #Executing Wilhelm's WP file interpretation script

loc_data = get_coords(WPfilename)

lat_start = loc_data[0][0]   #Location of manoeuvre start, from WP file
lon_start = loc_data[0][1]   
alt_start = loc_data[0][2]

lat_lineup = loc_data[1][0]  #Location of line up point, from WP file
lon_lineup = loc_data[1][1]
alt_lineup = loc_data[1][2]

velocity_input_index=0  #Index number for velocity input, used for data storage

datalength = datalength #Length of data that is to be collected
times = np.zeros(shape=(len(velocity_inputs), datalength)) #Creating empty data arrays
latitude = np.zeros(shape=(len(velocity_inputs), datalength))
longitude = np.zeros(shape=(len(velocity_inputs), datalength))
altitude = np.zeros(shape=(len(velocity_inputs), datalength))

#Data Collection----------------------------------------------------------------

for velocity_input in velocity_inputs: #Iterating over all elevator angles

    print('Starting data collection sequence for velocity input %4.2f'\
          % (velocity_input))
    
    #Waiting to reach starting WP-----------------------------------------------
    print('Waiting for GPS locations to match')
    for t in np.arange(0, 10000): #Iterating over an undefined time period
        lat = 80.805000 
        lon = -1.490000
        alt = 50
        #lat = cs.lat   #Code importing current coordinate values
        #lon = cs.lng   *** Just need to change from the fixed values above
        #alt = cs.alt

        #Coordinate check, exit while-loop when coordinates match
        while lat != lat_start and lon != lon_start and alt != alt_start: 
            time.sleep(t_int_gps) #Coordinate check done every t_int_gps seconds

        print('GPS coordinates match with test start location!')
        break #Stopping for-loop

    #Commands to UAV------------------------------------------------------------
    #"Code changing velocity input to UAV" ***
    print('Changing velocity input to %5.2f (Velocity input index: %d)'\
          % (velocity_input, velocity_input_index))
    #"Code changing thrust level to 0" ***
    print('Changing thrust level to 0')
    time.sleep(5) #Delay 5 seconds to let glider settle (e.g. not in stall, etc)

    #Reading off data-----------------------------------------------------------
    #Iterating through time
    print('Data collection start!')
    tic = time.clock() #Start of count (t_0)
    for i in np.linspace(0,len(times[0])-1,len(times[0])): 
        toc = time.clock() #Time for each individual datapoint (t_i)
        times[velocity_input_index][i] = toc - tic
        #Code reading values from MP
        latitude[velocity_input_index][i] = 80.805000 
        longitude[velocity_input_index][i] = -1.490000
        altitude[velocity_input_index][i] = 50
        #latitude[velocity_input_index][i] = cs.lat
        #longitude[velocity_input_index][i] = cs.lng *** Again, comment out 
        #altitude[velocity_input_index][i] = cs.alt      fixed values please
        print("Time: %6.4f, Latitude: %6.4f, Longitude: %6.4f, Altitude: %6.4f"\
              % (times[velocity_input_index][i],\
                 latitude[velocity_input_index][i],\
                 longitude[velocity_input_index][i],\
                 altitude[velocity_input_index][i]))
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


#Csv export---------------------------------------------------------------------
with open(resultfilename, 'w') as openedcsv:
    csvwriter = csv.writer(openedcsv, delimiter=',')
    data = [times, latitude, longitude, altitude]
    csvwriter.writerows(data)
