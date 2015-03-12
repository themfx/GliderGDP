from __main__import v
import MissionPlanner
import clr
import time
import csv
import math
clr.AddReference("MissionPlanner.Utilities")
pi = math.pi

def DelayToHead(head,tol=10,wait=0.2):
    """
    Waits until a defined heading (head [deg]) is reached within a
    certain tolerance (tol [deg]), checking at regular intervals
    (wait [ms]).
    """
    print("Waiting for alignment to %.0f deg" %head)
    def t_(a):
        if a%360==0:
            a+=1e-6     # Avoid function asymptotes

        a = math.radians(a)     # Convert to radians
        return math.tan(0.5*(a-pi))

    # Find current ground course
    gc = v.attitude.yaw

    # Define heading window to fall between
    hU= head + tol
    hL= head - tol

    if t_(hU)>t_(hL):
        while (t_(gc)<t_(hL)) or (t_(gc)>t_(hU)):
            time.sleep(wait)
            gc = v.attitude.yaw    # Update gc
    else:
        while (t_(gc)<t_(hL)) and (t_(gc)>t_(hU)):
            time.sleep(wait)
            gc = v.attitude.yaw    # Update gc
    
    print(" - alignment confirmed (%.0f), proceeding" %gc)
    pass
        
def addLatLng(dx,dy,lat=cs.lat,lng=cs.lng):
    rE = 6368e3     # Radius of earth in m

    dlng = math.degrees(dx/rE)
    dlat = math.degrees(dy/rE)

    lat += dlat
    lng += dlng
    return (lat,lng)

def rCentre(r,h=cs.groundcourse):   #,U=cs.airspeed):
    d = r * (math.sqrt(3)-1)    # Offset for loiter centre
    hr= math.radians(h)         # Heading in radians

    dx = d*math.cos(hr) + (r+d)*math.sin(hr)
    dy = (r+d)*math.cos(hr) - d*math.sin(hr)

    print("rCentre calculated dx=%f, dy=%f" %(dx,dy))

    (lat,lng) = addLatLng(dx,dy)
    return (lat,lng)

def StartGlide(vT=10):
    """
    Initilises a glide with a certain target airspeed (vT [m/s]).
    """
    
    Script.ChangeParam("THR_MAX",0)
    print("THR_MAX=0")
    Script.ChangeParam("TRIM_ARSPD_CM",int(vT*100))
    Script.ChangeParam("LIM_PITCH_MAX",600)         # ac dep!!!
    
    pass

def ArtSoar(Talt=100):
    """
    Sets up an aritifical soar where the propellor is used to gain
    altitude up to a certain target (Talt [m]).
    """
    Script.ChangeMode("guided")
    print("Mode changed to 'guided'")

    print("Setting up temp WP")
    item = MissionPlanner.Utilities.Locationwp()

    # Setup loiter location
    #r = Script.GetParam("WP_LOITER_RAD")
    #print("WP_LOITER_RAD=%f" %r)
    #(lat,lng) = rCentre(r)
    lat = cs.lat
    lng = cs.lng
    MissionPlanner.Utilities.Locationwp.lat.SetValue(item,lat)
    MissionPlanner.Utilities.Locationwp.lng.SetValue(item,lng)
    MissionPlanner.Utilities.Locationwp.alt.SetValue(item,Talt)
    print("Sending MAV command")
    MAV.setGuidedModeWP(item)
    print(" - sent")

    Script.ChangeParam("THR_MAX",100)
    slam()

    # Removed this to slow soar
    #Script.ChangeParam("TRIM_ARSPD_CM",2200)
    #print("Target airspeed now 22m/s")
    pass

##################################################################

def GlideMonitor(wpEnd,RunName,vAir,t=200):
    """
    Monitors a glide up until a defined waypoint (wpEnd) by
    logging the time, airspeed and altitude over a certain
    sampling frequency (t [ms]). This is outputted to a csv file
    ...?
    """
    results = []

    # Initial parameters
    v_air = cs.airspeed
    alt = cs.alt
    lat = cs.lat
    lng = cs.lng
    
    begin = time.time()
    while cs.wpno != (wpEnd+1):
        #now = time.time()-begin
        
        alt = cs.alt
        if (cs.lat,cs.lng)!=(lat,lng):
            now= time.time() - begin
            alt = cs.alt
            lat = cs.lat
            lng = cs.lng
            
            results.append([now,v_air,alt,cs.pitch])

            # Update new v_air and alt
            v_air = cs.airspeed
            alt = cs.alt
        if Script.GetParam("TRIM_ARSPD_CM")!=(vAir*100):
            Script.ChangeParam("TRIM_ARSPD_CM",vAir*100)
        Script.Sleep(t)
    print("%d time steps taken, writing to file" %(len(results)))

    # Write results to file
    with open('results_%s.csv'%(RunName),'wb') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        for line in results:
            writer.writerow(line)
    return results

def _GMonitor(wpEnd,RunName,t=50):
    #OLD!!!
    v=[]
    LD=[]
    #begin = time.time()

    # Initial values
    T0 = time.time()
    #print('time set')
    V0 = cs.airspeed
    #print('v0 set')
    A0 = cs.alt
    #print('initial values set, sleeping')
    Script.Sleep(t)

    # Loop until reach end waypoint
    while cs.wpno != (wpEnd+1):
        # Calculate changes
        dT = time.time() - T0
        dA = A0 - cs.alt
        dX = V0 * dT
        if dA!=0:
            LD.append(dX/dA)
            v.append(V0)

            V0 = cs.airspeed
            T0 = time.time()
            A0 = cs.alt
            #v.append(V0)

        # Sleep until next time step
        Script.Sleep(t)

    # Write to file
    print("Captured %d results" %(len(v)))
    with open('results_%s.csv'%(RunName),'wb') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        for point in range(len(v)):
            writer.writerow([v[point],LD[point]])
    return (v,LD)

def plot_vLD(v,LD,title):
    plt.plot(v,LD,'.')
    plt.xlabel('Airspeed [m/s]')
    plt.ylabel('L/D')
    plt.savefig("%s.png"%(title))
    plt.close()

def rAnalyse(r):
    N=len(r)
    r_=r[int(0.3*N):int(0.9*N)]
    N_=len(r_)

    v_=0
    for line in r_:
        v_+=line[1]
    v_/=N_

    dAdt = (r_[-1][2]-r_[0][2])/(r_[-1][0]-r_[0][0])
    LD = v_/dAdt
    print("L/D value was %6.4f" %(LD))
    pass

##################################################################
# lj code
##################################################################
def inflight_stage(hA,hB,dAB):

    delta_h_ideal = (1./LD)*dAB           #ideal altitude change from current position
                                            #to target WP based on ideal glide slope

    ideal_alt = hB + delta_h_ideal          #ideal altitude

    if hA < ideal_alt:

        delta_h_diff = ideal_alt - hA

        E_req_AB = m*g*delta_h_diff
        
        #print ("More energy required!")
        #print ("Additional alt required en route = %.3f m" % delta_h_diff)
        #print ("Additional energy required en route = %.3f J" % E_req_AB)
        return delta_h_diff
        
    else:

        E_req_AB = 0
        
        #print ("No additional alt required to reach next WP")
        #print ("No additional energy required to reach next WP")
        return None
        
#--------------------------------------------------------------------#



"""UAV/glider flight parameters"""

m = 20.                     #UAV/glider mass
g = 9.81                    #gravitational constant
C_D = 0.05                   #total drag coefficient
C_L = 1.5                   #Cruise lift coefficient
LD = 14             # estimated ld
##################################################################
def MonitorH(wp):
    print("Monitoring flight to WP%d" %(wp))
    i=0
    while cs.wpno==wp:
        cAlt =cs.alt
        xtra = inflight_stage(cAlt,80,cs.wp_dist)
        if xtra!=None:
            print("Too low (%6fm) detected, correcting" %(xtra))
            tAlt=cs.alt+xtra*1.2    # includes safety factor
            if tAlt/cs.alt > 1.2:
                head = cs.nav_bearing
                ArtSoar(tAlt+5)
                DelayToAlt(tAlt)
                DelayToHead(head)
                print("Reached target alt, continuing")
                Script.ChangeMode('auto')
                StartGlide()
            else:
                print("Not climbing, dAlt too small (%f)" %xtra)
        Script.Sleep(1000)
##################################################################
def gsTest():
    resetParas()
    waitfor(3)
    StartGlide()
    for loop in [1,2,3]:
        for w in [3,4,2]:
            MonitorH(w)
        resetParas()
        print("Loop %d complete" %loop)
    print("Scriptomplete")


##################################################################

def latestGG():
    resetParas()
    for airspeed in [10,12,14,16,18,20]:
        print('Running loop for Vair=%d' %(airspeed))
        waitfor(4)
        StartGlide(airspeed)
        waitfor(4+1)
        #waitfor(4+2)
        r=GlideMonitor(5,'SouthRun_%d'%(airspeed),airspeed)
        resetParas()
        rAnalyse(r)
        #plot_vLD(v,LD,'SouthRun')
        waitfor(8)
        StartGlide(airspeed)
        waitfor(8+1)
        #waitfor(8+2)
        r=GlideMonitor(9,'NorthRun_%d'%(airspeed),airspeed)
        resetParas()
        rAnalyse(r)
        #plot_vLD(v,LD,'NorthRun')
        print('complete')

# dont forget to get mp to loop wps!

##################################################################

def origGG():
    resetParas()
    DelayToAlt(95)
    for i in range(5):
        StartGlide()
        MonitorAltDrop()
        resetParas()
        ArtSoar()
        #StartGlide(95)
        DelayToAlt(95)
        Script.ChangeMode("auto")
    print("### Script complete ###")
##################################################################
##################################################################
test = 'GS'

if test=='GS':
    gsTest()
elif test=='LD':
    latestGG()
##################################################################
##################################################################
