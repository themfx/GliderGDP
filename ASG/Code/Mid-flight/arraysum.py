# A sum function to add up the elements in an array up to a given value, N
# Laurence Jackso, lj8g10
# updated by wilhelm munthe, wm4g10 27/01/2015


def arraysum(a, N):        # new slightly faster arraysum.
    return float(sum(a[:N]))

#def arraysum(a, N):
#    s = []
#    for i in range(N):
#        s.append(a[i])
#
#    arsum = sum(s)
#
#    return float(arsum)
#        
