# Characteristics of active aircraft

# WARNING: needs matching to UAV demo before FT02

#aircraft
m = 4.99		# mass [kg]

#Glide polar Coefficients
A = -0.0236    #V^2 coefficient
B = 0.4023      #V coefficient
C = -2.2389      #Constant

#Zero wind optimal L/D ratio
#LD_neutral = 17.43
LD_fixed = 9.00      # based on 5m/s headwind (approx. 11.2mph)

#operational
hmax = 90.0		# maximum flight ceiling [m]
hmin = 8.0		# minimum safe flight altitude [m]
SF = 0.9		# Safety Factor

#global
g = 9.81		# gravitational acceleration [m/s^2]

# Wind info
wVel = 0.0		# current wind velocity
wDir = 0.0		# current wind direction
