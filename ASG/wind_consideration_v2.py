# --- Laurence Jackson, lj8g10 ---
# This code uses the glide polar for the UAV (obtained through
#  wind tunnel testing) to calculate current L/D ratio accounting
#  for the effects of head/tailwinds and sink/rising air mass.
#  The equations used below were obtained analytically.

# Note: positive Vw is defined as a headwind
#       positive Vs is defined as a sinking air mass
#       A,B,C are the glide polar coefficients (quadratic
#		relation)

def Current_LD(V,Vw,Vs,A,B,C):
	# Sink rate as a function of airspeed
	Vv = (A*(V**2.))+(B*V)+C
	# Gradient of line representing glide angle
	grad = (Vv-Vs)/(V-Vw)

    LD_actual = -1./grad
    return LD_actual





    
