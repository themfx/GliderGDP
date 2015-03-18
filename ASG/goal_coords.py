from math import sin, asin, cos, atan2, radians


def new_coord(lat00, long00, angle, distance):
    """Attempt at finding lat and long from input data..."""
    # http://stackoverflow.com/questions/7278094/moving-a-cllocation-by-x-meters/20241963#20241963
    rad_earth = 6371e3          # Earth's radius [google]
    rad_d = 1.0*distance/rad_earth  # Radial distance between points.
    lat0, long0 = map(radians, [lat00, long00])
    lat = asin(sin(lat0)*cos(rad_d) + cos(lat0)*sin(rad_d)*cos(angle))
    lon = long0 + atan2(sin(angle)*sin(rad_d)*cos(lat0),
                        cos(rad_d) - sin(lat0)*sin(lat))

    return lat, lon
