# Overiding safety check to make sure UAV is within landing
# distance of a safe landing zone (WP)
# Laurence Jackson, lj8g10

from coord_WP_dist import *
from __main__ import v
from active_aircraft import LD_fixed

"""Modified from Wilhelm's code, with alt removed"""

def lon_lat_coords(filename):

    coords = []

    f=open(filename) #reading file
    text=f.read()
    f.close()
    lines=text.split('\n')[1:] #only reading data, not header

    for line in lines: #1 line at at time
        data=line.split()

        if len(data)>=11: #avoid header again and one test for invalid data
            lat=float(data[8])      #select appropriate data
            lon=float(data[9])

            temp_coord=[lat,lon]
            coords.append(temp_coord)
        else:
            break

    return coords

"""Calculates current ground distance from current location to all
designated safe WP, again adapted from Wilhelm's code"""

def dist_safeWP(cs_lat,cs_lon,coords):
    """This function uses the Haversine Formula [1, accessed 2014, Nov 4th, 20:45] to compute distances between a series of waypoints. input 'coords' is a list with minimum two elements in format [latitude, longitude, altitude]. Output in form [distance(WP1,WP2), altitude(WP1)]. Altitude is assumed to have little affect and it is not included in calculation."""
    #source1: http://en.wikipedia.org/wiki/Haversine_formula
    R_E=6371e3 #Earth's Radius in meters [2, google]
    
    def haversin(theta):
        """subfunction for special trig formula."""
        hsin=(1-cos(theta))/2.0
        return hsin
    def dist(lat1, lat2, lon1, lon2):
        """subfunction for calculating distance between two points using Haversine Formula referenced above."""
        d=2*R_E*asin(sqrt(haversin(lat2-lat1) +cos(lat1)*cos(lat2)*haversin(lon2-lon1)))
        return d

    out_dist=[]

    for i in range(len(coords)):
        [lat1, lon1]=[cs_lat, cs_lon]
        [lat2, lon2]=coords[i]
        lat1, lon1, lat2, lon2=map(radians,[lat1, lon1, lat2, lon2]) #convert to radians for trig functions
        temp_dist=dist(lat1, lat2, lon1, lon2)

        out_dist.append(temp_dist)
            
    return out_dist

"""Checks to see if UAV is currently within safe landing distance
of a safe landing waypoint"""

def safety_check(cs_alt,d_safe):

    safe_alt=[]

    for i in range(len(d_safe)):
        h_ideal = (1/LD_fixed)*d_safe[i]
        safe_alt.append(h_ideal)

    #Check individual safety zones 
    safetycheck = []
    for i in range(len(safe_alt)):
        if cs_alt > safe_alt[i]:
            safetycheck.append(1)
            print ("Safety WP%d currently reachable" %(i+1))
        else:
            safetycheck.append(0)

    #Check overall remaining flight safety zones 
    check = sum(safetycheck)
    if check > 0:
        print ("\nSafe landing zone(s) are available")
    else:
        print ("WARNING!! WARNING!!")
        print ("No safe landing points within range currently!")
        

