#Laurence Jackson, lj8g10

#Wind corrected glide slope

def opt_glide(V_as,V_w):


    V = V_as + V_w              #air velocity over UAV
                                #+ve V_w represents a headwind

    #--------------------------------------------------------#
    #Glide ratio profile
    #From experimental data
    def L_D_profile(V):
        LD_V = (-0.0407*(V**2))+(2.9111*V)-5.0182
        return LD_V

    #--------------------------------------------------------#

    L_D = L_D_profile(V)

    print("Wind corrected L/D: %.2f" % L_D)


    

    

    

    
